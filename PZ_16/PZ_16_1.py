class counter:
    def __init__(self):
        self.counter_num = 0

    def increment(self):
        self.counter_num += 1

    def decrement(self):
        self.counter_num -= 1


count = counter()
print(count.counter_num)  # Вывод: 0
count.increment()
print(count.counter_num)  # Вывод: 1
count.decrement()
print(count.counter_num)  # Вывод: 0
