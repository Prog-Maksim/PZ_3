# Организовать и вывести последовательность из N случайных целых чисел. Из
# исходной последовательности организовать первую последовательность, содержащую
# числа кратные трем, и вторую – для всех остальных. Найти количество элементов в
# полученных последовательностях.

import random


def main():
    number_list = [random.randint(111, 999) for _ in range(random.randint(10, 100))]
    print(f"Последовательность чисел: \n{number_list}")

    sort_list_1 = [i for i in number_list if (i % 3) == 0]
    print(f"\nЧисла кратные 3 из исходной последовательности: \n{sort_list_1}")
    print(f"Размер: {len(sort_list_1)} \n")

    sort_list_2 = [i for i in number_list if (i % 3) != 0]
    print(f"Все остальные числа из исходной последовательности: \n{sort_list_2}")
    print(f"Размер: {len(sort_list_2)}")


if __name__ == "__main__":
    main()
