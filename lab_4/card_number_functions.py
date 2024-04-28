import file_handler
import hashlib
import multiprocessing as mp
import time

from matplotlib import pyplot as plt
from tqdm import tqdm


def check_card_number(guessed_part: int, bins: list, last_digit: int, hash: str) -> str | None:
    """Checking whether the hash of the guessed card is equal to the hash of the original bank card
        Args:
          guessed_part: the guessed part is the card number
          bins: list of bins numbers
          last_digit: the last 4 bank card numbers
          hash: hash of the bank card
        Returns:
          the guessed bank card number
    """
    for bin in bins:
        guessed_card_number = f"{bin}{str(guessed_part).zfill(6)}{last_digit}"
        if hashlib.sha224(guessed_card_number.encode()).hexdigest() == hash:
            return guessed_card_number


def select_card_number_helper(hash: str, bins: list, last_digit: int, count_process: int) -> str | None:
    """The assistant function for selecting the card number by hash
       It is necessary to transfer the number of processes
        Args:
          hash: hash of the bank card
          bins: list of bins numbers
          last_digit: the last 4 bank card numbers
          count_process: the number of processes to calculate
        Returns:
          bank card number
    """
    with mp.Pool(count_process) as p:
        for result in p.starmap(check_card_number, [(i, bins, last_digit, hash) for i in list(range(0, 999999))]):
            if result:
                print(f"Номер подобранной карты при количестве процессов = {count_process} : {result}")
                file_handler.write_card_number("card_number.json", result)
                p.terminate()
                return result


def select_card_number(hash: str, bins: list, last_digit: int) -> str | None:
    """The shell function for selecting the card number
        Args:
          hash: hash of the bank card
          bins: list of bins numbers
          last_digit: the last 4 bank card numbers
        Returns:
          bank card number
    """
    return select_card_number_helper(hash, bins, last_digit, mp.cpu_count())


def check_card_using_luna(card_number: str) -> bool:
    """Checking the correctness of the bank card number using the Luna algorithm
        Args:
          card_number: bank card number
        Returns:
          the flag for the correctness of the card number
    """
    card_number = [int(digit) for digit in card_number]
    for i in range(len(card_number)):
        if i % 2 == 0:
            card_number[i] *= 2
            if card_number[i] > 9:
                card_number[i] = (card_number[i] % 10) + (card_number[i] // 10)
    return sum(card_number) % 10 == 0


def hash_collision_search_time(hash: str, bins: list, last_digit: int) -> None:
    """Measuring the time for searching for hash function collisions and
       plotting the time dependence on the number of processes spent
        Args:
          hash: hash of the bank card
          bins: list of bins numbers
          last_digit: the last 4 bank card numbers
    """
    time_list = []
    for count_process in tqdm(range(1, int(mp.cpu_count() * 1.5)), desc="Поиск коллизии"):
        start_time = time.time()
        if select_card_number_helper(hash, bins, last_digit, count_process):
            time_list.append(time.time() - start_time)
    fig = plt.figure(figsize=(30, 5))
    plt.ylabel('Время поиска коллизии, с')
    plt.xlabel('Количество процессов')
    plt.plot(list(range(1, int(mp.cpu_count() * 1.5))), time_list, color='green', linestyle='--', marker='x', linewidth=1, markersize=4)
    plt.show()