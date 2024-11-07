# utils.py
#Función para leer archivos y convertir datos de entrada.

def read_file_in_blocks(file_path, block_size=1024*1024):
    with open(file_path, 'rb') as f:
        while chunk := f.read(block_size):
            yield chunk

def parse_input(input_data):
    return input_data.split(',') if isinstance(input_data, str) else [str(input_data)]
