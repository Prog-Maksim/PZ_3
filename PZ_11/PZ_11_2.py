# Из предложенного текстового файла (text18-3.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы третей
# строки их числовыми кодами.

import os
from chardet.universaldetector import UniversalDetector


def search_charset(file_name: str) -> str:
    """
    Функция для определения кодироки файла
    :param file_name: путь до файла
    :return: кодировка файла
    """

    detector = UniversalDetector()
    with open(file_name, 'rb') as fh:
        for line in fh:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result['encoding']


def read_file(file_name: str) -> str:
    if os.path.isfile(file_name):
        with open(file_name, "r", encoding=search_charset(file_name)) as file:
            return file.read()
    return ""


def proccessing_data_punctuation(text: str) -> int:
    punctiation_library = ['.', ',', ':', ';', '?', '«', '»']
    count_punctuation = 0

    new_text = ' '.join(text.split('\n')[:4])
    for i in new_text:
        if i in punctiation_library:
            count_punctuation += 1

    return count_punctuation


def replace_symbols(text: str) -> str:
    new_text = text.split('\n')

    for i in new_text[2]:
        new_text[2] = new_text[2].replace(i, str(ord(i)))

    return '\n'.join(new_text)


def save_result(text: str):
    with open(r'File_result_2.txt', 'w', encoding='utf-8') as file:
        file.write(text)


def main() -> None:
    text = read_file("text18-3.txt")
    print(f"Содержимое текстового файла: \n{text}\n------------------------------\n")

    len_punctuation = proccessing_data_punctuation(text=text)
    print(f"Кол-во знаков пунктуации: {len_punctuation}")
    save_result(replace_symbols(text))


if __name__ == '__main__':
    main()
