# Дан список размера N. Найти номер его первого локального минимума (локальный
# минимум — это элемент, который меньше любого из своих соседей).

def find_local_minimum(numbers: list) -> int:
    n = len(numbers)

    for i in range(n):
        if i == 0:  # Проверяем первый элемент
            if numbers[i] < numbers[i + 1]:
                return i
        elif i == n - 1:  # Проверяем последний элемент
            if numbers[i] < numbers[i - 1]:
                return i
        else:  # Проверяем остальные элементы
            if numbers[i] < numbers[i - 1] and numbers[i] < numbers[i + 1]:
                return i

    return -1  # Если локальный минимум не найден


if __name__ == "__main__":
    numbers = list()
    try:
        numbers = [int(i) for i in input("Введите числа через пробел: ").split()]

        index = find_local_minimum(numbers)
        if index != -1:
            print("Номер первого локального минимума:", index)
        else:
            print("Локальный минимум не найден")
    except ValueError:
        print("Требуется ввести числа!")