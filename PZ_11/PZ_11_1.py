# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Квадраты четных элементов:
# Сумма квадратов четных элементов:
# Среднее арифметическое суммы квадратов четных элементов:

import random
import os


def create_file(numbers: list) -> None:
    with open("File_numbers.txt", "w", encoding='utf-8') as file:
        file.write(str(numbers))


def random_number() -> list:
    num = random.randint(50, 100)
    rnd = [random.randint(-100, 100) for i in range(num)]
    create_file(numbers=rnd)


def read_file() -> list:
    if os.path.isfile("File_numbers.txt"):
        with open("File_numbers.txt", "r", encoding='utf-8') as file:
            numbers = eval(file.read())

        return numbers
    return None


def save_result(data: str) -> None:
    with open("File_result.txt", "w", encoding='utf-8') as file:
        file.write(data)


def processing_function(numbers: list) -> str:
    square_list = [i ** 2 for i in numbers if i > 0]
    str_data = (f"# Исходные данные: \n{numbers}\n\n"
                f"# Количество элементов: \n{len(numbers)}\n\n"
                f"# Минимальный элемент: \n{min(numbers)}\n\n"
                f"# Квадраты четных чисел: \n{square_list} \n\n"
                f"# Сумма квадратов четных элементов: \n{sum(square_list)}\n\n"
                f"# Среднее арифметическое суммы квадратов четных чисел: \n{round(sum(square_list) / len(square_list), 2)}")

    save_result(str_data)
    return str_data


def main():
    random_number()
    numbers = read_file()
    print(processing_function(numbers))


if __name__ == "__main__":
    main()
