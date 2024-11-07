# md5_hash.py
import hashlib
from multiprocessing import Pool
import concurrent.futures
from utils import read_file_in_blocks, parse_input

def md5_hash(data):
    # Codificar la entrada si es una cadena de texto
    if isinstance(data, str):
        data = data.encode()  # Convertir la cadena en bytes
    hash_obj = hashlib.md5()
    hash_obj.update(data)
    return hash_obj.hexdigest()

def md5_parallel(blocks):
    with Pool() as pool:
        return pool.map(md5_hash, blocks)

def md5_concurrent(blocks):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        return list(executor.map(md5_hash, blocks))

def md5_file_parallel(file_path):
    blocks = read_file_in_blocks(file_path)
    return md5_parallel(blocks)

def md5_file_concurrent(file_path):
    blocks = read_file_in_blocks(file_path)
    return md5_concurrent(blocks)
