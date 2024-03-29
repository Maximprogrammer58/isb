import json
import logging

from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


logging.basicConfig(level=logging.INFO)


def serialize_symmetric_key(path: str, key: bytes) -> None:
    """Serialization of the symmetric encryption key
        Args:
            path: the path to the file
            key: symmetric encryption key
    """
    try:
        with open(path, 'wb') as key_file:
            key_file.write(key)
    except Exception as error:
        logging.error(error)


def deserialization_symmetric_key(path: str) -> bytes:
    """Deserialization of the symmetric encryption key
        Args:
            path: the path to the file
        Returns:
            symmetric key
    """
    try:
        with open(path, mode='rb') as key_file:
            return key_file.read()
    except Exception as error:
        logging.error(error)


def serialize_public_key(public_pem: str,
                         public_key: rsa.RSAPublicKey) -> None:
    """Serialization of the RSA Asymmetric Encryption Public Key
        Args:
            public_pem: the path to the file
            public_key: public key of RSA
    """
    try:
        with open(public_pem, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except Exception as error:
        logging.error(error)


def deserialization_public_key(public_pem: str) -> rsa.RSAPublicKey:
    """Deserialization of the RSA Asymmetric Encryption Public Key
        Args:
            public_pem: the path to the file
        Returns:
            RSA Asymmetric Encryption Public Key
    """
    try:
        with open(public_pem, 'rb') as pem_in:
            public_bytes = pem_in.read()
        return load_pem_public_key(public_bytes)
    except Exception as error:
        logging.error(error)


def serialize_private_key(private_pem: str,
                          private_key: rsa.RSAPrivateKey) -> None:
    """Serialization of the RSA Asymmetric Encryption Private Key
        Args:
            private_pem: the path to the file
            private_key: RSA Asymmetric Encryption Private Key
    """
    try:
        with open(private_pem, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
    except Exception as error:
        logging.error(error)


def deserialization_private_key(private_pem: str) -> rsa.RSAPrivateKey:
    """Deserialization of the RSA Asymmetric Encryption Private Key
        Args:
            private_pem: the path to the file
        Returns:
            RSA Asymmetric Encryption Private Key
    """
    try:
        with open(private_pem, 'rb') as pem_in:
            private_bytes = pem_in.read()
        return load_pem_private_key(private_bytes, password=None, )
    except Exception as error:
        logging.error(error)


def read_data(file_path: str) -> str:
    """Reading data from a file
        Args:
            file_path: the path to the file
        Returns:
            file contents
    """
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            data = file.read()
        return data
    except Exception as error:
        logging.error(error)


def read_bytes(file_path: str) -> bytes:
    """Reading bytes from a file
        Args:
            file_path: the path to the file
        Returns:
            file contents in bytes
    """
    try:
        with open(file_path, "rb") as file:
            data = file.read()
        return data
    except Exception as error:
        logging.error(error)


def write_bytes_text(file_path: str, bytes_text: bytes) -> None:
    """Writing a sequence of bytes to a file
        Args:
            file_path: the path to the file
            bytes_text: data to be written as bytes
    """
    try:
        with open(file_path, "wb") as file:
            file.write(bytes_text)
    except Exception as error:
        logging.error(error)


def write_text(file_path: str, info: str) -> None:
    """Writing info to a file
        Args:
            file_path: the path to the file
            info: data to be written in file
    """
    try:
        with open(file_path, "w", encoding='utf-8') as file:
            file.write(info)
    except Exception as error:
        logging.error(error)


def read_json(path: str) -> dict:
    """Reading a json file
        Args:
            path: the path to the file
        Returns:
            json object (dictionary)
    """
    with open(path, 'r', encoding='UTF-8') as file:
        return json.load(file)
