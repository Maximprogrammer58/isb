from cryptography.hazmat.primitives import padding
from modules.serialize_and_deserialize import deserialization_symmetric_key, deserialization_private_key, read_bytes, write_text
import cryptography.hazmat.primitives.asymmetric as asymetric_padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Decryption:
    def __init__(self, encrypted_path_text: str, private_key_path: str,
                 path_encrypted_symmetric_key: str, path_decrypted_text: str) -> None:
        self.encrypted_path_text = encrypted_path_text
        self.private_key_path = private_key_path
        self.path_encrypted_symmetric_key = path_encrypted_symmetric_key
        self.path_decrypted_text = path_decrypted_text
        self.__symmetric_key = None
        self.__key_size = 16

    def decrypt_symmetric_key(self) -> bytes:
        encrypted_symmetric_key = deserialization_symmetric_key(self.path_encrypted_symmetric_key)
        private_key = deserialization_private_key(self.private_key_path)
        self.__symmetric_key = private_key.decrypt(encrypted_symmetric_key, asymetric_padding.padding.OAEP(mgf=asymetric_padding.padding.MGF1(algorithm=hashes.SHA256()),
                                                           algorithm=hashes.SHA256(), label=None))
        return self.__symmetric_key

    def decrypt_text_using_symmetric_key(self) -> None:
        text = read_bytes(self.encrypted_path_text)
        iv = text[:self.__key_size]
        encrypted_text = text[self.__key_size:]
        cipher = Cipher(algorithms.SEED(self.__symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
        unpadder = padding.PKCS7(self.__key_size * 8).unpadder()
        unpadded_dc_text = unpadder.update(decrypted_text) + unpadder.finalize()
        write_text(self.path_decrypted_text, unpadded_dc_text.decode('UTF-8'))