# Составить генератор (yield), который выводит из строки только цифры.


def main():
    txt = "sgtvrk456ct45634vs56fghdtf89769df464587"
    yield from [num for num in txt if num.isdigit()]


if __name__ == "__main__":
    [print(i) for i in main()]
