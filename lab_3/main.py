import argparse

from enum import Enum
from modules.Asymmetric_algorithm import AsymmetricCryptography
from modules.serialize_and_deserialize import read_json, serialize_symmetric_key, serialize_private_key, serialize_public_key
from modules.Symmetric_algorithm import SymmetricCryptography


class Option(Enum):
    GENERATE_SYMMETRIC_KEY = 0
    GENERATE_ASYMMETRIC_KEYS = 1
    ENCRYPT_TEXT = 2
    DECRYPT_TEXT = 3
    ENCRYPT_SYMMETRIC_KEY = 4
    DECRYPT_SYMMETRIC_KEY = 5


if __name__ == "__main__":
    parser = argparse.ArgumentParser("")
    symmetric_crypt = SymmetricCryptography()
    asymmetric_crypt = AsymmetricCryptography()

    parser.add_argument("option", type=int,
                        help="Выбор режима работы: "
                             "0-генерация симметричного ключа"
                             "1-генерация ассимметричных ключей"
                             "2-шифрование текста"
                             "3-дешифрование текста"
                             "4-шифрование симметричного ключа"
                             "5-дешифрование симметричного ключа")
    parser.add_argument("settings", type=str,
                        help="Введите путь к файлу с пользовательскими настройками")
    args = parser.parse_args()

    settings = read_json(args.settings)
    match(args.option):
        case Option.GENERATE_SYMMETRIC_KEY.value:
            symmetric_key = symmetric_crypt.get_symmetric_key()
            serialize_symmetric_key(settings["symmetric_key"], symmetric_key)
        case Option.GENERATE_ASYMMETRIC_KEYS.value:
            public_key, private_key = asymmetric_crypt.generate_asymmetric_keys()
            serialize_public_key(settings["public_key"], public_key)
            serialize_private_key(settings["private_key"], private_key)
        case Option.ENCRYPT_TEXT.value:
            encrypted_text = symmetric_crypt.encrypt_text_using_symmetric_key(settings["initial_file"],
                                                                              settings["symmetric_key"],
                                                                              settings["encrypted_file"])
            print(f"Зашифрованный текст: {encrypted_text}")
        case Option.DECRYPT_TEXT.value:
            decrypted_text = symmetric_crypt.decrypt_text_using_symmetric_key(settings["symmetric_key"],
                                                                              settings["encrypted_file"],
                                                                              settings["decrypted_file"])
            print(f"Дешифрованный текст: {decrypted_text}")
        case Option.ENCRYPT_SYMMETRIC_KEY.value:
            asymmetric_crypt.encrypt_symmetric_encryption_key_with_public(settings["public_key"],
                                                                          settings["symmetric_key"],
                                                                          settings["encrypted_symmetric_key"])
        case Option.DECRYPT_SYMMETRIC_KEY.value:
            asymmetric_crypt.decrypt_symmetric_key(settings["encrypted_symmetric_key"],
                                                   settings["private_key"],
                                                   settings["decrypted_symmetric_key"])
        case _:
            print("Не выбрана подходящяя опция")

