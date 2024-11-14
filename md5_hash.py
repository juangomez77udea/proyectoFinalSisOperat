import hashlib
from concurrent.futures import ThreadPoolExecutor
import threading

def md5_hash(chunk):
    hash_obj = hashlib.md5()
    hash_obj.update(chunk)
    result = hash_obj.hexdigest()

    current_thread = threading.current_thread()
    print(f'Hilo: {current_thread.name}, '
          f'Identificador: {current_thread.ident}, '
          f'Resultado del hash: {result[:8]}...')
    return result

def md5_parallel(input_data, num_threads):
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')

    chunk_size = max(1, len(input_data) // num_threads)
    chunks = [input_data[i:i + chunk_size] for i in range(0, len(input_data), chunk_size)]

    while len(chunks) < num_threads:
        chunks.append(b'')

    if len(chunks) > num_threads:
        chunks[num_threads-1:] = [b''.join(chunks[num_threads-1:])]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(md5_hash, chunks))

    return ''.join(results)

def md5_concurrent(input_data, num_threads):
    return md5_parallel(input_data, num_threads)

def md5_file_parallel(file_path, num_threads):
    with open(file_path, 'rb') as file:
        return md5_parallel(file.read(), num_threads)

def md5_file_concurrent(file_path, num_threads):
    return md5_file_parallel(file_path, num_threads)