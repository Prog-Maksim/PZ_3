# Дан символ C. Вывести два символа, первый из которых предшествует символу C в кодовой таблице, а второй следует за
# символом C.
from colorama import Fore
from colorama import Style


def char_to_number(char: str):
    num_to_back = chr(ord(char) - 1)
    num_to_next = chr(ord(char) + 1)
    print(f"Символы которые стоят перед и после символа: '{char}'")
    print(f"'{num_to_back}' << '{char}' >> '{num_to_next}'")


def check_string(text: str):
    if text.isdigit():
        raise ValueError(f"{Fore.RED}Требуется ввети символ а не число!{Style.RESET_ALL}")
    if len(text) != 1:
        raise ValueError(f"{Fore.RED}Требуется ввести только один символ!{Style.RESET_ALL}")


if __name__ == "__main__":
    try:
        text = input("Введите один символ: ")
        try:
            check_string(text=text)
            char_to_number(char=text)
        except ValueError as ex:
            print(ex)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Вы завершили работу программы{Style.RESET_ALL}")