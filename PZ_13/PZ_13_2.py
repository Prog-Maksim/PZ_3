# Из матрицы сформировать массив из положительных четных элементов, найти их сумму и среднее
# арифметическое.
import random


def print_array(matrix: list) -> None:
    txt: str = ""
    for i in matrix:
        txt = f"{txt}{i}\n"
    print(txt)


def create_matrix(num_rows: int, num_cols: int) -> list:
    matrix = [[random.randint(-2, 5) for _ in range(num_cols)] for _ in range(num_rows)]
    return matrix


def main():
    matrix = create_matrix(5, 5)
    print(f"Исходная матрица:")
    print_array(matrix)

    new_matrix = [j for i in matrix for j in i if j > 0 and j % 2 == 0]

    print(f"Массив четных элементов: \n{new_matrix}")
    print("Сумма чисел: ", sum(new_matrix))
    print("Среднее число:", round(sum(new_matrix) / len(new_matrix), 2))


if __name__ == "__main__":
    main()
