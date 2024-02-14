def caesar_cipher(text: str, key: int, alphabet: str = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ") -> str:
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            index = (alphabet.index(letter) + key) % len(alphabet)
            encrypted_text += alphabet[index]
        else:
            encrypted_text += letter
    return encrypted_text