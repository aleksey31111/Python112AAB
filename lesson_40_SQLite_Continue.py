import sqlite3 as sq

################## Data Base ######################

print("# SELECT [ALL | DISTINCT] {|СТОЛБЕЦ1 [, СТОЛБЕЦ2]}")
print("ТАБЛИЦА1 [, ТАБЛИЦА2]")
print("WHERE (условие)")
print("\t - Операторы сравнения.")
print("\t - BETWEEN a AND b")
print("\t - LIKE ( NOT LIKE ) : : %-Любое Количество Символов; _-Любой Одиночный Символ;")
print("IS NULL")
print("# GLOB # : *-Любое Количество Символов; ?-Любой Одиночный Символ;\n"
      "\t\t.-Любой Одиночный Символ; [abc]-Один Из Заданных Символов;\n"
      "\t\t[0-8a-zA-Z]-Заданный диапазон;\n"
      "\t\t^-[^abc]-Любой кроме Заданных")
print("\tIN (NOT IN) (Набор значений)")
print("Переименование Поля Заголовка:"
      "1) - SELECT FName AS Фамилия;")
print("ORDER BY имя_поля [ASC|DESC] - Сортировка Поля По Возрастанию | Убыванию.")
# LIMIT
# IN (NOT IN) -
print("3 - Способ Создания БД SQLite."
      "\nINTEGER PRIMARY KEY AUTOINCREMENT,"
      "\nNOT NULL, BLOB NOT NULL DEFAULT, INTEGER NOT NULL CHECK(age > 0 AND age < 100),"
      "\nemail TEXT UNIQUE")
print("Переименование Табшлицы В БД.")
# with sq.connect('user_home_40.db') as con:
#     cur = con.cursor()
    #     # cur.execute("DROP TABLE users")
    #     cur.execute("""CREATE TABLE IF NOT EXISTS person_home_40(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name TEXT NOT NULL,
    #     phone BLOB NOT NULL DEFAULT +79090000000,
    #     age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
    #     email TEXT UNIQUE
    #     )""")

    #     cur.execute("""
    #     ALTER TABLE person_home_40
    #     RENAME TO person_table_home_40;
    #     """)

    #     cur.execute("""
    #     ALTER TABLE person_table_home_40
    #     ADD COLUMN address;
    #     """)

    # cur.execute("""
    #     ALTER TABLE person_table_home_40
    #     RENAME COLUMN address TO home_address
    # """)

    # cur.execute("""
    #     ALTER TABLE person_table_home_40
    #     DROP COLUMN home_address
    # """)

    # cur.execute("""
    #         DROP TABLE person_table_home_40
    # """)

    # cur.execute("""
    #         DROP TABLE person
    # """)

print("### INSERT -  Добавляет Новые Строки В Таблицу:"
      "\nINSERT INTO имя_таблицы [(столбец1 [, столбец2)] VALUE (значение1 [,значение2])]")
print("### UPDATE - Изменяет Строки")
print("### DELETE - Удаляет Строки")
print("INSERT INTO имя_таблицы [(столбец1 [, столбец2)] VALUE (значение1 [,значение2])]")
print("SELECT список_столбцов")
print("FROM таблица")
print("WHERE условие")

with sq.connect('I:\PythonCours\Python\lesson_40_30_05_22/db_4.db') as con:
    cur = con.cursor()
    cur.execute("""
    SELECT *
    FROM Ware
    ORDER BY Price DESC
    LIMIT 2,5;
    """)
    # res = cur.fetchall()
    # print(res)
    # for res in cur:
    #     print(res)
    res = cur.fetchone()
    res2 = cur.fetchmany()
    print(res)
    print(res2)
