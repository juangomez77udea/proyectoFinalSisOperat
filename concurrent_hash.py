# concurrent_hash.py
import asyncio
from hash_generator import HASH

async def generate_hash_concurrently(data_list, algorithm="sha256"):
    loop = asyncio.get_event_loop()
    tasks = [loop.run_in_executor(None, HASH.generaHash, data.encode(), algorithm) for data in data_list]
    return await asyncio.gather(*tasks)
