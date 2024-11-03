# blake_generator.py
import hashlib

class BlakeHash:
    @staticmethod
    def genera_blake(datos):
        h = hashlib.blake2b()
        h.update(datos)
        return h.hexdigest()
