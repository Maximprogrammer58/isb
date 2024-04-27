import file_handler
import card_number_functions


if __name__ == '__main__':
    info = file_handler.read_json("card_info.json")
    card_number = file_handler.read_json("card_number.json")["card_numbers"][0]
    card_number_functions.select_card_number(info["hash"], info["bins_list"], info["last_digit"])
    print(card_number_functions.check_card_using_luna(card_number))