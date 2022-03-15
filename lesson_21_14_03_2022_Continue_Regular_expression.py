# ############ LESSON 21 ###########
##### SPECSYMBOL Mean REAPETE - Output SYMBOLS Pattern Before 1 NOT a MATCH,
#####  after That Substitutes Pattern Again, for Match.
# # + = Количество Повторений РЕГУЛЯРНЫХ ВЫРАЖЕНИЙ от 1 До Бесконечности.
# # * =  Количество Повторений РЕГУЛЯРНЫХ ВЫРАЖЕНИЙ от 0 До Бесконечности.
# # ? =   Количество Повторений РЕГУЛЯРНЫХ ВЫРАЖЕНИЙ от 0 До 1.
import re

s = "Я ищу совпадения в 2021 году. И я их обязательно найдую 4546"
reg1 = r'\w'  # Шаблон Для ОДНОГО СИМВОЛА или ЦИФРЫ До "Точки" или "Пробела"
reg2 = r'\w+'  # Шаблон Для СИМВОЛОВ и ЦИФР Встречающихся Больше ОДНОГО РАЗА, До "Точки" или "Пробела"
reg3 = r'\d'  # Шаблон Для ОДНОЙ ЦИФРЫ До "Символа" или "Точки" или "Пробела"
reg4 = r'\d+'  # Шаблон Для ЦИФР До "Символа" или "Точки" или "Пробела"
reg5 = r'20*'  # Шаблон Сначала Для 2-ек, После Для 0-ей До "Символа" или "ДРУгОЙ ЦИФРЫ" или "Точки" или "Пробела"
reg6 = r'20?'  # Шаблон Сначала Для 2-ек, После Для 0-ей 0-Раз или 1-Раз До "Символа" или "ДРУгОЙ ЦИФРЫ" или "Точки" или "Пробела"
print(s)
print("Пример РЕГУЛЯРНЫХ ВЫРАЖЕНИЙ: \n \
 1)r'\w' 2)r'\w+' 3)r'\d' 4)r'\d+' 5)r'20*' 6)r'20?'")
print(re.findall(reg1, s))
print(re.findall(reg2, s))
print(re.findall(reg3, s))
print(re.findall(reg4, s))
print(re.findall(reg5, s))
print(re.findall(reg6, s))
print()

d = "Цифры: 7, +17, -42, 0013, 0.3"
print(d)
print("Пример РЕГУЛЯРНЫХ ВЫРАЖЕНИЙ: \n \
1)r'\d' 2)r'\d+' 3)r'\+?\d+' 4)r'-?\d+' 5)r'[-=]?\d+' 6)r'[\+]?[\d.]+'")
print(re.findall(r'\d', d))
print(re.findall(r'\d+', d))
print(re.findall(r'\+?\d+', d))
print(re.findall(r'-?\d+', d))
print(re.findall(r'[-+]?\d+', d))
print(re.findall(r'[\+]?[\d.]+', d))
print()

# #### EXAMPLE 1: ####
print("EXAMPLE 1: Избавится От КОМЕНТАРИЯ, и 'Дата рождения' Укакзать Сначала а Затем ДАТУ\n \
Используем re.sub(r'#.', '', s1")
s1 = "05-03-1987 # Дата рождения"
print("Дата рождения: ", re.sub(r'#.*', "", s1))
print()

# ### Task 1 ###
print("Задача 1: Заменить в  ДАТЕ РОЖДЕНИЯ '-' на '.'.")
print("Variant 1: Задание 1 Урок 21")
s1 = "05-03-1987 # Дата рождения"
print(s1)
print(re.sub(r'-', '.', s1))
print()
print("Variant 2: Задание 1 Урок 21 и Удалить КОММЕНТАРИЙ.")
s1 = "05-03-1987 # Дата рождения"
print(s1)
print('Дата рождения:', re.sub(r'-', '.', re.sub(r'#.*', '', s1)))
print()
print("Variant 3: Задание 1 Урок 21")
s1 = "05-03-1987 # Дата рождения"
print(s1)
print("Дата рождения:", re.sub(r"-", ".", s1))
print()
print()

#### EXAMPLE 2 ####
print("EXAMPLE 2: Напишите РЕГУЛЯРНОЕ ВЫРАЖЕНИЯ Для Нахождения Всех КЛЮЧЕЙ и ЗНАЧЕНИЙ")
import re

s2 = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
print("Исходная СТРОКА: ", s2)
print("Используем Шаблоны: 1)r'\w+\s*=\s*\w+\s*\w*' 2)r'\w+\s*=\s*[^;]+' 3)r'\w+\s*=[^;]+'")
reg = r'\w+\s*=\s*\w+\s*\w*.?\w?.?'
reg1 = r'\w+\s*=\s*[^;]+'
reg2 = r'\w+\s*=[^;]+'
print(re.findall(reg, s2))
print(re.findall(reg1, s2))
print(re.findall(reg2, s2))
print()

##### CONTINUE Lesson #####
print("{n} = Ровно n Повторений.")

