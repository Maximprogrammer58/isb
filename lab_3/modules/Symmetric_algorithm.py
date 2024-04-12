import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from modules.serialize_and_deserialize import read_bytes, read_data, write_text, write_bytes_text, deserialization_symmetric_key
from cryptography.hazmat.primitives import padding


class SymmetricCryptography:
    """Working with Symmetric Cryptography"""
    def get_symmetric_key(self) -> bytes:
        """Getting a symmetric key
            Returns:
                symmetric key
        """
        return os.urandom(16)

    def encrypt_text_using_symmetric_key(self, path_text: str, path_symmetric_key: str, path_encrypted_text: str) -> str:
        """Encrypt the text using a symmetric algorithm and save it in the specified path"""
        """Reading a json file
                Args:
                    path_text: the path to the file
                    path_symmetric_key: the path to the symmetric key file
                    path_encrypted_text: the path to the encrypted text file
                Returns:
                    encrypted text
        """
        iv = os.urandom(16)
        text = read_data(path_text)
        symmetric_key = deserialization_symmetric_key(path_symmetric_key)
        cipher = Cipher(algorithms.SEED(symmetric_key), modes.CBC(iv))
        padder = padding.PKCS7(128).padder()
        bytes_text = bytes(text, 'UTF-8')
        padded_text = padder.update(bytes_text) + padder.finalize()
        encryptor = cipher.encryptor()
        encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
        encrypted_text = iv + encrypted_text
        write_bytes_text(path_encrypted_text, encrypted_text)
        return encrypted_text

    def decrypt_text_using_symmetric_key(self, path_symmetric_key: str, encrypted_path_text: str,
                                         path_decrypted_text: str) -> str:
        """Decrypt the text using a symmetric algorithm and save it along the specified path
                Args:
                    path_symmetric_key: the path to the symmetric key file
                    encrypted_path_text: the path to the encrypted text file
                    path_decrypted_text: the path to the decrypted text file
                Returns:
                    decrypted text
        """
        key_size = 16
        text = read_bytes(encrypted_path_text)
        iv = text[:key_size]
        encrypted_text = text[key_size:]
        symmetric_key = deserialization_symmetric_key(path_symmetric_key)
        cipher = Cipher(algorithms.SEED(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
        unpadder = padding.PKCS7(key_size * 8).unpadder()
        unpadded_dc_text = unpadder.update(decrypted_text) + unpadder.finalize()
        dec_text = unpadded_dc_text.decode('UTF-8')
        write_text(path_decrypted_text, dec_text)
        return dec_text

