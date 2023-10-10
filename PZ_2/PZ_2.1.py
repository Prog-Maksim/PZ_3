# Дано трехзначное число. Вывести вначале его последнюю цифру (единицы), а затем - его среднюю цифру (десятки)

def main_number(number: int) -> None:
    print("Последняя цифра (единица):", number % 10)
    print("Средняя цифра (десятки):", (number % 100) // 10)


def check_number(number: int) -> None:
    """
    Данная функция проверяет переданное ей число
    :param number:  принимает число
    :return: ничего не возвращает
    """

    if len(str(number)) == 3:
        main_number(number=number)
    else:
        print("Введенное вами число не трехзначное")


if __name__ == "__main__":
    try:
        check_number(int(input("Введите число: ")))
    except ValueError:
        print("Требуется ввести число")
    except KeyboardInterrupt:
        print("\nВы закончили работу программы")