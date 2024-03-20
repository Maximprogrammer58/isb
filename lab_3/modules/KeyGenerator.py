import os
import logging

from serialize_and_deserialize import serialize_public_key, serialize_private_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

logging.basicConfig(level=logging.INFO)

class KeyGenerator:
    def __init__(self, path_serialize_encrypted_symmetric_key: str,
                 path_serialize_public_key: str,  path_serialize_private_key: str) -> None:
        self.__path_encrypted_symmetric_key = path_serialize_encrypted_symmetric_key
        self.__path_public_key = path_serialize_public_key
        self.__path_private_key = path_serialize_private_key
        self.__public_key = None
        self.__private_key = None
        self.__symmetric_key = os.urandom(16)

    def get_symmetric_key(self) -> bytes:
        return self.__symmetric_key

    def generate_asymmetric_keys(self) -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.__private_key = keys
        self.__public_key = keys.public_key()
        return self.__public_key, self.__private_key

    def serialize_asymmetric_keys(self) -> None:
        serialize_public_key(self.__path_public_key, self.__public_key)
        serialize_private_key(self.__path_private_key, self.__private_key)

    def encrypt_symmetric_encryption_key_with_public(self) -> None:
        try:
            encryption_key = self.__public_key.encrypt(self.generate_symmetric_key(), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
            with open(self.__path_encrypted_symmetric_key, 'wb') as key_file:
                key_file.write(encryption_key)
        except Exception as error:
            logging.error(error)