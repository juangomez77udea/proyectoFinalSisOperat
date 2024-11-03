import asyncio
from md5_generator import MD5Hash

async def generate_md5_concurrently(data_list):
    loop = asyncio.get_event_loop()
    tasks = [loop.run_in_executor(None, MD5Hash.genera_md5, data.encode()) for data in data_list]
    return await asyncio.gather(*tasks)
