# parallel_hash.py
from multiprocessing import Pool
from hash_generator import HASH

def generate_hash_in_parallel(data_list, algorithm="sha256"):
    with Pool() as pool:
        results = pool.starmap(HASH.generaHash, [(data.encode(), algorithm) for data in data_list])
    return results
