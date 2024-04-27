import json
import logging


logging.basicConfig(level=logging.INFO)


def read_card_info(path: str) -> dict:
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except Exception as error:
        logging.error(error)


def write_card_numbers(path: str, card_numbers: list) -> None:
    try:
        with open(path, "w", encoding="UTF-8") as file:
            json.dump({"card_numbers":  card_numbers}, file)
    except Exception as error:
        logging.error(error)