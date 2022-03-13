###### LESSON 20 19.03.2022
##### Continue Method Of String ####
#### rfind - Get 1 - 3 Arguments. -1 - Not FOUND
# s = "hello, WORLD! I am learning Python."
# print(s.rfind("l"))  # Index LAST ELEMENT. 19
# print(s.rfind("l", 3, 20))  # 19
# print(s.rfind("al"))  # Element NOT Found. -1
# print(s.rfind("l", 3, 19))  # 3
# print(s.rfind("l", 0, 19))  # 3
# #### rindex -
# print(s.rindex("l"))  #
# print(s.rindex("l", 3, 20))  # 19
# ###print(s.rindex("al"))  # Element NOT Found. ERROR.
# print(s.rindex("l", 3, 19))  # 3
# print(s.rindex("l", 0, 19))  # 3

### Task 1: ###
# print("Задача 1 На Уроке 20: Дана СТРОКА.\n"
#       "1) Есди БУКВА 'f' Встречается Только Один Раз, Вывести ЕЕ ИНДЕКС.\n"
#       "2) Если БУКВА 'f' Встречается Два и Более Раз, Вывести ИНДЕКС Первого и Последнего Появления.\n"
#       "3) Если БУКВА 'F' Не Встречается, НИЧЕГО Не Выводите.")
# s = "Send unlimited free texts and make WiFi calls from a free phone number. \
# Download the free app or sign up online to pick you free phone namber."
# print("Variant 1: Задача 1 На Уроке 20")
# # print(len(s))
# for i in s:
#     if i == "f" and s.count(i) >= 2:
#         # print(s.index(i))
#         print(s.find(i), end=" ")
#         # print(s.rindex(i))
#         print(s.rfind(i))
#         break
#     elif i == "f" and s.count(i) == 1:
#         # print(s.index(i))
#         # print(s.find(i))
#         # print(s.rindex(i))
#         print(s.rfind(i))
#         break
#
# print("Variant 2: Задача 1 На Уроке 20")
#
#
# def func(x):
#     for i in x:
#         if x.count('f') > 2:
#             print(x.find('f'), x.rfind('f'))
#         if x.count('f') == 1:
#             print(x.find('f'))
#         else:
#             break
#
#
# func(s)
#
# print("Variant 3: Задача 1 На Уроке 20. Верный.")
# c = s
# if c.count('f') > 2:
#     print(s.find('f'), s.rfind('f'))
# elif c.count('f') == 1:
#     print(s.find('f'))

### Task 2: ###
# print("Задача 2 На Уроке 20: Дана СТРОКА, БУКВА 'h' Встречается Два Раза. \n"
#       "1) Удалить Из Жтой СТРОКИ Первое и Последнее Вхождение БУКВЫ 'h',\n"
#       "     а Также Все СИМВОЛЫ Между НИМИ")
# print("Variant 1. Задача 2 На Уроке 20")
# s = "I am learning Python. hello, WORLD!"
# h = 'h'
# s_without_h = ""
# # for letter_h in s:
# if s.count(h) > 1:
#     s_without_h = s[:s.find(h)] + s[s.rfind(h)+1:]
# print(s_without_h)
#
# print("Variant 2. Задача 2 На Уроке 20")
# s = "I am learning Python. hello, WORLD!"
# start = s.find("h")
# end = s.rfind("h")
# print(start, end)
# s1 = s[0:start]
# s2 = s[end + 1:]
# s_new = s1 + s2
# print(s_new)
#
#
# print("Variant 3. Задача 2 На Уроке 20. Правильный ВАРИАНТ.")
# c = 'I am learning Python. hello, World!'
# c = c[:c.find('h')] + c[c.rfind('h') + 1:]
# print(c)

