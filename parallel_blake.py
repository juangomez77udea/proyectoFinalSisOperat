from multiprocessing import Pool
from blake_generator import BlakeHash

def generate_blake_in_parallel(data_list):
    with Pool() as pool:
        results = pool.map(BlakeHash.genera_blake, [data.encode() for data in data_list])
    return results
