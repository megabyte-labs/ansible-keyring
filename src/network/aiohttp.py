""" aiohttp is an asynchronous http client for python """

import asyncio
from aiohttp import ClientSession


async def fetch(sem, url, session):
    # Fetch function with semaphore.
    async with sem:
        async with session.get(url) as response:
            return await response.read()


async def run():
    url = "http://google.com/"
    tasks = []
    # create instance of Semaphore with max tasks set to 1k
    sem = asyncio.Semaphore(1000)

    # Use ClientSession so that we don't open a new connection per request
    async with ClientSession() as session:
        for i in range(25):
            task = asyncio.ensure_future(fetch(sem, url.format(i), session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses


asyncio.run(run)