# ###### CONTINUE LESSON ######
# print("Чем Заканчивается, Начинается СТРОКА. Метод str.endswith() str.startswith().\n"
#       "С Тремя Параметрами. Возвращает Булево-ЗНАЧЕНИЕ.")
# s = "hello, WORLD! I am learning Python."
# print(s.endswith("on."))
# print(s.endswith("lo", 0, 5))  # End Str with BOOLERN
# print(s.startswith("hello"))
# print(s.startswith("I am", 14))  # Start Str with BOOLERN
#
# print("Какие ТИПЫ ДАННЫХ в Строке. \n data.isalnum()")
# print('abs123'.isalnum())  # String Contant NUM, STR.  TRUE
# print("5".isalnum())
# print("ы".isalnum())
# print("".isalnum())  # FALSE
#
# print("data.isalpha()")
# print("ABCabc".isalpha())  # Str Contain ONLY LETTER   TRUE
# print("ABC123".isalpha())  # FALSE
#
# print("data.isdigit()")
# print('123'.isdigit())  # Only NAMBER  TRUE
# print('123abc'.isdigit())  # Only NAMBER  FALSE
#
# print("data.isidentifier()")
# print("abc".isidentifier())  # VALID IDENTIFIER
# print("1abc".isidentifier())  # NOT VALID IDENTIFIER
# print("%abc".isidentifier())  # NOT VALID IDENTIFIER
#
# print("data.islower()")
# print('abc'.islower())  # lower NUM and registr LETTER and always Symbol TRUE
# print('Abc'.islower())  # FALSE
# print('abc$123'.islower())  # TRUE
#
# print("data.isspace()")
# print(" \t \n".isspace())  # String Contain SPACE CHARACTER.
# print(" a ".isspace())  # False
#
# print("data.istitle()")
# print("The Apple".istitle())  # Every WORLD 1 Letter Capitalise and NAM and SYMBOL TRUE
# print("The apple".istitle())  # FALSE
#
# print("isupper()")
# print("ABC$!1".isupper())
# print("ABc".isupper())
#
# # ##### FORMAT method #####
# print("Методы ФОРМАТИРОВАНИЯ:")
# print("str.center(all_length, 'sybmbol'")
# print("py".center(29))
# print("py".center(10, "-"))
# print("py".center(3, "#"))
# print("py".center(9, "-"))
#
# print("Очень Полезные МЕТОДЫ:")
# # #### Delete SPICE and NOT ONLY SPACE #####
# print("Удаление ПРОБЕЛОВ: слева - str.lstrip(), str.rstrip() - справа. Пока Есть в Параметре")
# print('      py   '.lstrip())
# print('   py         '.rstrip())
# print('https://www.python.org'.lstrip('/:pths'))
# print('py.$$$;'.rstrip(";$."))
# print('https://www.python.org'.lstrip('/:pths').rstrip("org."))
# print('      py   '.strip())
# print("www.python.org".strip("org.w"))
# print('https://www.python.org/'.strip("/org.w:pths"))  # letter "p" is LOSS
# print('https://www.python.org'.lstrip('/:pths').rstrip("org."))
# print("     py     ".strip())
# print("https://www.python.org/".strip("/org.w:pths"))
#
# print("Более Интересные МЕТОДЫ Строк.")
# print(("str.replace('symbol or symbols", 'number_Of_Time_REPLACE'))
# s = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(s.replace("Nython", "Python"))  # Change old on New
# print(s.replace("N", "P"))
# print(s.replace("Nython", "Python", 2))  # Change old on New
#
# print("##### Transform Type Of DATA ##### Строки хорошо Взаимодейвсивуют Со СТРОКАМИ")
# print("str.split('element', 'max_split_number'")
# s = "-"  # STRING
# seq = ('a', 'b', 'c')  # LIST or ITERABLE DATA-TYPE
# print(s.join(seq))
#
# print("..".join(['1', '2']))
# #### print("..".join([1, 2]))  # ERROR
# print(":".join('Hello'))
# #
# print("Срока разделенная пробелами".split())
# print("Срока разделенная пробелами".split(" "))
# print("www.puthon.org".split("."))
# print("www.puthon.org".split(".", 1))
# print("www.puthon.org.ru".split(".", 1))
#
# print("Ввод Нескольких СТРОК: INPUT('-->').SPLIT()")
# print("a = input('--> ').split()")
# # print(a)
#
# # ### Task 3: ###
# print("Задача 3: Пользователь Вводит ФАМИЛИЮ, ИМЯ и ОТЧЕСТВО.\n \
#                   1) Приложение Должно Вывести ФАМИЛИЮ и ИНИЦИАЛЫ.")
# # # a = input("Enter FIO: ").split()
# #
# a = "Bashkirov Aleksey  Aleksandrovich".split()
# print("Variant 1. Task 3 Lesson 20")
# # a = input('-> ').split()
# print(a[0], a[1][:1] + '.' + a[2][:1] + '.')
# print("Variant 2. Task 3 Lesson 20")
# # # a = input('-> ').split()
# print(a[0], a[1][0]+'.', a[2][0]+'.')
#
# print("Continue LESSON:")
# print("www.puthon.org".split(".", 1))  #
# print("www.puthon.org".rsplit(".", 1))
#
#
# ### Task 4: ###
# print("Задача 4: Встроке Заменить ПРОБЕЛЫ Символом *.")
# print("Variant 1. Task 4 lesson 20.")
# str1 = " В строке заменить пробелы символом"
# print(str1.replace(" ", "*"))
#
# print("Variant 2. Task 4 Lesson 20")
# print('*'.join(str1.split(" ")))
#
# # str1 = " В строке заменить пробелы символом"
# # s = '*'.join((input('Введите строку: '.split())))
# # s = '*'.join(str1.split()))

