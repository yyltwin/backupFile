#!/usr/bin/env python
# -*- coding:utf-8 -*-

import aiohttp

import asyncio

from asyncio import Lock, Queue

cache = {}
lock = Lock()


async def get_stuff(url):
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request("GET", url)
        cache[url] = stuff
        return stuff


async def parse_stuff():
    stuff = await get_stuff("http://www.baidu.com")
    print(stuff)


async def use_stuff():
    stuff = await get_stuff("http://www.baidu.com")
    print(stuff)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([use_stuff(), parse_stuff(), get_stuff("http://www.baidu.com")]))