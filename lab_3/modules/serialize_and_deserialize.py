import logging

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


logging.basicConfig(level=logging.INFO)


def serialize_symmetric_key(path: str, key: bytes) -> None:
    try:
        with open(path, 'wb') as key_file:
            key_file.write(key)
    except Exception as error:
        logging.error(error)


def deserialization_symmetric_key(path: str) -> bytes:
    try:
        with open(path, mode='rb') as key_file:
            return key_file.read()
    except Exception as error:
        logging.error(error)


def serialize_public_key(public_pem: str, public_key: rsa.RSAPublicKey) -> None:
    try:
        with open(public_pem, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except Exception as error:
        logging.error(error)


def deserialization_public_key(public_pem: str) -> rsa.RSAPublicKey:
    try:
        with open(public_pem, 'rb') as pem_in:
            public_bytes = pem_in.read()
        return load_pem_public_key(public_bytes)
    except Exception as error:
        logging.error(error)


def serialize_private_key(private_pem: str, private_key: rsa.RSAPrivateKey) -> None:
    try:
        with open(private_pem, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
    except Exception as error:
        logging.error(error)


def deserialization_private_key(private_pem: str) -> rsa.RSAPrivateKey:
    try:
        with open(private_pem, 'rb') as pem_in:
            private_bytes = pem_in.read()
        return load_pem_private_key(private_bytes, password=None, )
    except Exception as error:
        logging.error(error)