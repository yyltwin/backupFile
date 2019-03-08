#!/usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio
import re
import aiohttp
import aiomysql
from pyquery import PyQuery

import sys
print(sys.version)


start_url = "http://www.jobbole.com"
waiting_urls = []
seen_url = set()


stopping = False

sem = asyncio.Semaphore(3)


async def fetch(url, session):
    # async with sem:
    try:
        async with session.get(url) as resp:
            print("url status: ", resp.status)
            if resp.status in [200, 201]:
                data = await resp.text()
                return data
    except Exception as e:
        print(e)


def extract_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startswith("http") and url not in seen_url:
            urls.append(url)
            waiting_urls.append(url)
    return urls


async def init_urls(url, session):
    html = await fetch(start_url, session)
    seen_url.add(html)
    extract_urls(html)


async def atricle_handler(url, session, pool):
    html = await fetch(url, session)
    seen_url.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            insert_sql = "insert into article_test(title) values('{}')".format(title)
            await cur.execute(insert_sql)


async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waiting_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            url = waiting_urls.pop()
            print("start get url:", url)
            if re.match('http://.*?jobbole.com/\d+/', url):
                if url not in seen_url:
                    asyncio.ensure_future(atricle_handler(url, session, pool))
                    # await asyncio.sleep(30)
            # else:
            #     if url not in seen_url:
            #         asyncio.ensure_future(init_urls(url, session))


async def main(loop):  # 建立连接池
    pool = await aiomysql.create_pool(host="127.0.0.1", port=3306,
                                      user='root', password='root',
                                      db='spider_test', loop=loop, charset='utf8',
                                      autocommit=True)

    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        seen_url.add(start_url)
        extract_urls(html)

    # asyncio.ensure_future(init_urls(start_url))
    asyncio.ensure_future(consumer(pool))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()
