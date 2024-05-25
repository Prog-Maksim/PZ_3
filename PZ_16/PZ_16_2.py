# Создайте класс "Автомобиль", который содержит информацию о марке, модели и
# годе выпуска. Создайте класс "Грузовик", который наследуется от класса
# "Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
# "Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
# информацию о количестве пассажиров.

class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year


class Truck(Car):
    def __init__(self, brand: str, model: str, year: int, carrying_capacity: float):
        super().__init__(brand, model, year)
        self.carrying_capacity = carrying_capacity


class PassengerCar(Car):
    def __init__(self, brand: str, model: str, year: int, passenger_capacity: int):
        super().__init__(brand, model, year)
        self.passenger_capacity = passenger_capacity
