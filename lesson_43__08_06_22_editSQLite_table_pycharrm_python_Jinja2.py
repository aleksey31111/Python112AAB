### LESSON 43 ###
import sqlite3 as sq

# cars = [
#     ('BMV',54000),
#     ('Shevrolet',54000),
#     ('BMV2',54000),
#     ('Citroen',54000),
#     ('Honday',54000),
#
# ]


# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#
#
with sq.connect('cars_home_43.db') as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS users(
        model TEXT,
        ava BLOB,
        score INTEGER
    );
    """)
print("Выбореа Из Таблицы Одного Элемента ava")
#     cur.execute("SELECT ava FROM users LIMIT 1")
#     img=cur.fetchone()['ava']
#     write_ava('out.png', img)
print("Чтение картинки")
# img = read_ava(1)
# if img:
#     binary = sq.Binary(img)
#     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))

print("### Создание таблицы продажи ###"
      "\n# CREATE TABLE IF NOT EXISTS cost( "
    "\n# name"
    "\n# TEXT, tr_in"
    "\n# INTEGER, buy"
    "\n# INTEGER"
    "\n)")
print("Выборка Из Таблицы cars")
#    # cur.execute("SELECT model, price FROM cars")
print("Выборка con.row_factory = sq.Row")
# print(con.row_factory)
print("Получение cur.fetchall(), cur.fetchone(), cur.fetchmany()")
# rows = cur.fetchall()
# rows = cur.fetchone()
# rows = cur.fetchmany()
# print(rows)
print("Цикл Из cur res['model'], res['price']")
#   for res in cur:
#       print(res['model'], res['price'])
print("Вставка в Таблицу cars Запорожец и Покупка Ильей")
# cur.execute("INSERT INTO cars VALUES(NULL, 'ZАПОРОЖЕЦ', 1000)")
# last_row_id = cur.lastrowid # id last Entry
# buy_car_id = 2  # auto that Customer Buy
# cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))
print("Выполнение нескольких execute Через executescript")
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)

# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

# cur.executemany("INSERT INTO cars VALUES(NULL,?,?)",cars)

# for car in cars:
#     cur.execute("INSERT INTO cars VALUES(NULL,?,?)",car)

# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
# cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars VALUES(3, 'Mersede', 57000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")

# con.commit() - Сохр изменения в БД
# con.close()
# con=None
# try:
#     con = sq.connect('cars.db')
#     cur = con.cursor()
#     con.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars2 SET price = price + 100;
#     """)
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка Выполнения Запроса")
# finally:
#     if con:
#         con.close()


# with sq.connect('cars.db') as con:
#     # con.row_factory = sq.Row
#     cur=con.cursor()
#     # with open("sql_dump.sql", "w") as f:
#     #     for sql in con.iterdump():
#     #         f.write(sql)
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)

# data = [("car", "машина"), ("house", "дом"), ("tree", "дерево")]
# con = sq.connect(':memory:')
# with con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS dict(
#     eng TEXT,
#     rus TEXT)
#     """)
#
#     cur.executemany("INSERT INTO dict VALUES(?, ?)", data)
#
#     cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
#     print(cur.fetchall())


###### WSGI #####
### Шаблонизатор - Jinja ### pip install
# {{ }} - Выражение для вставеи Конструкции Python  в Шаблон
# {% %} - Спецификация шаблона
# {# #} - Блок комментариев
# ## - Строчный комментарий

from jinja2 import Template

# class Person:
#     def __init__(self):
#
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#
# per = {'name':"Игорь", 'age':28}
# # name = 'Игорь'
# age=28
# tm = Template("Мне {{ a*2 }} лет. Меня зовут {{ name }}")
# # msg = tm.render(n=name, a=age)
# msg = tm.render(p=per)
# print(msg)

# data = """{% raw %}Строка, с названием {{ name }}. Со значением {% endraw %}"""
# tm = Template(data)
# msg = tm.render(name="Igor")
#
# print(msg)
#
# link = "<a href='#'>SSulka</a>"
# tm=Template("{{ link | e}}}")
# msg = tm.render(link=link)
# print(msg)


## HOMEWORK 43 ##
# Созд БД. Добавить Данные через PyCharm(Python)