################ REGULAR EXPRESSIONS #####################################
print("РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ Со Стороны Front-End:\n \
      1) Проверка ОПРЕДЕЛЕННЫХ ПОЛЕЙ - LOGIN, PASSWORD, ADDRESS - \n \
           - Отправка КОРРЕКТНЫХ ДАННЫХ на СЕРВЕР. \n"
      "РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ Со Стороны Back-End:\n \
            1) Для Проверки ФОРМ - Для Отслеживания Поступающих ДАННЫХ. \n \
            2) ВАЛИДАЦИЯ ДАННЫХ")
print("РЕГУЛЯРНЫЕ ВЫРАЖЕНЯ Могут Искать СОВПАДЕНИЯ Но НЕ ШАБЛОН.")

# print("str.find(str)")
# s = "Я ищу совпадения в 2021 году. И я их обязательно найду. 4546"
# reg = 'я'
# print(s.find(reg))
# print(reg in s)
#
# print("ОСНОВНЫЕ Методы РЕГУЛЯРНЫХ ВЫРАЖЕНИЙ. Return LIST Contain All math")
# print("Сначала Импортируем МОДУЛЬ re - МОДУЛЬ Регулярных Выражений.")
# import re

# print("Method FINDALL(pattern,str)")
# s = "Я ищу совпадения в 2021 году. И я их обязательно найду. 4546"
# print(s)
# reg = 'я'
# reg1 = 'совпадения'
# reg2 = "Я ищу"
# reg3 = "."
# reg4 = "\\."
# reg5 = r'\.'
# print(re.findall(reg, s))  # Return LIST Contain All math
# print(re.findall(reg1, s))  # Return LIST Contain All math
# print(re.findall(reg2, s))  # Return LIST Contain All math
# print(re.findall(reg3, s))  # Return LIST Contain All math
# print(re.findall(reg4, s))  # Return LIST Contain All math
# print(re.findall(reg5, s))  # Return LIST Contain All math
# print(re.findall('12', s))

# print("Method SEARCH(pattern, str): ")
# import re
# s = "Я ищу совпадения в 2021 году. И я их обязательно найду. 4546"
# reg = 'я'
# reg1 = 'совпадения'
# reg2 = "Я ищу"
# reg3 = "."
# reg4 = "\\."
# reg5 = r'\.'
# print(re.search(reg, s))  # Return 1 Found Math and Finit Work
# print(re.search(reg, s).span())  # Out Begin INDEX and Fine INDEX.
# print(re.search(reg1, s).span())   # Out Begin INDEX and Fine INDEX.
# print(re.search(reg1, s).start())  # Out Begin INDEX.
# print(re.search(reg1, s).end())  # Out Fine INDEX.
# print(re.search(reg1, s).group())  # Return find element
#
# print()
# print("Поиск По Заданному ШАБЛОНУ Относительно Начала Строки. MATCH()")
# import re
# s = "Я ищу совпадения в 2021 году. И я их обязательно найду. 4546"
# reg = 'я'
# reg1 = 'совпадения'
# reg2 = "Я ищу"
# reg3 = "."  # Special Simbol.
# reg4 = "\\."
# reg5 = r'\.'
# print(re.match(reg, s))
# print(re.match(reg1, s))
# print(re.match(reg2, s))
# print()
#
# print("METHOD RE.SPLIT(pattern, str)")
# print("Разбиение СТРОКИ По ШАБЛОНУ.")
# print(re.split(reg, s))
# print(re.split(reg, s,1))
# print(re.split(reg1, s, 1))
# print(re.split(reg2, s))
# print(re.split(reg3, s))
# print(re.split(reg4, s))
# print(re.split(reg5, s))
# print()
#
# print("RE.SUB(pattern, new_symbol, str)")
# print("Поиск и Замена Символа.")
# print(re.sub(reg, "!", s))
# print(re.sub(reg, "!", s, 1))
# print()

