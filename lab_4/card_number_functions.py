import file_handler
import hashlib
import multiprocessing as mp
import numpy as np

from matplotlib import pyplot as plt


def check_card_number(guessed_part: int, bins: list, last_digit: int, hash: str) -> str | None:
    for bin in bins:
        guessed_card_number = f"{bin}{str(guessed_part).zfill(6)}{last_digit}"
        if hashlib.sha224(guessed_card_number.encode()).hexdigest() == hash:
            return guessed_card_number
    return None


def select_card_number(hash: str, bins: list, last_digit: int) -> None:
    guessed_card_number = []
    with mp.Pool(mp.cpu_count()) as p:
        for res in p.starmap(check_card_number, [(i, bins, last_digit, hash) for i in list(range(0, 999999))]):
            if res:
                guessed_card_number.append(res)
    file_handler.write_card_numbers("card_number.json", guessed_card_number)


def check_card_using_luna(card_number: str) -> bool:
    card_number = [int(digit) for digit in card_number]
    for i in range(len(card_number)):
        if i % 2 == 0:
            card_number[i] *= 2
            if card_number[i] > 9:
                card_number[i] = (card_number[i] % 10) + (card_number[i] // 10)
    return sum(card_number) % 10 == 0