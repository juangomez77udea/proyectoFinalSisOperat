# hash_generator.py
import hashlib

class HASH:
    @staticmethod
    def generaHash(datos, algoritmo="sha256"):
        h = hashlib.new(algoritmo)
        h.update(datos)
        return h.hexdigest()
