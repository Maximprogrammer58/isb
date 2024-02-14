import json


def read_file(path: str) -> str:
    with open(path, "r", encoding='UTF-8') as file:
        text = file.read()
    return text


def write_file(path: str, info: str) -> None:
    with open(path, "w", encoding='UTF-8') as file:
        file.write(info)


def read_json(path: str) -> str:
    with open(path, 'r', encoding='UTF-8') as file:
        return json.load(file)
