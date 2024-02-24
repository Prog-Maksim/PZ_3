# В квадратной матрице элементы на главной диагонали увеличить в 2 раза.
import random


def print_array(matrix: list) -> None:
    txt: str = ""
    for i in matrix:
        txt = f"{txt}{i}\n"
    print(txt)


def create_matrix(array_size) -> list:
    matrix = [[random.randint(1, 51) for _ in range(array_size)] for _ in range(array_size)]
    return matrix


def square_matrix(matrix: list) -> list:
    for i in range(len(matrix)):
        matrix[i][i] *= 2
    return matrix


def main() -> None:
    matrix = create_matrix(5)
    print(f"Исходная матрица:")
    print_array(matrix)
    print("Матрица с значениями главной диагонали увеличенные в 2 раза:")
    print_array(square_matrix(matrix))


if __name__ == "__main__":
    main()
