from flask import current_app as app
from cryptography.fernet import Fernet

key = app.config["SECRET_KEY"]
fernet = Fernet(key)


def encrypt_id(data: bytes) -> bytes:
    """
    @param data: bytes
    @return: bytes
    """
    encrypted_id: bytes = fernet.encrypt(data)
    return encrypted_id


def decrypt_id(encrypted_id: bytes) -> int:
    """
    @param encrypted_id: bytes
    @return: bytes
    """
    decrypted_id_in_byte: bytes = fernet.decrypt(encrypted_id)
    decrypted_id = int(decrypted_id_in_byte.decode())
    return decrypted_id
