# Дана строка, содержащая цифры и строчные латинские буквы. Если буквы в строке упорядочены по алфавиту, то вывести 0;
# в противном случае вывести номер первого символа строки, нарушающего алфавит.
from colorama import Fore, Style


def check_alphabet(text: str) -> int:
    """
    Функция для проверки строки на соблюдение алфавита
    Возвращает -1, если строка упорядочена, или индекс первого элемента, нарушающего порядок
    :param text: строка для проверки
    :return: результат проверки.
    """
    for i in range(len(text) - 1):
        if text[i] > text[i+1]:
            return i + 1
    return -1


if __name__ == "__main__":
    try:
        txt = input("Введите символы и цифры: ")
        result = check_alphabet(text=txt)

        if result == -1:
            print(f"{Fore.GREEN}Строка упорядочена по алфавиту{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Символ под номером {result} не соответствует алфавиту{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Вы завершили работу программы{Style.RESET_ALL}")
