# Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг конфет.


def price_candy(num: float) -> None:
    for nums in range(1, 11):
        print(f"{nums} кг конфет стоит: {round(nums * num, 2)} рублей")


if __name__ == "__main__":
    try:
        number: float = float(input("Введите стоимость 1 кг конфет: "))
        price_candy(num=number)
    except ValueError:
        print("Требуется ввести число")
    except KeyboardInterrupt:
        print("Вы завершили выполнение программы")

    input()
