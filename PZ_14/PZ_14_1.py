# Из исходного текстового файла (hotline.txt) перенести в первый файл строки с корректными
# номерами телефонов
# (т.е. в номере должно быть 11 цифр, например, 86532547891), а во второй с
# некорректными номерами телефонов. Посчитать
# полученные строки в каждом файле.

import re


def read_file() -> str:
    with open('hotline.txt', 'r', encoding="utf-8") as file:
        yield from file.readlines()


def processing_data() -> tuple:
    try:
        phone_pattern = re.compile(r'\b\d{11}\b')

        correct_count = sum(1 for line in read_file() if line.replace('\n', '') != "" and
                            re.search(phone_pattern, line))
        incorrect_count = sum(1 for line in read_file() if line.replace('\n', '') != "" and
                              not re.search(phone_pattern, line))

        with (open('correct_numbers.txt', 'w', encoding="utf-8") as correct_file,
              open('incorrect_numbers.txt', 'w', encoding="utf-8") as incorrect_file):
            for line in read_file():
                if re.search(phone_pattern, line):
                    correct_file.write(line)
                else:
                    incorrect_file.write(line)

        return correct_count, incorrect_count
    except Exception as error:
        print(error)


def main() -> None:
    correct_count, incorrect_count = processing_data()
    print(f'Количество строк с корректными номерами: {correct_count}')
    print(f'Количество строк с некорректными номерами: {incorrect_count}')


if __name__ == "__main__":
    main()
