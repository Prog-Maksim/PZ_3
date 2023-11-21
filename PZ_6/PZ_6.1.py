# Дан первый член A и разность D арифметической прогрессии. Сформировать и
# вывести список размера 10, содержащий 10 первых членов данной прогрессии: A, A
# + D, A + 2*D, A + 3*D, ... .

def progressions(a: int, b: int) -> list:
    progression = []

    for i in range(10):
        member = A + i * D
        progression.append(member)

    return progression


if __name__ == "__main__":
    A = int(input("Введите первый член: "))
    D = int(input("Введите разность арифметичекой прогрессии: "))

    print(f"Прогрессия первых 10 членов: {progressions(a=A, b=D)}")