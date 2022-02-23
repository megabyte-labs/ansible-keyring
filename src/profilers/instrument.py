"""
PyInstrument is a very simple to use python profiler that helps you find
bottlenecks in your software.
"""

import asyncio
from pyinstrument import Profiler


async def example():
    p = Profiler(async_mode='disabled')

    # Basically run our code within the profiler's context...
    with p:
        print('Started...')
        await asyncio.sleep(1)
        print('Finished!')

    # Then, check the profiler results
    p.print()


asyncio.run(example())
