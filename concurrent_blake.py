import asyncio
from blake_generator import BlakeHash

async def generate_blake_concurrently(data_list):
    loop = asyncio.get_event_loop()
    tasks = [loop.run_in_executor(None, BlakeHash.genera_blake, data.encode()) for data in data_list]
    return await asyncio.gather(*tasks)
