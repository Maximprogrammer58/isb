from file_handler import read_json
from card_number_functions import select_card_number, check_card_using_luna, hash_collision_search_time


if __name__ == '__main__':
    info = read_json("card_info.json")
    card_number = read_json("card_number.json")["card_number"]
    select_card_number(info["hash"], info["bins_list"], info["last_digit"])
    print(f"Корректность номера карты: {check_card_using_luna(card_number)}")
    hash_collision_search_time(info["hash"], info["bins_list"], info["last_digit"])