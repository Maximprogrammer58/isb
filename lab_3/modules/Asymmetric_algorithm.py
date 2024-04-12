from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from modules.serialize_and_deserialize import (write_bytes_text, deserialization_public_key,
                                               deserialization_symmetric_key, deserialization_private_key, serialize_symmetric_key)


class AsymmetricCryptography:
    """Working with Asymmetric Cryptography"""
    def generate_asymmetric_keys(self) -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        """Getting asymmetric keys
            Returns:
                a pair of keys (public and private)
        """
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        return keys.public_key(), keys

    def encrypt_symmetric_encryption_key_with_public(self, path_public_key: str, path_symmetric_key: str,
                                                     path_encrypted_symmetric_key: str) -> None:
        """Encrypt the symmetric encryption key with a public key and save it in the specified path
                Args:
                    path_public_key: the path to the file with the asymmetric public key
                    path_symmetric_key: the path to the symmetric key file
                    path_encrypted_symmetric_key: the path to the encrypted symmetric key file
        """
        symmetric_key = deserialization_symmetric_key(path_symmetric_key)
        public_key = deserialization_public_key(path_public_key)
        encryption_key = public_key.encrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                algorithm=hashes.SHA256(), label=None))
        write_bytes_text(path_encrypted_symmetric_key, encryption_key)

    def decrypt_symmetric_key(self, path_encrypted_symmetric_key: str, private_key_path: str,
                              path_decrypted_symmetric_key: str) -> bytes:
        """Decrypt the symmetric key
                Args:
                    path_encrypted_symmetric_key: the path to the encrypted symmetric key file
                    private_key_path: the path to the file with the asymmetric private key
                Returns:
                    symmetric key
        """
        encrypted_symmetric_key = deserialization_symmetric_key(path_encrypted_symmetric_key)
        private_key = deserialization_private_key(private_key_path)
        symmetric_key = private_key.decrypt(encrypted_symmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                                                           algorithm=hashes.SHA256(), label=None))
        serialize_symmetric_key(path_decrypted_symmetric_key, symmetric_key)
        return symmetric_key