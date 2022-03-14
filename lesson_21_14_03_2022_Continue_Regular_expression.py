# ############ LESSON 21 ###########
# # + = 1 - или больше
# # * = 0 - или больше
# # ? = 0 или 1
# import re
#
# s = "Я ищу совпадения в 2021 году. И я их обязательно найдую 4546"
# reg = r'20*'
# reg1 = r'20?'
# print(s)
# print(re.findall(reg, s))
# print(re.findall(reg1, s))
#
# d = "Цифры: 7, +17, -42, 0013, 0.3"
# print(d)
# print(re.findall(r'\d', d))
# print(re.findall(r'\d+', d))
# print(re.findall(r'\+?\d+', d))
# print(re.findall(r'-?\d+', d))
# print(re.findall(r'[-+]?\d+', d))
# print(re.findall(r'[\+]?[\d.]+', d))
#
# #### EXAMPLE 1: ####
# s = "05-03-1987 # Дата рождения"
# print("Дата рождения: ", re.sub(r"#.*", "", s))
#
# ### Task 1 ###
# # print(re.sub('-', '\\.'), s)
#
# print('Дата рождения:', re.sub(r'-', '.', re.sub(r'#.*', '', s)))
#
# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"-", ".", s))
#

#### EXAMPLE 2 ####
# import re
# s = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# reg = r'\w+\s*=\s*\w+\s*\w*'
# reg1 = r'\w+\s*=\s*[^;]+'
# reg2 = r'\w+\s*=[^;]+'
# print(re.findall(reg, s))
# print(re.findall(reg1, s))
# print(re.findall(reg2, s))

##### CONTINUE Lesson #####
## {n} = Ровно n Повторений.

#### Example 3: ####
# import re
# s1 = "12 сентября 2021 года 45478912"
# reg1 = r"\d{2,4}"
# print(re.findall(reg1, s1))

# ### ABREVIATURE ###
# s1 = "МИД - Министерство иностранных делб ГЭС - гидроэлектростанция, ФСБ - Федеральная служба безопасности"
# reg1 = r"[А-ЯЁ]{2}s*[А-ЯЁ]*"
# print(re.findall(reg1, s1))
#
# ### Task 3: ###
# # s2 = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
#
# # s3 = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# # reg = r"[0-9]{11}"
# # print(re.findall(reg, s3))
#
# s3 = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg = r"\+?7[0-9]{10}"
# print(re.findall(reg, s3))

# reg = '\+*\d{10}[^,]

# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg = r'[+]*\d{11}'
# print(re.findall(reg, s))

# reg = r"[+]?7\d{2,}"


##### CONTINUE Lesson #####
# import re
# s = "Я ищу совпадения в 2021 году. И я их обязательно найдую 4546"
# reg = r'\w+\s\w+'
# reg = r'\w+\.$'
# print(re.findall(reg,s))

# ################### FLAGS #######################
# import re
#
# s1 = "12 сентября 2021 года 45478912"
# print(re.findall(r"\w", "12 + й"))
# print(re.findall(r"\w", "12 + й", flags=re.ASCII))
#
# s4 = 'hello world'
# print(re.findall(r"\w+", s4, flags=re.DEBUG))
#
#
# s = "Я ищу совпадения в 2021 году. И я их обязательно найду."
# reg = r'я'
# print(re.findall(reg, s, re.I))


# import re
# text = """
# one
# two
# """
# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, flags=re.DOTALL))
# print(re.findall(r"one&", text, flags=re.MULTILINE))


# import re
# text = """
# "one": 1,
# "two": 2,
# "three": 3
# """
# print(re.findall(r'^["\w+]+', text))
# print(re.findall(r'^["\w+]+', text, flags=re.DOTALL))
# print(re.findall(r'^["\w+]+', text, flags=re.MULTILINE))


# import re
# print(re.findall("""
# [a-z,-]+  # part 1
# @
# [a-z, -]+  # part 2
# """), 'test@mail.ru', re.VERBOSE)

# import re
# text = """Python,
# python
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))


# ##### DEF #####
# import re
#
#
# def validate_name(name):
#     # return re.findall(r'^[a-z0-9_-]{3,16}$', name, re.IGNORECASE)
#     return re.findall(r'[a-z0-9_-]{3,16}', name, re.IGNORECASE)
#
# print(validate_name('Python_master'))
# print(validate_name(('Py')))
# print(validate_name('@Python_master'))
# print(validate_name('@Python_master#$%#^&'))

import re

# mail = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
# pat = ['\w*@']

# s = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# reg2 = r"[+]?7\d{2,}"
# print(re.findall(reg2, s))
# reg3 = r'[а-яa-z0-9_.-]+@[а-яa-z0-9_.-]+'
# print(re.findall(reg3, s))

# s = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# reg4 = "[а-я0-9@.a-z_-]+"
# reg4 = r"[\w.-]+@[\w.=]+[\w]{2.3}"
# print(re.findall(reg4, s))

# text2='123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3-67@i.ru 1login@ru.name.ru'
# reg=r'[a-z0-9._-]*@[a-z0-9._-]*'
# print(re.findall(reg,text2)


##### Continue Lesson ##### GRADY and LAIZY SEARCH #####
# *?, +?, ?? = LAIZY SEARCH
# {m,n}?, {,n}?, {m,}?

# text ="<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))

# text ="<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text).group())

# s1="<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# s2="<p>Изображение <img> - фон страницы</p>"
# reg = r"<img.^>?"
# print(re.findall(reg, s1))
# reg = r"<img[^>]*>"
# print(re.findall(reg, s2))
# reg = r"<img\s+[^>]*>"
# print(re.findall(reg, s1))


# ### task 5: ###
# text = "Python (в русском языке распространено название пито́н[16] или пайтон[17]) — высокоуровневый язык " \
#        "программирования общего назначения с динамической типизацией и автоматическим управление памятью[18][19]."
# # print(re.findall(r".[\d[^]]", text))
# print(re.findall(r"\[.*?]", text))


# #### CONTINUE Lesson ####
# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = r"Петр|Ольга|Виталий"
# print(re.findall(reg, s))

s = "int = 4, float = 4.0, double = 8.0f"
reg = r"\w+\s*=\s*\d[.\w+]*"
print(re.findall(reg, s))
reg1=r"int\s*=\s*\d[.\w+]*|float\s*=\s*\d[.\w+]*"
print(re.findall(reg1, s))
reg2 = r"(?:int|float)\s*=\s*\d[.\w+]*"  #(?:) - группирующая скобка .вляется не сохраняюцей
print(re.findall(reg2, s))
# () - группирующая скобка .вляется сохраняюцей