import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from modules.serialize_and_deserialize import serialize_public_key, serialize_private_key, write_bytes_text


class KeyGenerator:
    """Hybrid System Key Generation
        Methods:
            __init__(): class initializer
            __call__(): a method can make an instance of a class behave like a function
            get_symmetric_key(): getting a symmetric key
            generate_asymmetric_keys(): getting asymmetric keys
            serialize_asymmetric_keys(): serialize private and publix asymmetric keys
            encrypt_symmetric_encryption_key_with_public(): encrypt the symmetric encryption key with a public key
    """
    def __init__(self, path_serialize_encrypted_symmetric_key: str,
                 path_serialize_public_key: str, path_serialize_private_key: str) -> None:
        """Class initializer
            Args:
                path_serialize_encrypted_symmetric_key: path to serialize the encrypted symmetric key
                path_serialize_public_key: path to serialize the public key
                path_serialize_private_key: path to serialize the private key
        """
        self.__path_encrypted_symmetric_key = path_serialize_encrypted_symmetric_key
        self.__path_public_key = path_serialize_public_key
        self.__path_private_key = path_serialize_private_key
        self.__public_key = None
        self.__private_key = None
        self.__symmetric_key = os.urandom(16)

    def get_symmetric_key(self) -> bytes:
        """Getting a symmetric key
            Returns:
                symmetric key
        """
        return self.__symmetric_key

    def generate_asymmetric_keys(self) -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        """Getting asymmetric keys
            Returns:
                a pair of keys (public and private)
        """
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.__private_key = keys
        self.__public_key = keys.public_key()
        return self.__public_key, self.__private_key

    def serialize_asymmetric_keys(self) -> None:
        """Serialize private and publix asymmetric keys"""
        serialize_public_key(self.__path_public_key, self.__public_key)
        serialize_private_key(self.__path_private_key, self.__private_key)

    def encrypt_symmetric_encryption_key_with_public(self) -> None:
        """Encrypt the symmetric encryption key with a public key and save it in the specified path"""
        encryption_key = self.__public_key.encrypt(self.__symmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                algorithm=hashes.SHA256(), label=None))
        write_bytes_text(self.__path_encrypted_symmetric_key, encryption_key)

    def __call__(self) -> None:
        """A method can make an instance of a class behave like a function"""
        print(f"Симметричный ключ: {self.get_symmetric_key()}")
        self.generate_asymmetric_keys()
        print(f"Публичный ключ: {self.__public_key}")
        print(f"Секретный ключ: {self.__private_key}")
        self.serialize_asymmetric_keys()
        self.encrypt_symmetric_encryption_key_with_public()
