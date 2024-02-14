import crypto
import file_handler


def main():
    # part 1
    text = file_handler.read_file("texts/part1/text.txt")
    key = file_handler.read_file("texts/part1/key.txt")
    encrypted_text = crypto.caesar_cipher(text, int(key))
    file_handler.write_file("texts/part1/encrypted_text.txt", encrypted_text)


if __name__ == "__main__":
    main()