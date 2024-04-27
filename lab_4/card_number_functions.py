import file_handler
import hashlib
import logging
import multiprocessing as mp
import time

from matplotlib import pyplot as plt


logging.basicConfig(level=logging.INFO)


def check_card_number(guessed_part: int, bins: list, last_digit: int, hash: str) -> str | None:
    for bin in bins:
        guessed_card_number = f"{bin}{str(guessed_part).zfill(6)}{last_digit}"
        if hashlib.sha224(guessed_card_number.encode()).hexdigest() == hash:
            return guessed_card_number


def select_card_number_helper(hash: str, bins: list, last_digit: int, count_process: int) -> str | None:
    with mp.Pool(count_process) as p:
        for result in p.starmap(check_card_number, [(i, bins, last_digit, hash) for i in list(range(0, 999999))]):
            if result:
                logging.info(f"Номер подобранной карты: {result}")
                file_handler.write_card_number("card_number.json", result)
                p.terminate()
                return result


def select_card_number(hash: str, bins: list, last_digit: int) -> None:
    select_card_number_helper(hash, bins, last_digit, mp.cpu_count())


def check_card_using_luna(card_number: str) -> bool:
    card_number = [int(digit) for digit in card_number]
    for i in range(len(card_number)):
        if i % 2 == 0:
            card_number[i] *= 2
            if card_number[i] > 9:
                card_number[i] = (card_number[i] % 10) + (card_number[i] // 10)
    return sum(card_number) % 10 == 0

def hash_collision_search_time(hash: str, bins: list, last_digit: int) -> None:
    time_list = []
    for count_process in range(1, int(mp.cpu_count() * 1.5)):
        start_time = time.time()
        if select_card_number_helper(hash, bins, last_digit, count_process):
            time_list.append(time.time() - start_time)
    fig = plt.figure(figsize=(30, 5))
    plt.ylabel('Время поиска коллизии')
    plt.xlabel('Количество процессов')
    plt.plot(list(range(1, int(mp.cpu_count() * 1.5))), time_list, color='green', linestyle='--', marker='x', linewidth=1, markersize=4)
    plt.show()