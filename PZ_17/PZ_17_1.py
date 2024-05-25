import tkinter as tk
from tkinter import ttk

def submit():
    print("Регистрация прошла успешно")

def clear():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_confirm_password.delete(0, tk.END)
    combo_specialization.set('')
    gender.set(None)
    for var in skills_vars:
        var.set(0)
    text_additional_info.delete('1.0', tk.END)

# Создание главного окна
root = tk.Tk()
root.title("Анкета Web-разработчика")

# Фреймы для левой и правой стороны с разными цветами фона
left_frame = tk.Frame(root, bg='lightgray')
right_frame = tk.Frame(root, bg='gray')

left_frame.grid(row=0, column=0, rowspan=13, sticky='nsew')
right_frame.grid(row=0, column=1, columnspan=3, rowspan=13, sticky='nsew')

# Добавление разделительной линии
separator1 = ttk.Separator(root, orient='vertical')
separator1.grid(row=0, column=1, rowspan=12, padx=5)

# Метка и поле для имени пользователя
tk.Label(root, text="Регистрационное имя", bg='lightgray').grid(row=0, column=0, sticky='e')
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, columnspan=3, sticky='we', padx=(0, 5))

# Добавление разделительной линии
separator1 = ttk.Separator(root, orient='horizontal')
separator1.grid(row=1, column=0, columnspan=4, sticky='ew', pady=5)

# Метка и поля для пароля
tk.Label(root, text="Пароль", bg='lightgray').grid(row=2, column=0, sticky='e')
entry_password = tk.Entry(root, show='*')
entry_password.grid(row=2, column=1, sticky='we')

tk.Label(root, text=": подтвердите пароль", bg='gray').grid(row=3, column=2, sticky='w')
entry_confirm_password = tk.Entry(root, show='*')
entry_confirm_password.grid(row=3, column=1, sticky='we')

separator2 = ttk.Separator(root, orient='horizontal')
separator2.grid(row=4, column=0, columnspan=4, sticky='ew', pady=5)

# Метка и выпадающий список для специализации
tk.Label(root, text="Ваша специализация", bg='lightgray').grid(row=5, column=0, sticky='e')
combo_specialization = ttk.Combobox(root, values=["Web-мастер", "Программист", "Дизайнер"])
combo_specialization.grid(row=5, column=1, sticky='we')

separator2 = ttk.Separator(root, orient='horizontal')
separator2.grid(row=6, column=0, columnspan=4, sticky='ew', pady=5)

# Метка и радиокнопки для выбора пола
tk.Label(root, text="Пол", bg='lightgray').grid(row=7, column=0, sticky='e')
gender = tk.StringVar(value="М")
tk.Radiobutton(root, text='М', variable=gender, value='М', bg='gray').grid(row=7, column=1, sticky='w')
tk.Radiobutton(root, text='Ж', variable=gender, value='Ж', bg='gray').grid(row=7, column=2, sticky='w')

separator2 = ttk.Separator(root, orient='horizontal')
separator2.grid(row=8, column=0, columnspan=4, sticky='ew', pady=5)

# Метка и флажки для навыков
tk.Label(root, text="Ваши навыки", bg='lightgray').grid(row=9, column=0, sticky='ne')
skills_frame = tk.Frame(root, bg="gray")
skills_frame.grid(row=9, column=1, columnspan=3, sticky='w')

skills = ["знание HTML и CSS", "знание Perl", "знание ASP", "знание Adobe Photoshop", "знание JAVA", "знание JavaScript", "знание Flash"]
skills_vars = [tk.IntVar() for _ in skills]

for skill, var in zip(skills, skills_vars):
    tk.Checkbutton(skills_frame, text=skill, variable=var, bg='gray').pack(anchor='w')

separator2 = ttk.Separator(root, orient='horizontal')
separator2.grid(row=10, column=0, columnspan=4, sticky='ew', pady=5)

# Метка и текстовое поле для дополнительной информации
tk.Label(root, text="Дополнительные сведения о себе", bg='lightgray').grid(row=11, column=0, sticky='ne')
text_additional_info = tk.Text(root, width=40, height=5)
text_additional_info.grid(row=11, column=1, columnspan=3, sticky='we', padx=(0, 5))

separator2 = ttk.Separator(root, orient='horizontal')
separator2.grid(row=12, column=0, columnspan=4, sticky='ew', pady=5)

# Кнопки регистрации и очистки формы
button_frame = tk.Frame(root)
button_frame.grid(row=13, column=1)

tk.Button(button_frame, text="зарегистрироваться", command=submit).pack(side='left', padx=5, pady=(0, 5))
tk.Button(button_frame, text="очистить форму", command=clear).pack(side='left', padx=5, pady=(0, 5))

# Настройка расширяемости столбцов
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.mainloop()