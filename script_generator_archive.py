import os
import random
import string

# Ruta para el escritorio
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Crear la carpeta Desktop si no existe
if not os.path.exists(desktop_path):
    os.makedirs(desktop_path)


def generate_random_text_file(file_name, size_in_bytes):
    file_path = os.path.join(desktop_path, file_name)
    with open(file_path, "w") as f:
        while f.tell() < size_in_bytes:
            random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=100)) + '\n'
            f.write(random_text)

    print(
        f"Archivo '{file_name}' creado con éxito en el escritorio con un tamaño aproximado de {size_in_bytes / (1024 * 1024):.2f} MB.")
    print(f"Ruta completa del archivo generado: {file_path}")


def main():
    print("Seleccione el tamaño del archivo a generar:")
    print("1 - 1 MB")
    print("2 - 5 MB")
    print("3 - 10 MB")
    print("4 - 50 MB")
    print("5 - 100 MB")

    option = input("Opción: ")

    file_sizes = {
        "1": 1 * 1024 * 1024,
        "2": 5 * 1024 * 1024,
        "3": 10 * 1024 * 1024,
        "4": 50 * 1024 * 1024,
        "5": 100 * 1024 * 1024
    }

    if option in file_sizes:
        size_in_bytes = file_sizes[option]
        file_name = f"archivo_prueba_{size_in_bytes // (1024 * 1024)}MB.txt"
        generate_random_text_file(file_name, size_in_bytes)
    else:
        print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
