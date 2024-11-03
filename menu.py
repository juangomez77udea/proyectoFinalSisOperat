# main.py
import asyncio
from parallel_md5 import generate_md5_in_parallel
from concurrent_md5 import generate_md5_concurrently
from parallel_hash import generate_hash_in_parallel  # SHA-256
from concurrent_hash import generate_hash_concurrently  # SHA-256
from parallel_blake import generate_blake_in_parallel  # BLAKE
from concurrent_blake import generate_blake_concurrently  # BLAKE

def main():
    x = 0
    while x < 1:
        print("Elige el número del algoritmo a usar: ")
        print("1-SHA256")
        print("2-MD5")
        print("3-BLAKE")
        print("4-Acabar el programa")
        nAlgoritmo = int(input())

        if nAlgoritmo == 4:
            x = 1
            break

        print("Introduce datos a hashear (separados por comas si son múltiples): ")
        datos = input().split(',')

        print("Seleccione el método de procesamiento:")
        print("1- Paralelo")
        print("2- Concurrente")
        metodo = int(input())

        if nAlgoritmo == 1:  # SHA256
            if metodo == 1:
                hashes = generate_hash_in_parallel(datos)
                print("\nHashes SHA256 generados en paralelo:", hashes)
            elif metodo == 2:
                hashes = asyncio.run(generate_hash_concurrently(datos))
                print("\nHashes SHA256 generados concurrentemente:", hashes)

        elif nAlgoritmo == 2:  # MD5
            if metodo == 1:
                hashes = generate_md5_in_parallel(datos)
                print("\nHashes MD5 generados en paralelo:", hashes)
            elif metodo == 2:
                hashes = asyncio.run(generate_md5_concurrently(datos))
                print("\nHashes MD5 generados concurrentemente:", hashes)

        elif nAlgoritmo == 3:  # BLAKE
            if metodo == 1:
                hashes = generate_blake_in_parallel(datos)
                print("\nHashes BLAKE generados en paralelo:", hashes)
            elif metodo == 2:
                hashes = asyncio.run(generate_blake_concurrently(datos))
                print("\nHashes BLAKE generados concurrentemente:", hashes)
        else:
            print("Método no válido. Intente de nuevo.")
            continue

if __name__ == "__main__":
    main()