#### Example 3: ####
print("EXAMPLE 3: {n}")
import re

s3 = "12 сентября 2021 года 45478912"
reg1 = r"\d{2,4}"  # Искать ЦИФРЫ От 2 До 4
print(re.findall(reg1, s1))
print()

print("EXEMPLE 4: Вывод АБРЕВИЯТУР с Помощью РВ.")
# ### ABREVIATURE ###
s4 = "МИД - Министерство иностранных делб ГЭС - гидроэлектростанция, ФСБ - Федеральная служба безопасности"
reg1 = r'[А-Я]{3}'
reg2 = r"[А-ЯЁ]{2,}"
reg3 = r"[А-ЯЁ]{2,}\s*[А-ЯЁ]*"
print(re.findall(reg1, s4))
print(re.findall(reg2, s4))
print(re.findall(reg3, s4))
print()

### Task 3: ###
print("Задача 3: Найти НОМЕР ТЕЛЕФОНА в Формате +7хххххххххх или 7хххххххххх")
print("Variant 1: Задача 3 Урок 21")
s5 = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
pat = r'[+]?\d{10}'
print(re.findall(pat, s5))
print()

print("Variant 2: Задача 3 Урок 21")
s5 = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
reg = r"[+]?[0-9]{11}"
print(re.findall(reg, s5))
print()

print("Variant 3: Задача 3 Урок 21")
s5 = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
reg = r"\+?7[0-9]{10}"
print(re.findall(reg, s5))
print()

print("Variant 4: Задача 3 Урок 21")
reg = r'\+*\d{10}[^,]'
print(re.findall(reg, s5))
print()

print("Variant 5: Задача 3 Урок 21")
s5 = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
reg = r'[+]*\d{11}'
print(re.findall(reg, s5))
print()

print("Variant 6: Задача 3 Урок 21")
reg = r"[+]?7\d{2,}"
print(re.findall(reg, s5))
print()
print()
##### CONTINUE Lesson #####
print("METACHARACTER In REGULAR EXPRESSIO: ^ - Begin Of String, $ - Finit Of String. ")
print("Use Follow RE: 1)r'^\w+\s\w+' 2)r'\w+\s\w+' 3)r'\w+.$' 4)r'\w+\.$' 5)r'\w+\.'")
# import re
s6 = "Я ищу совпадения в 2021 году. И я их обязательно найду. 4546"
s7 = "Я ищу совпадения в 2021 году. И я их обязательно найду."
print("SOURCE String 1: " + s6)
reg1 = r'^\w+\s\w+'
reg2 = r'\w+\s\w+'
reg3 = r'\w+.$'
reg4 = r'\w+\.$'
reg5 = r'\w+\.'
print(re.findall(reg1, s6))
print(re.findall(reg2, s6))
print(re.findall(reg3, s6))
print(re.findall(reg4, s6))
print(re.findall(reg5, s6))
print("SOURE String 2: " + s7)
print(re.findall(reg1, s7))
print(re.findall(reg2, s7))
print(re.findall(reg3, s7))
print(re.findall(reg4, s7))
print(re.findall(reg5, s7))
print()
print()
print()
print()
# ################### FLAGS #######################
print("\t\t\t\t FLAGS ( ФЛАГИ )  \t\t\t\t")
print("Flags: 1)re.ASCII(re.A); 2)re.IGNORECASE(re.I); 3)re.MULTILINE(re.M); \n \
4)re.DOTALL(re.S); 5)re.VERBOSE(re.X); 6)re.DEBUG")
# import re
print("1) Flag - re.ASCII ( re.A )")
s8 = "12 сентября 2021 года 45478912"
print(re.findall(r"\w+", "12 + й"))
print(re.findall(r"\w+", "12 + й", flags=re.ASCII))
print(re.findall(r"\w+", "12 + g", flags=re.A))
print()

print("6) Flag - re.DEBUG ")
s9 = 'hello world'
print(re.findall(r"\w+", s9, flags=re.DEBUG))
print(re.findall(r"\w\+", s9, flags=re.DEBUG))
print()

print("6) Flag - re.IGNORECASE ( re.I ) ")
s10 = "Я ищу совпадения в 2021 году. И я их обязательно найду."
reg = r'я'
print(re.findall(reg, s10))
print(re.findall(reg, s10, re.I))
print(re.findall(reg, s10, flags=re.I))
print()

print("4) Flag - re.DOTALL ( re.S ) ")
# import re
text = """
one
two
"""
print(re.findall(r"one.\w+", text))
print(re.findall(r"one.\w+", text, flags=re.DOTALL))
print()

print("4) Flag - re.MULTILINE ( re.M ) ")
print(re.findall(r"one$", text))
print(re.findall(r"one$", text, flags=re.MULTILINE))
print()

print("EXAMPLE: Multiline, Dotall")
# import re
text = """
{
"one": 1,
"two": 2,
"three": 3
}
"""
print(re.findall(r'^["\w+]+', text))
print(re.findall(r'^["\w]+', text, flags=re.DOTALL))
print(re.findall(r'^["\w+]+', text, flags=re.MULTILINE))
print()

