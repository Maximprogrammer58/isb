from modules.KeyGenerator import KeyGenerator
from modules.Encryption import Encryption
from modules.Decryption import Decryption


if __name__ == "__main__":
    key_generator = KeyGenerator("symmetric.txt", 'public.pem','private.pem')
    key_generator.get_symmetric_key()
    key_generator.generate_asymmetric_keys()
    key_generator.serialize_asymmetric_keys()
    key_generator.encrypt_symmetric_encryption_key_with_public()

    encrypt = Encryption("text.txt", "private.pem", "symmetric.txt", "encrypt_text.txt")
    encrypt.decrypt_symmetric_key()
    encrypt.encrypt_text_using_symmetric_key()

    decrypt = Decryption("encrypt_text.txt", "private.pem", "symmetric.txt", "decrypt_text.txt")
    decrypt.decrypt_symmetric_key()
    decrypt.decrypt_text_using_symmetric_key()