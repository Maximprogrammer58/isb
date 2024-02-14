import crypto
import file_handler


def main():
    # part 1
    text = file_handler.read_file("texts/part1/text.txt")
    key = file_handler.read_file("texts/part1/key.txt")
    encrypted_text = crypto.caesar_cipher(text, int(key))
    file_handler.write_file("texts/part1/encrypted_text.txt", encrypted_text)

    # part 2
    code = file_handler.read_file("texts/part2/code.txt")

    print(f"\nЧастота букв в русском языке: {file_handler.read_json('freq.json')}")
    print(f"Частота букв в зашифр. тексте: {crypto.frequency_analysis(code)}")
    print(f"\nЗашифрованный текст: {code}")
    
    code = code.replace("М", " ")
    code = code.replace("Ф", "М")
    code = code.replace("И", "Ф")
    code = code.replace(">", "И")
    code = code.replace("Е", "С")
    code = code.replace("О", "Е")
    code = code.replace("Ь", "Щ")
    code = code.replace("А", "Ь")
    code = code.replace("Л", "Я")
    code = code.replace("Р", "З")
    code = code.replace("Д", "Р")
    code = code.replace("1", "О")
    code = code.replace("r", "Т")
    code = code.replace("Х", "Н")
    code = code.replace("4", "А")
    code = code.replace("c", "Д")
    code = code.replace("П", "Ж")
    code = code.replace("2", "П")
    code = code.replace("К", "Ю")
    code = code.replace("8", "К")
    code = code.replace("Й", "Х")
    code = code.replace("7", "Й")
    code = code.replace("Ч", "Ц")
    code = code.replace("<", "Ч")
    code = code.replace("a", "В")
    code = code.replace("b", "Г")
    code = code.replace("Ы", "Ш")
    code = code.replace("\n", "Ы")
    code = code.replace("Б", "Э")
    code = code.replace("5", "Б")
    code = code.replace("У", "Л")
    code = code.replace("t", "У")

    print(f"\nРасшифрованный текст: {code}")
    file_handler.write_file("texts/part2/decode_text.txt", code)


if __name__ == "__main__":
    main()