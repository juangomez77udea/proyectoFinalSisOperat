import hashlib
from concurrent.futures import ThreadPoolExecutor
import threading


def blake_hash(input_data):
    if isinstance(input_data, str):
        data = input_data.encode('utf-8')
    elif isinstance(input_data, bytes):
        data = input_data
    else:
        raise ValueError("Input must be a string or bytes")

    hash_obj = hashlib.blake2b()
    hash_obj.update(data)
    result = hash_obj.hexdigest()

    current_thread = threading.current_thread()
    print(f'Hilo: {current_thread.name}, '
          f'Identificador: {current_thread.ident}, '
          f'Resultado del hash: {result[:8]}...')
    return result


def blake_parallel(input_data, num_threads):
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')

    chunk_size = max(1, len(input_data) // num_threads)
    chunks = [input_data[i:i + chunk_size] for i in range(0, len(input_data), chunk_size)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(blake_hash, chunks))

    return ''.join(results)


def blake_concurrent(input_data, num_threads):
    return blake_parallel(input_data, num_threads)


def blake_file_parallel(file_path, num_threads):
    from utils import read_file_in_blocks
    blocks = list(read_file_in_blocks(file_path))
    return blake_parallel(b''.join(blocks), num_threads)


def blake_file_concurrent(file_path, num_threads):
    return blake_file_parallel(file_path, num_threads)