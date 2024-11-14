from sha256_hash import sha256_parallel, sha256_concurrent
from md5_hash import md5_parallel, md5_concurrent
from blake_hash import blake_parallel, blake_concurrent
from benchmark import benchmark
from utils import parse_input
from script_generator_archive import select_file_size

def run_benchmark(algorithm, input_type, input_data, num_threads):
    algorithms = {
        "sha256": {"parallel": sha256_parallel, "concurrent": sha256_concurrent},
        "md5": {"parallel": md5_parallel, "concurrent": md5_concurrent},
        "blake": {"parallel": blake_parallel, "concurrent": blake_concurrent}
    }

    selected_algorithm = algorithms.get(algorithm)
    if not selected_algorithm:
        print(f"Algoritmo {algorithm} no soportado.")
        return

    # Procesar el input_data si es texto
    if input_type == "text":
        input_data = parse_input(input_data)

    # Evaluación en modo paralelo
    print(f"\nEvaluando {algorithm} en modo paralelo con {num_threads} hilos...")
    parallel_metrics = benchmark(selected_algorithm["parallel"], input_data, num_threads)
    print("Resultado (Paralelo):", parallel_metrics["result"])
    print(f"Tiempo (Paralelo): {parallel_metrics['time']} segundos")
    print(f"Uso de memoria (Paralelo): {parallel_metrics['memory']} MB")
    print(f"Memoria máxima (Paralelo): {parallel_metrics['peak_memory']} MB")
    print(f"Uso de CPU (Paralelo): {parallel_metrics['cpu']}%")

    # Evaluación en modo concurrente
    print(f"\nEvaluando {algorithm} en modo concurrente con {num_threads} hilos...")
    concurrent_metrics = benchmark(selected_algorithm["concurrent"], input_data, num_threads)
    print("Resultado (Concurrente):", concurrent_metrics["result"])
    print(f"Tiempo (Concurrente): {concurrent_metrics['time']} segundos")
    print(f"Uso de memoria (Concurrente): {concurrent_metrics['memory']} MB")
    print(f"Memoria máxima (Concurrente): {concurrent_metrics['peak_memory']} MB")
    print(f"Uso de CPU (Concurrente): {concurrent_metrics['cpu']}%")

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
            print("\nSelecciona el Tamaño del Archivo a Generar:")
            print("1 - 1 MB\n2 - 5 MB\n3 - 10 MB\n4 - 50 MB\n5 - 100 MB")
            file_option = input("Opción: ")
            file_path = select_file_size(file_option)  # Generar el archivo de prueba según la opción seleccionada
            input_data = file_path
        else:
            input_data = input("Introduce los datos a hashear (separados por comas si son múltiples): ")

        # Solicitar el número de hilos
        num_threads = int(input("¿Cuántos hilos deseas usar para la evaluación? (1-8): "))
        run_benchmark(algorithm, input_type, input_data, num_threads)

if __name__ == "__main__":
    main()