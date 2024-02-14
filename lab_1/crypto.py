def caesar_cipher(text: str, key: int, alphabet: str = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ") -> str:
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            index = (alphabet.index(letter) + key) % len(alphabet)
            encrypted_text += alphabet[index]
        else:
            encrypted_text += letter
    return encrypted_text


def frequency_analysis(text: str) -> dict:
    frequency = {}
    for letter in text:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    for key in frequency:
        frequency[key] = frequency[key] / len(text)
    return dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))


def decryption_by_key(code: str, key: dict) -> str:
    '''The function for decryption by key helps to get rid of a large number of replace'''
    for letter in key:
        code = code.replace(letter, key[letter])
    return code