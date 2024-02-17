# Из матрицы сформировать массив из положительных четных элементов, найти их сумму и среднее
# арифметическое.
import random


def create_matrix(num_rows: int, num_cols: int) -> list:
    matrix = [[random.randint(1, 51) for _ in range(num_cols)] for _ in range(num_rows)]
    return matrix


def main():
    matrix = create_matrix(5, 5)
    print(f"Исходная матрица: \n{matrix}")

    new_matrix = [j for i in matrix for j in i if j > 0 and j % 2 == 0]

    print(f"Массив четных элементов: \n{new_matrix}")
    print("Сумма чисел: ", sum(new_matrix))
    print("Среднее число:", sum(new_matrix) / len(new_matrix))


if __name__ == "__main__":
    main()
