# Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16', отражающая продажи продукции по дням в кг.
# Преобразовать информацию из строки в словари, с использованием функции найти максимальные продажи по
# каждому виду продукции, результаты вывести на экран.

class SalesStatistics:
    def __init__(self, text: str):
        self.fruit_string = text
        self.__fruit_dict = self.__string_conversion()
        self.__stats()

    def data_values(self):
        return self.__fruit_dict

    def __string_conversion(self) -> dict:
        """
        Преобразовывает переданную строку классу.
        Возвращает ошибку если строку не удалось преобразовать.
        :return: Преобразованая строка в словарь.
        """
        fruits_list = self.fruit_string.split()
        fruits_dict = dict()
        current_fruit = str()

        for item in fruits_list:
            if item.isalpha():
                current_fruit = item
                fruits_dict[current_fruit] = list()
            else:
                fruits_dict[current_fruit].append(int(item))

        if fruits_dict is not None:
            return fruits_dict
        raise ValueError("Invalid string fruit")

    def __stats(self) -> None:
        """
        Создает словари данных хранящие в себе минимальные и максимальные продажи за определнный день.
        :return: Ничего.
        """

        self.__min_values = {fruit: (min(self.__fruit_dict[fruit]), self.__fruit_dict[fruit].index(min(self.__fruit_dict[fruit])) + 1) for fruit in self.__fruit_dict}
        self.__max_values = {fruit: (max(self.__fruit_dict[fruit]), self.__fruit_dict[fruit].index(max(self.__fruit_dict[fruit])) + 1) for fruit in self.__fruit_dict}

    def min_sales(self) -> str:
        """
        Информация по фруктам о минимально проданном кол-во фруктов за день
        :return: строка информации.
        """
        result = [f"{self.__min_values[fruit][1]} дня было продано: {self.__min_values[fruit][0]} {fruit}" for fruit in self.__min_values]

        return "\n".join(result)

    def max_sales(self) -> str:
        """
        Информация по фруктам о максимально проданном кол-во фруктов за день
        :return: строка информации.
        """
        result = [f"{self.__max_values[fruit][1]} дня было продано: {self.__max_values[fruit][0]} {fruit}" for fruit in self.__max_values]

        return "\n".join(result)

    def __str__(self) -> str:
        result = [f"Общая сумма продаж {fruit} за {len(num)} дней: {sum(num)} штук" for fruit, num in self.__fruit_dict.items()]
        return "\n".join(result)

    def __call__(self, *args, **kwargs):
        print("Минимальные продажи:")
        print(self.min_sales())
        print("Максимальные продажи:")
        print(self.max_sales())


if __name__ == "__main__":
    a = SalesStatistics("апельсины 45 991 63 100 12 яблоки 13 47 26 0 16")
    a()
    print()
    print(a)
