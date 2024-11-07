# blake_hash.py
import hashlib
from multiprocessing import Pool
import concurrent.futures
from utils import read_file_in_blocks, parse_input

def blake_hash(data):
    # Codificar la entrada si es una cadena de texto
    if isinstance(data, str):
        data = data.encode()  # Convertir la cadena en bytes
    hash_obj = hashlib.blake2b()
    hash_obj.update(data)
    return hash_obj.hexdigest()

def blake_parallel(blocks):
    with Pool() as pool:
        return pool.map(blake_hash, blocks)

def blake_concurrent(blocks):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        return list(executor.map(blake_hash, blocks))

def blake_file_parallel(file_path):
    blocks = read_file_in_blocks(file_path)
    return blake_parallel(blocks)

def blake_file_concurrent(file_path):
    blocks = read_file_in_blocks(file_path)
    return blake_concurrent(blocks)
