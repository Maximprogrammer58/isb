import file_handler
import card_number_functions


if __name__ == '__main__':
    info = file_handler.read_card_info("card_info.json")
    card_number_functions.select_card_number(info["hash"], info["bins_list"], info["last_digit"])
