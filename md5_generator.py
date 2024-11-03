import hashlib

class MD5Hash:
    @staticmethod
    def genera_md5(datos):
        h = hashlib.md5()
        h.update(datos)
        return h.hexdigest()
