# В квадратной матрице элементы на главной диагонали увеличить в 2 раза.
import random


def create_matrix(num_rows: int, num_cols: int) -> list:
    matrix = [[random.randint(1, 51) for _ in range(num_cols)] for _ in range(num_rows)]
    return matrix


def square_matrix(matrix: list) -> list:
    return [matrix[i][i] for i in range(len(matrix))]


def main():
    matrix = create_matrix(5, 5)
    print(f"Исходная матрица: \n{matrix}")
    print("Матрица с значениями главной диагонали возведенне во вторую степень:")
    print(square_matrix(matrix))


if __name__ == "__main__":
    main()
