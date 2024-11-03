import asyncio
import tracemalloc
import timeit
from parallel_hash import generate_hash_in_parallel  # SHA-256 paralelo
from concurrent_hash import generate_hash_concurrently  # SHA-256 concurrente
from parallel_md5 import generate_md5_in_parallel  # MD5 paralelo
from concurrent_md5 import generate_md5_concurrently  # MD5 concurrente
from parallel_blake import generate_blake_in_parallel  # BLAKE paralelo
from concurrent_blake import generate_blake_concurrently  # BLAKE concurrente

def benchmark(func, *args):
    # Inicia medición de uso de la memoria
    tracemalloc.start()

    start_time = timeit.default_timer()
    result = func(*args)
    elapsed_time = timeit.default_timer() - start_time

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Convertimos la memoria de bytes a MB
    memory_usage = current / (1024 * 1024)
    peak_memory_usage = peak / (1024 * 1024)

    return result, elapsed_time, memory_usage, peak_memory_usage

def main():
    while True:
        print("Elige el número del algoritmo a usar: ")
        print("1 - SHA256")
        print("2 - MD5")
        print("3 - BLAKE")
        print("4 - Acabar el programa")
        nAlgoritmo = int(input())

        if nAlgoritmo == 4:
            break

        print("Introduce datos a hashear (separados por comas si son múltiples): ")
        datos = input().split(',')

        if nAlgoritmo == 1:  # SHA256
            print("\n...Ejecutando SHA256 en modo paralelo con medición de eficiencia...")
            hashes_paralelo, tiempo_paralelo, memoria_paralelo, pico_memoria_paralelo = benchmark(generate_hash_in_parallel, datos)
            print("Hashes SHA256 generados en paralelo:", hashes_paralelo)
            print(f"Tiempo de ejecución: {tiempo_paralelo:.6f} segundos")
            print(f"Memoria utilizada: {memoria_paralelo:.6f} MB; Pico de memoria: {pico_memoria_paralelo:.6f} MB\n")

            print("Ejecutando SHA256 en modo concurrente con medición de eficiencia...")
            hashes_concurrente, tiempo_concurrente, memoria_concurrente, pico_memoria_concurrente = benchmark(asyncio.run, generate_hash_concurrently(datos))
            print("Hashes SHA256 generados concurrentemente:", hashes_concurrente)
            print(f"Tiempo de ejecución: {tiempo_concurrente:.6f} segundos")
            print(f"Memoria utilizada: {memoria_concurrente:.6f} MB; Pico de memoria: {pico_memoria_concurrente:.6f} MB\n")

        elif nAlgoritmo == 2:  # MD5
            print("\nEjecutando MD5 en modo paralelo con medición de eficiencia...")
            hashes_paralelo, tiempo_paralelo, memoria_paralelo, pico_memoria_paralelo = benchmark(generate_md5_in_parallel, datos)
            print("Hashes MD5 generados en paralelo:", hashes_paralelo)
            print(f"Tiempo de ejecución: {tiempo_paralelo:.6f} segundos")
            print(f"Memoria utilizada: {memoria_paralelo:.6f} MB; Pico de memoria: {pico_memoria_paralelo:.6f} MB\n")

            print("Ejecutando MD5 en modo concurrente con medición de eficiencia...")
            hashes_concurrente, tiempo_concurrente, memoria_concurrente, pico_memoria_concurrente = benchmark(asyncio.run, generate_md5_concurrently(datos))
            print("Hashes MD5 generados concurrentemente:", hashes_concurrente)
            print(f"Tiempo de ejecución: {tiempo_concurrente:.6f} segundos")
            print(f"Memoria utilizada: {memoria_concurrente:.6f} MB; Pico de memoria: {pico_memoria_concurrente:.6f} MB\n")

        elif nAlgoritmo == 3:  # BLAKE
            print("\nEjecutando BLAKE en modo paralelo con medición de eficiencia...")
            hashes_paralelo, tiempo_paralelo, memoria_paralelo, pico_memoria_paralelo = benchmark(generate_blake_in_parallel, datos)
            print("Hashes BLAKE generados en paralelo:", hashes_paralelo)
            print(f"Tiempo de ejecución: {tiempo_paralelo:.6f} segundos")
            print(f"Memoria utilizada: {memoria_paralelo:.6f} MB; Pico de memoria: {pico_memoria_paralelo:.6f} MB\n")

            print("Ejecutando BLAKE en modo concurrente con medición de eficiencia...")
            hashes_concurrente, tiempo_concurrente, memoria_concurrente, pico_memoria_concurrente = benchmark(asyncio.run, generate_blake_concurrently(datos))
            print("Hashes BLAKE generados concurrentemente:", hashes_concurrente)
            print(f"Tiempo de ejecución: {tiempo_concurrente:.6f} segundos")
            print(f"Memoria utilizada: {memoria_concurrente:.6f} MB; Pico de memoria: {pico_memoria_concurrente:.6f} MB\n")

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
