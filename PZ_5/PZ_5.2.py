# Описать функцию TrianglePS(параметры), вычисляющую по стороне a
# равностороннего треугольника его периметр P = 3*a и площадь S = a2 √3/4. С
# помощью этой функции найти периметры и площади трех равносторонних
# треугольников с данными сторонами.
import math

def TrianglesPS(a: int):
    perimetr: int = 3 * a
    ploshad = a ** 2 * math.sqrt((3 / 4))
    print(f"периметр: {perimetr}, площадь: {ploshad}")


if __name__ == "__main__":
    try:
        number = input("Введите три стороны в см: ").split()
        [TrianglesPS(a=int(i)) for i in number]
    except ValueError:
        print("Введите число!")
    except KeyboardInterrupt:
        print("Вы завершили работу программы")
