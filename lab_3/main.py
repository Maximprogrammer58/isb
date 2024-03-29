import argparse

from modules.Decryption import Decryption
from modules.Encryption import Encryption
from modules.KeyGenerator import KeyGenerator
from modules.serialize_and_deserialize import read_json


if __name__ == "__main__":
    settings = read_json("settings.json")

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Запускает режим генерации ключей')
    group.add_argument('-enc', '--encryption', help='Запускает режим шифрования')
    group.add_argument('-dec', '--decryption', help='Запускает режим дешифрования')

    args = parser.parse_args()

    if args.generation is not None:
        key_generator = KeyGenerator(settings["symmetric_key"],
                                     settings["public_key"],
                                     settings["private_key"])
        key_generator()
    elif args.encryption is not None:
        encrypt = Encryption(settings["initial_file"],
                             settings["private_key"],
                             settings["symmetric_key"],
                             settings["encrypted_file"])
        encrypt()
    else:
        decrypt = Decryption(settings["encrypted_file"],
                             settings["private_key"],
                             settings["symmetric_key"],
                             settings["decrypted_file"])
        decrypt()
