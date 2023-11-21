# Составить функцию, которая выполнит суммирования числового ряда.

def the_sum_number(nums: list) -> int:
    return sum(nums)


def the_sum_number_new(nums: list) -> int:
    number = 0
    for i in nums:
        number += i

    return number


if __name__ == "__main__":
    try:
        number: list = [int(num) for num in input("Введите числа через пробел: ").split()]
        print("Сумма чисел:", the_sum_number(nums=number))
    except ValueError:
        print("Требуется ввести число")
    except KeyboardInterrupt:
        print("\nВы завершили работу программы")

# Попытка реализовать программу в одну строку
# the_sum_number = lambda: print("Сумма числового ряда:", sum([int(num) for num in input("Введите числа через пробел: ").split()]))
# the_sum_number()
