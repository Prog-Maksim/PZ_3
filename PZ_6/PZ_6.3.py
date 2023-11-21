# Дан список размера N (N — четное число). Поменять местами его первый элемент
# со вторым, третий — с четвертым и т. д.


def swap_elements(input_list: list):
    for i in range(0, len(input_list), 2):
        if i+1 < len(input_list):
            input_list[i], input_list[i+1] = input_list[i+1], input_list[i]


if __name__ == "__main__":
    numbers = list()
    try:
        numbers = [int(i) for i in input("Введите числа через пробел: ").split()]
        if len(numbers) % 2 != 0:
            raise KeyError

        swap_elements(numbers)
        print(numbers)
    except ValueError:
        print("Требуется вводить числа!")
    except KeyError:
        print("Количество чисел должно быть четным!")