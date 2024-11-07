# benchmark.py
#mide el tiempo y la memoria utilizada al calcular el hash.

import tracemalloc
import timeit

def benchmark(func, *args):
    tracemalloc.start()
    start_time = timeit.default_timer()

    result = func(*args)

    elapsed_time = timeit.default_timer() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    memory_usage = current / (1024 * 1024)  # MB
    peak_memory_usage = peak / (1024 * 1024)  # MB

    return result, elapsed_time, memory_usage, peak_memory_usage