# print("REGULAR ESPRESSIONS")
# import re
# s = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. 4546"
# s1 = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счёта."
# reg = r'2021'
# reg1 = r'[201]'
# reg2 = r'[0-9]'
# reg3 = r'[12][0-9][0-9][0-9]'
# reg4 = r'[а-я]'
# reg5 = r'[а-яё]'
# reg6 = r'[АаЯ-яё]'
# print("s", s)
# print("s1", s1)
# print(re.findall(reg, s))  #[2021
# print(re.findall(reg, s1))  #[2021
# print(re.findall(reg1, s))
# print(re.findall(reg1, s1))
# print(re.findall(reg2, s))
# print(re.findall(reg2, s1))
# # # From 1900 - 2999
# print(re.findall(reg3, s))
# print(re.findall(reg3, s1))
# print(re.findall(reg4, s))
# print(re.findall(reg4, s1))
# print(re.findall(reg5, s))
# print(re.findall(reg5, s1))
# print(re.findall(reg6, s))
# print(re.findall(reg6, s1))
#
#
# s2= "Еда, беду, победа"
# reg7 = '[Ее]д[ау]'
# print(re.findall(reg7, s2))
#
# s1 = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счета."
# reg6 = r'[Аа-яё.]'
# print(re.findall(reg6, s1))
# s2 = "Ели[-ели]."
# reg7 = r'[А-Яа-яё.-]'
# print(re.findall(reg7, s2))
# reg8 = r'[А-Яа-яё.\[\]-]'
# print(re.findall(reg8, s2))
#
# reg9 = r'[^ 0-9]'
# print(re.findall(reg9, s1))
# reg10 = r'[1-2]'
# print(re.findall(reg10, s1))
#
# # ### Task 5 ### hour(00 - 23) minute(00 = 59)
# print("Задача 5: Найти время в Формате: [16:25]")
# str5 = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты в диапазоне от 00 до 59 2021-06-15T01:09."
# reg11 = r"[0-2][0-9]:[0-5][0-9]"  #"[12][0-9]:[0-5][0-9]"
# print(re.findall(reg11, str5))

import re
s1 = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счета."
reg = r'\.'
print(re.findall(reg, s1))

###### ABREVIATURE #######
s1 = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счета."
reg12 = r'\D'  # eny NAM
reg13 = r'\w'  # Nam, Lett
reg14 = r'\s'  # Space
reg15 = r'\D'  # NOT eny NAM
reg16 = r'\w'  # NOT Nam, Lett
reg17 = r'\s'  # NOT Space

print(re.findall(reg12, s1))
print(re.findall(reg13, s1))
print(re.findall(reg14, s1))
print(re.findall(reg15, s1))
print(re.findall(reg16, s1))
print(re.findall(reg17, s1))
print("# ##### \A \B \Z ##### \a \b \z #####")
s6 = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счета."
reg18 = r'\AЯ ищу'
reg19 = r"\AИ я их"
reg20 = r'счета.\Z'
reg21 = r'ния\b'
reg22 = r'\Bния'
print(re.findall(reg18, s6))
print(re.findall(reg19, s6))
print(re.findall(reg20, s6))
print(re.findall(reg21, s6))
print(re.findall(reg22, s6))