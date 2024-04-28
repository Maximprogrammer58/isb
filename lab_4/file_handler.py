import json
import logging


logging.basicConfig(level=logging.INFO)


def read_json(path: str) -> dict:
    """The function of reading data from a json file
        Args:
          path: the path to the file
        Returns:
          Dictionary with json file structure
    """
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except Exception as error:
        logging.error(error)


def write_card_number(path: str, card_numbers: list) -> None:
    """The function of writing card number to a file
        Args:
          path: the path to the file
    """
    try:
        with open(path, "w", encoding="UTF-8") as file:
            json.dump({"card_number":  card_numbers}, file)
    except Exception as error:
        logging.error(error)