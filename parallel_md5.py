from multiprocessing import Pool
from md5_generator import MD5Hash

def generate_md5_in_parallel(data_list):
    with Pool() as pool:
        results = pool.map(MD5Hash.genera_md5, [data.encode() for data in data_list])
    return results