print("5) Flag - re.VERBOSE ( re.X ) ")
# import re
print(re.findall("""
[a-z.-]+  # part 1
@
[a-z, -]+  # part 2
""", 'test@mail.ru', re.VERBOSE))
print()

print("Use FLAGS In RE: 1)a 2)i 3)m 4)s 5)x")
# import re
text2 = """Python,
python
PYTHON"""
reg = "(?im)^python"
print(re.findall(reg, text2))
print()

print("Польза От Символов ^ - Начало Строки, и $ - Коней Строки.")
print("EXAMPLE 5: Правильность Имени.")


# ##### DEF #####
# import re
def validate_name(name):
    return re.findall(r'^[a-z0-9_-]{3,16}$', name, re.IGNORECASE)


#    return re.findall(r'[a-z0-9_-]{3,16}', name, re.IGNORECASE)


print(validate_name('Python_master'))
print(validate_name(('Py')))
print(validate_name('@Python_master'))
print(validate_name('@Python_master#$%#^&'))
print()

# import re
print("EXAMPLE 7 - Найти Все АДРЕСА Электронной почты.")
print("Variant 1: EXAPMLE 7, LESSON - 21 ")
mail = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
pat = r'[\w._-]+@[\w.-]+[\w]{2,3}'
print(re.findall(pat, mail))
print()

print("Variant 2: EXAPMLE 7, LESSON - 21 ")
s11 = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
reg2 = r"\w*.\w+.\w+@\w+.\w+.ru"
print(re.findall(reg2, s11))
reg3 = r'[а-яa-z0-9_.-]+@[а-яa-z0-9_.-]+'
print(re.findall(reg3, s11))
print()

print("Variant 3: EXAPMLE 7, LESSON - 21 ")
text2 = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3-67@i.ru 1login@ru.name.ru'
reg = r'[a-z0-9._-]*@[a-z0-9._-]*'
print(re.findall(reg, text2))
print()
print()
print()
print()

##### Continue Lesson ##### GRADY and LAIZY SEARCH #####
print("*?, +?, ?? = LAIZY SEARCH")
print("{m,n}?, {,n}?, {m,}? - LAIZY REPETITION")
print()

print("GRADY SEARCH: ")
text6 = "<body>Пример жадного соответствия регулярных выражений</body>"
print(re.findall('<.*>', text6))
print()

print("LAIZY SEARCH: ")
text6 = "<body>Пример жадного соответствия регулярных выражений</body>"
print(re.findall('<.*?>', text6))
print()

print("group() - совпадения.")
text = "<body>Пример жадного соответствия регулярных выражений</body>"
print(re.search('<.*>', text).group())
print(re.search('<.*?>', text).group())

print("Search TEG <img>")
s12 = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
s13 = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
s14 = "<p>Изображение <img> - фон страницы</p>"
reg1 = r"<img.*?>"
reg2 = r"<img.[^>]*>?"
reg3 = r"<img\s+[^>]*?src\s*=\s*[^>]+>"
print(re.findall(reg1, s12))
print(re.findall(reg1, s13))
print(re.findall(reg1, s14))
print(re.findall(reg2, s12))
print(re.findall(reg2, s13))
print(re.findall(reg2, s14))
print(re.findall(reg3, s12))
print(re.findall(reg3, s13))
print(re.findall(reg3, s14))

# reg = r"<img[^>]*>"
# print(re.findall(reg, s2))
# reg = r"<img\s+[^>]*>"
# print(re.findall(reg, s1))


# ### Task 4: ###
print("Задача 4: Найти Все СНОСКИ в КВАДРАТНЫХ СКОБКАХ.")
text8 = "Python (в русском языке распространено название пито́н[16] или пайтон[17]) — высокоуровневый язык " \
       "программирования общего назначения с динамической типизацией и автоматическим управление памятью[18][19]."
# print(re.findall(r".[\d[^]]", text))
print(re.findall(r"\[.*?]", text8))
print()
print()

# #### CONTINUE Lesson ####
print("Или в РЕ: |")
s15 = "Петр, Ольга и Виталий отлично учатся!"
reg = r"Петр|Ольга|Виталий"
print(re.findall(reg, s15))
print()

print("?:) - группирующая скобка является не сохраняюцей")
print("() - группирующая скобка является сохраняюцей.")
s16 = "int = 4, float = 4.0, double = 8.0f"
reg = r"\w+\s*=\s*\d[.\w+]*"
print(re.findall(reg, s16))
reg1=r"int\s*=\s*\d[.\w+]*|float\s*=\s*\d[.\w+]*|double\s*=\s*\d[.\w+]*"
print(re.findall(reg1, s16))
reg2 = r"(?:int|float|double)\s*=\s*\d[.\w+]*"  #(?:) - группирующая скобка .вляется не сохраняюцей
print(re.findall(reg2, s16))
# # () - группирующая скобка .вляется сохраняюцей
