# Составить генератор (yield), который выводит из строки только цифры.

def main():
    txt = "sgtvrk456ct45634vs56fghdtf89769df464587"
    for num in txt:
        if not num.isalpha():
            yield num


if __name__ == "__main__":
    for i in main():
        print(i)
