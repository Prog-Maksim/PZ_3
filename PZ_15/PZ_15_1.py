# Приложение КАФЕДРА для автоматизации работы отдела кадров ВУЗа. Таблица
# Преподавательский состав должна содержать следующие данные: Табельный номер,
# Фамилия И.О., Дата рождения, Должность, Ученая степень, Нагрузка, Зарплата.

import sqlite3


def create_database():
    with sqlite3.connect("my_database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
                CREATE TABLE if not exists teachers (
    service_number VARCHAR(5),
    surname VARCHAR(30),
    name VARCHAR(30),
    middle_name VARCHAR(30),
    birthday DATETIME,
    post VARCHAR(30),
    academic_degree INT,
    load INT,
    price FLOAT(5,2)
);
                """)

        conn.commit()


def show_tables(data: list):
    for i in data:
        print(i)

def insert_data():
    with sqlite3.connect("my_database.db") as conn:
        cursor = conn.cursor()

        commands = """INSERT INTO teachers VALUES ('00001', 'Филиппов', 'Михаил', 'Никитич', '2000-04-10', 'Программист', 4, 100, 49999);
INSERT INTO teachers VALUES ('00002', 'Воронин', 'Давид', 'Сергеевич', '2000-05-10', 'Историк', 1, 249, 99000.00);
INSERT INTO teachers VALUES ('00003', 'Михеев', 'Тигран', 'Никитич', '1985-07-18', 'Математик', 2, 48, 79466.00);
INSERT INTO teachers VALUES ('00004', 'Ильина', 'Анастасия', 'Антоновна', '1988-12-16', 'Физик', 5, 74, 38683.00);
INSERT INTO teachers VALUES ('00005', 'Морозова', 'Татьяна', 'Робертовна', '1994-03-09', 'Программист', 2, 126, 77151.00);
INSERT INTO teachers VALUES ('00006', 'Анисимов', 'Лука', 'Сергеевич', '1999-08-13', 'Историк', 2, 200, 82879.00);
INSERT INTO teachers VALUES ('00007', 'Федорова', 'Елизавета', 'Кирилловна', '1989-01-17', 'Математик', 3, 34, 65008.00);
INSERT INTO teachers VALUES ('00008', 'Жданов', 'Даниил', 'Маркович', '1997-10-20', 'Физик', 1, 218, 99223.00);
INSERT INTO teachers VALUES ('00009', 'Баранова', 'Анна', 'Ивановна', '1991-05-25', 'Программист', 4, 178, 54795.00);
INSERT INTO teachers VALUES ('00010', 'Виноградов', 'Кирилл', 'Эмирович', '1995-09-01', 'Историк', 2, 159, 88338.00);"""
        commands = commands.split(";")
        for i in commands:
            cursor.execute(i)

            conn.commit()


def search_data():
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
        print("Преподаватели к которых зарплаты больше 70 тыс.руб")
        command = """SELECT service_number, surname, name, middle_name, birthday, post, academic_degree, load, price FROM teachers WHERE price > 70000 ORDER BY price DESC;"""
        cursor.execute(command)
        print(show_tables(cursor.fetchall()))
        print("-------------------")

        print("Базовая ставка заработной платы преподавателей программистов")
        command = """SELECT service_number, surname, name, middle_name, price / load AS 'Базовая ставка' FROM teachers WHERE post = 'Программист';"""
        cursor.execute(command)
        print(show_tables(cursor.fetchall()))
        print("-----------------------")

        print("Преподаватели у которых день рождение после 1995-05-01")
        command = """SELECT service_number, surname, name, middle_name, birthday FROM teachers WHERE birthday >= '1995-05-01';"""
        cursor.execute(command)
        print(show_tables(cursor.fetchall()))

def update_data():
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
        command = """UPDATE teachers SET load = (load + 30), price = price + (price * 30 / 100) WHERE load <= 50; 
        UPDATE teachers SET post = 'Физик ядерщик' WHERE post = 'Физик'; 
        UPDATE teachers SET load = load - (load * 15 / 100) WHERE load >= 200;"""
        commands = command.split(";")

        for i in commands:
            cursor.execute(i)

        conn.commit()


def delete_data():
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()

        command = """DELETE FROM teachers WHERE post = 'Физик ядерщик';
DELETE FROM teachers WHERE price >= 100000;
DELETE FROM teachers WHERE academic_degree >= 4;"""
        commands = command.split(";")

        for i in commands:
            cursor.execute(i)

        conn.commit()

if __name__ == "__main__":
    create_database()
    insert_data()
    search_data()
    # update_data()
    # delete_data()
