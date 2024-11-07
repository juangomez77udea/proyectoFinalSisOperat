# sha256_hash.py
import hashlib
from multiprocessing import Pool
import concurrent.futures
from utils import read_file_in_blocks, parse_input

def sha256_hash(data):
    hash_obj = hashlib.sha256()
    hash_obj.update(data.encode())
    return hash_obj.hexdigest()

def sha256_parallel(data_list):
    with Pool() as pool:
        return pool.map(sha256_hash, data_list)

def sha256_concurrent(blocks):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        return list(executor.map(sha256_hash, blocks))

def sha256_file_parallel(file_path):
    blocks = read_file_in_blocks(file_path)
    return sha256_parallel(blocks)

def sha256_file_concurrent(file_path):
    blocks = read_file_in_blocks(file_path)
    return sha256_concurrent(blocks)
