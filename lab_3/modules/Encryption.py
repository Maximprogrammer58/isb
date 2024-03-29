import os
import cryptography.hazmat.primitives.asymmetric as asymetric_padding

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from modules.serialize_and_deserialize import deserialization_symmetric_key, read_data, deserialization_private_key, write_bytes_text
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding


class Encryption:
    """ Data encryption by a hybrid system
        Methods:
            __init__(): class initializer
            __call__(): a method can make an instance of a class behave like a function
            decrypt_symmetric_key(): decrypt the symmetric key
            encrypt_text_using_symmetric_key(): encrypt the text using a symmetric algorithm
    """
    def __init__(self, path_text: str, private_key_path: str,
                 path_encrypted_symmetric_key: str, path_encrypted_text: str) -> None:
        """Class initializer
            Args:
                path_text: the path to the encrypted text file
                private_key_path: the path to the private key of the asymmetric algorithm
                path_encrypted_symmetric_key: the path to the encrypted key of the symmetric algorithm
                path_encrypted_text: the path to save the encrypted text file
        """
        self.path_text = path_text
        self.private_key_path = private_key_path
        self.path_encrypted_symmetric_key = path_encrypted_symmetric_key
        self.path_encrypted_text = path_encrypted_text
        self.__symmetric_key = None
        self.__iv = os.urandom(16)

    def decrypt_symmetric_key(self) -> bytes:
        """Decrypt the symmetric key
            Returns:
                symmetric key
        """
        encrypted_symmetric_key = deserialization_symmetric_key(self.path_encrypted_symmetric_key)
        private_key = deserialization_private_key(self.private_key_path)
        self.__symmetric_key = private_key.decrypt(encrypted_symmetric_key, asymetric_padding.padding.OAEP(mgf=asymetric_padding.padding.MGF1(algorithm=hashes.SHA256()),
                                                                                                           algorithm=hashes.SHA256(), label=None))
        return self.__symmetric_key

    def encrypt_text_using_symmetric_key(self) -> None:
        """Encrypt the text using a symmetric algorithm and save it in the specified path"""
        text = read_data(self.path_text)
        cipher = Cipher(algorithms.SEED(self.__symmetric_key), modes.CBC(self.__iv))
        padder = padding.PKCS7(128).padder()
        bytes_text = bytes(text, 'UTF-8')
        padded_text = padder.update(bytes_text) + padder.finalize()
        encryptor = cipher.encryptor()
        encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
        encrypted_text = self.__iv + encrypted_text
        write_bytes_text(self.path_encrypted_text, encrypted_text)

    def __call__(self) -> None:
        """A method can make an instance of a class behave like a function"""
        print(f"Расшифрованный симметричный ключ: {self.decrypt_symmetric_key()}")
        self.encrypt_text_using_symmetric_key()
