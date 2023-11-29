# Дана строка, содержащая цифры и строчные латинские буквы. Если буквы в строке упорядочены по алфавиту, то вывести 0;
# в противном случае вывести номер первого символа строки, нарушающего алфавитный порядок.
from colorama import Fore
from colorama import Style


def sort_text(text: str) -> str:
    """
    Сортирует строку по алфавиту
    :param text: строка для сортировки
    :return: отсортированная строка
    """

    return "".join((sorted(list(text))))


def check_alphabet(text: str) -> int:
    """
    Функция для проверки строки на соблюдение алфавита
    Возвращает число -1 - если строка упорядочена, или любое другое число показывающее где допущена ошибка
    :param text: строка которую нужно проверить
    :return: результат проверки
    """
    txt = sort_text(text=text)

    if text != txt:
        for i in range(len(text)):
            if text[i] != txt[i]:
                return i
    return -1


if __name__ == "__main__":
    try:
        txt = input("Введите символы и цифры: ")
        result = check_alphabet(text=txt)

        if result == -1:
            print(f"{Fore.GREEN}Строка упорядочена по алфавиту{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Символ под номером: {result} не соответствует алфавиту{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Вы завершили работу программы{Style.RESET_ALL}")