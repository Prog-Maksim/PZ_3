# Из исходного текстового файла (hotline.txt) перенести в первый файл строки с корректными номерами телефонов
# (т.е. в номере должно быть 11 цифр, например, 86532547891), а во второй с некорректными номерами телефонов. Посчитать
# полученные строки в каждом файле.

import re


def read_file() -> str:
    with open('hotline.txt', 'r', encoding="utf-8") as file:
        yield from file.readlines()


def processing_data() -> tuple:
    try:
        correct_file = open('correct_numbers.txt', 'w', encoding="utf-8")
        incorrect_file = open('incorrect_numbers.txt', 'w', encoding="utf-8")

        correct_count = 0
        incorrect_count = 0

        # Регулярное выражение для поиска номеров телефонов
        phone_pattern = re.compile(r'\b\d{11}\b')

        # Перебираем строки и ищем номера телефонов
        for line in read_file():
            match = re.search(phone_pattern, line)
            if match:
                correct_file.write(line)
                correct_count += 1
            else:
                incorrect_file.write(line)
                incorrect_count += 1

        return correct_count, incorrect_count
    except Exception as error:
        print(error)
    finally:
        correct_file.close()
        incorrect_file.close()


def main() -> None:
    correct_count, incorrect_count = processing_data()
    print(f'Количество строк с корректными номерами: {correct_count}')
    print(f'Количество строк с некорректными номерами: {incorrect_count}')


if __name__ == "__main__":
    main()
