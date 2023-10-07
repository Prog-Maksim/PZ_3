# Дано целое число А. Проверить истинность высказывания: Число А является четным.

def check_number(num: int) -> None:
    if num % 2 == 0:
        print(f"Число А: {num} - это четное число")
    else:
        print(f"Число А: {num} - это не четное число")


if __name__ == "__main__":
    try:
        number: int = int(input("Введите число: "))
        check_number(num=number)
    except ValueError:
        print("Требуется ввести число")
    except KeyboardInterrupt:
        print("\nВы закончили работу программы")

    input("Нажмите любую клавишу чтобы завершить выполнение программы ")
