import time
import psutil
import os

def benchmark(algorithm_func, input_data, num_threads):
    # Medir el tiempo de ejecución
    start_time = time.time()

    # Ejecutar la función del algoritmo con los datos de entrada y el número de hilos
    result = algorithm_func(input_data, num_threads)

    # Medir el tiempo de ejecución después de la ejecución del algoritmo
    end_time = time.time()

    # Medición de otros parámetros
    memory_usage = psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024)  # en MB
    peak_memory = memory_usage  # Para este ejemplo, se puede hacer más detallado
    cpu_usage = psutil.cpu_percent()

    # Devolver las métricas
    metrics = {
        "result": result,
        "time": end_time - start_time,
        "memory": memory_usage,
        "peak_memory": peak_memory,
        "cpu": cpu_usage
    }

    return metrics