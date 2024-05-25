import tkinter as tk
from tkinter import messagebox

def main_number(number: int) -> None:
    last_digit = number % 10
    middle_digit = (number % 100) // 10
    result = f"Последняя цифра (единица): {last_digit}\nСредняя цифра (десятки): {middle_digit}"
    messagebox.showinfo("Результат", result)

def check_number() -> None:
    number_str = entry.get()
    try:
        number = int(number_str)
        if len(str(number)) == 3:
            main_number(number=number)
        else:
            messagebox.showerror("Ошибка", "Введенное вами число не трехзначное")
    except ValueError:
        messagebox.showerror("Ошибка", "Требуется ввести число")

# Создаем основное окно
root = tk.Tk()
root.title("Анализ трёхзначного числа")

# Создаем метку и поле ввода
label = tk.Label(root, text="Введите трёхзначное число:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

# Создаем кнопку для запуска проверки
button = tk.Button(root, text="Проверить", command=check_number)
button.pack(pady=10)

# Запускаем главный цикл приложения
root.mainloop()