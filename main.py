from sha256_hash import sha256_parallel, sha256_concurrent
from md5_hash import md5_parallel, md5_concurrent
from blake_hash import blake_parallel, blake_concurrent
from benchmark import benchmark
from utils import parse_input

def run_benchmark(algorithm, input_type, input_data):
    # Diccionario de funciones para cada algoritmo en modo paralelo y concurrente
    algorithms = {
        "sha256": {
            "parallel": sha256_parallel,
            "concurrent": sha256_concurrent
        },
        "md5": {
            "parallel": md5_parallel,
            "concurrent": md5_concurrent
        },
        "blake": {
            "parallel": blake_parallel,
            "concurrent": blake_concurrent
        }
    }

    # Obtener las funciones correspondientes para el algoritmo seleccionado
    selected_algorithm = algorithms.get(algorithm)

    if selected_algorithm:
        # Procesar el input_data para asegurar que sea una lista de elementos únicos
        if input_type == "text":
            input_data = parse_input(input_data)

        # Evaluar en modo paralelo
        print(f"\nEvaluando {algorithm} en modo paralelo...")
        parallel_result, parallel_time, parallel_mem, parallel_peak_mem = benchmark(selected_algorithm["parallel"], input_data)
        print(f"Resultado (Paralelo): {parallel_result}")
        print(f"Tiempo (Paralelo): {parallel_time} segundos")
        print(f"Uso de memoria (Paralelo): {parallel_mem} MB")
        print(f"Memoria máxima (Paralelo): {parallel_peak_mem} MB")

        # Evaluar en modo concurrente
        print(f"\nEvaluando {algorithm} en modo concurrente...")
        concurrent_result, concurrent_time, concurrent_mem, concurrent_peak_mem = benchmark(selected_algorithm["concurrent"], input_data)
        print(f"Resultado (Concurrente): {concurrent_result}")
        print(f"Tiempo (Concurrente): {concurrent_time} segundos")
        print(f"Uso de memoria (Concurrente): {concurrent_mem} MB")
        print(f"Memoria máxima (Concurrente): {concurrent_peak_mem} MB")
    else:
        print(f"Algoritmo {algorithm} no soportado.")

def main():
    while True:
        print("\nSelecciona el Algoritmo de Hash:")
        print("1 - SHA256\n2 - MD5\n3 - BLAKE\n4 - Salir")
        alg_choice = int(input("Opción: "))
        if alg_choice == 4:
            break

        # Mapear la opción seleccionada al nombre del algoritmo
        algorithms = {1: "sha256", 2: "md5", 3: "blake"}
        algorithm = algorithms.get(alg_choice)

        # Solicitar el tipo de entrada
        print("\nSelecciona el Tipo de Entrada:")
        print("1 - Archivo\n2 - Texto o Número")
        input_type = "file" if int(input("Opción: ")) == 1 else "text"

        if input_type == "file":
            file_path = input("Introduce la ruta del archivo: ")
            run_benchmark(algorithm, "file", file_path)
        else:
            input_data = input("Introduce los datos a hashear (separados por comas si son múltiples): ")
            run_benchmark(algorithm, "text", input_data)

if __name__ == "__main__":
    main()
