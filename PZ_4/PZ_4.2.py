# Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от
# деления определить, имеется ли в записи числа N цифра «2». Если имеется, то
# вывести TRUE, если нет — вывести FALSE

def check_number(num: int) -> bool:
    while num > 0:
        digit = num % 10
        if digit == 2:
            return True
        num //= 10
    return False


if __name__ == "__main__":
    try:
        number: int = int(input("Введите число N: "))
        print(check_number(num=number))
    except ValueError:
        print("Требуется ввести число")
    except KeyboardInterrupt:
        print("\nВы закончили выполнение программы")

    input()
