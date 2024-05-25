import pickle


class Counter:
    def __init__(self):
        self.counter_num = 0

    def increment(self):
        self.counter_num += 1

    def decrement(self):
        self.counter_num -= 1

def save_def(filename, instance):
    with open(filename, 'wb') as f:
        pickle.dump(instance, f)

def load_def(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


# Сохранение экземпляров класса
counter1 = Counter()
counter1.increment()

counter2 = Counter()
counter2.increment()
counter2.increment()

counter3 = Counter()
counter3.decrement()

save_def('counters.data', [counter1, counter2, counter3])

# Загрузка экземпляров класса из файла
loaded_counters = load_def('counters.data')

# Демонстрация загруженных экземпляров
for counter in loaded_counters:
    print(counter.counter_num)
