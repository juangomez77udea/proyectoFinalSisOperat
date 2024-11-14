import hashlib
from concurrent.futures import ThreadPoolExecutor
import threading


def sha256_partial_hash(chunk):
    hash_obj = hashlib.sha256()
    hash_obj.update(chunk)
    current_thread = threading.current_thread()
    print(f'Hilo: {current_thread.name}, '
          f'Identificador: {current_thread.ident}, '
          f'Hash parcial calculado')
    return hash_obj.digest()


def sha256_parallel(input_data, num_threads):
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    elif not isinstance(input_data, bytes):
        raise ValueError("Input must be a string or bytes")

    # Ensure we have at least num_threads chunks
    chunk_size = max(1, len(input_data) // num_threads)
    chunks = [input_data[i:i + chunk_size] for i in range(0, len(input_data), chunk_size)]

    # If we have fewer chunks than threads, add empty chunks
    while len(chunks) < num_threads:
        chunks.append(b'')

    # If we have more chunks than threads, combine extra chunks into the last one
    if len(chunks) > num_threads:
        chunks[num_threads - 1:] = [b''.join(chunks[num_threads - 1:])]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        partial_hashes = list(executor.map(sha256_partial_hash, chunks))

    # Combine partial hashes
    final_hash = hashlib.sha256()
    for partial_hash in partial_hashes:
        final_hash.update(partial_hash)

    return final_hash.hexdigest()


def sha256_concurrent(input_data, num_threads):
    return sha256_parallel(input_data, num_threads)


def sha256_file_parallel(file_path, num_threads):
    with open(file_path, 'rb') as file:
        return sha256_parallel(file.read(), num_threads)


def sha256_file_concurrent(file_path, num_threads):
    return sha256_file_parallel(file_path, num_threads)