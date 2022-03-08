# ### LESSON 19 ###
# #### CONTINUE String ####
# ##### Prefix s, f - More often Use #####
# ### Prefix u ### - Output UNICODE = Inheritance before Version Of Python e.g. Python 2
# print(u'Hello')
# print(u'Привет')
# print(u"Hello")
# print(u"Привет")
# ###### r(R) - for String - Sappres CHARACTER Escaping/
# print(r'Hello')
# print(r'Привет')
# print('I\'m learning\nPython')
# print(r'I\'m learning\nPython')
# print('C:\\file.txt')
# print(r'C:\file.txt')
# # #### print(r'C:\file\') print(r'C:\file\\')  ERROR
# print(r'C:\file\\')
# print(r'C:\file\\'[:-1])
# print(r'C:\file'+"\\")
# print('C:\\file\\')

###### b(B) - Byte format - Mode Save FILE


# ###### f(F) - String With VARIABLE In {}
# name = "Дмитрий"
# age = 25
# print("Иеня зовут ", name, ". Мне ", age, " лет.", sep="")
# print("Иеня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")

# ####  Insert MODULE ####
# import math as m
#
# print(f"Значение числа pi: {m.pi:.2f}")
# x = 13
# y = 3
# print(f"13/3 = {round(13 / 3, 2)}")
# print(f"{x}/{y} = {round({x} / {y}, 2)}")

# a = [1, 2, 3, 4, 5, 6]
# print(f"Forth ELEMENT Of List {a[3] * 2}")

# ###### Many String Format ######
# name = "frend"
# prof = "programmer"
# lang = "Python"
#
# message1 = f"Hello {name}. ", f"You are {prof}. ", f"On the language {lang}."
# message2 = (
#     f"Hello {name}. "
#     f"You are {prof}. "
#     f"On the language {lang}."
# )
# print(message1)
# print(message2)
#
# a = 74
# print(f"{a}")
# print(f"{{a}}")
# print(f"{{{a}}}")
# print(f"{{{{a}}}}")
# print(f"{{{{{a}}}}}")
# print(f"{{{{{{a}}}}}}")
# print(f"{{{{{{{a}}}}}}}")
#
# print(f"{{74}}")
#
# # #### fr - literal format and not format string.
# d = "my_doc"
# f = "data.txt"
# print(fr"home\{d}\{f}")
# print(r"home\{d}\{f}")
# print(f"home\\{d}\\{f}")
# print("home\\" + d + "\\" + f + d)


# ############## """ """, ''' ''' = FORMAT TEXT.
# s1 = '''
# Many String COMMENT.
# <div>
#     <a href="#">content</a>
# </div
# '''
# s2 = """
# Many String COMMENT.
# <div>
#     <a href="#">content</a>
# </div
# """
# print(s1)
# print(s2)
# "Hello"
# s1 = "Hello"
# print(s1)


### DESCRIPTION DOCUMENTAITION FUNCTION. ###
# def square(n):
#     """Принимает число n, Возврашает число n"""  # First POSITION For DOCUMENTAION.
#
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)


### EXTENDED Documentation EXAMPLE. ### Press ENTER betwin "TRIPLE Quotes"
# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет Площадь ЦИЛИНДРА.
#
#     Вычисляет площадь ЦИЛИНДРА На Основании заданной Высоты и Радиуса основания.
#     :param r: положительное число, РАДИУС основания цилиндра
#     :param h: положительное число, ВЫСОТА основания цилиндра
#     :return: положительное число, ПЛОЩАДЬ основания цилиндра
#     """
#     return 2 * math.pi * r * (r * h)
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


### String VALUE ###
# a = "Hello"
# b = 'Hello'
# c = """Hello"""
# d = '''Hello'''
# print(f"{a} {b} {c} {d}")


### Builting METHOD ###
# print(len('1111'))
# print(ord('a'))
# print(ord('#'))
# print(ord('г'))

#### Output ASCII - code of SIMBOL.
## ord(char) - ASCII Code for CHARACTER.
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# print(
#     "Task 1 with Teacher: Дана СТРОКА 'Test string for me', \n"
#     f"1) Сформировать список Содержащий ASCII коды символов Этой строки.\n"
#     f"2) Вычислить СРЕДНЕЕ АРИФМЕТИЧЕСКОЕ Полученных КОДОВ, и Дописать его в Начало списка.\n"
#     "3) Спросить у Пользователя еще 3 символа. Получить их ASCII коды.\n"
#     "4) Проверить Наличие Этих КОДОВ в списке, и Если Их нет Дописать в Коней СПИСКА.\n"
#     "5) Определить есть ли В Списке Элементы Равные ПОСЛЕДНЕМУ, Если ДА, Определить Сколько ИХ.\n"
#     "6) Отсортировать СПИСОК По Убыванию.\n"
# )
#
# my_str = "Test string for me"
# # my_str = "学习"
# arr = [ord(x) for x in my_str]
# print("ASCII коды СТРОКИ: 'Test string for me' = ", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("AVERAGE СТРОКИ: 'Test string for me' в начало списка ASCII кодов: ", arr)
# # # arr += [x for x in [ord(x) for x in (input("-> " + " "）[:3])] if x not in arr]
# # # print(arr)
# # arr += [x for x in [ord(x) for x in (input("--> ") + " "[:3])] if x not in arr]
# # print(arr)
# if arr[-1] in arr[:-1]:
#     print(arr.count(arr[-1]) - 1)
#
# # arr.sort(reverse=True)
# # print(arr)
# arr.sort(reverse=True)
# print(arr)

#### FUNCTION CHR ####
# print(chr(97))
# print(chr(40))
# print(chr(21731))
# print(chr(540))

### Task 2:  ###
# print("Задание 2: Даны два ЧИСЛА a=122, b=97, где a, b коды символов,"
#       "Вывести все СИМВОЛЫ ASCII коды которых между a и b.")
# a = 122
# b = 97
# str1 = ""
# for x in range(b, a + 1):
#     print(chr(x), end=" ")
# print("\n")
#
# a = 97
# b = 122
# str1 = ''
# for x in range(a, b + 1):
#     str1 += str(chr(x) + ' ')
# print(str1)
#
# print("\n")
# a = 122
# b = 97
# for x in range(b, a + 1):
#     print(chr(x), end=" ")
# print("\n")
#
# a = 122
# b = 97
#
# if a > b:
#     for x in range(b, a + 1):
#         print(chr(x), end=" ")
# else:
#     for x in range(a, b + 1):
#         print(chr(x), end=" ")


# #### COMPARE STRING ####
# print("apple" == "Apple")
# print("apple" > "Apple") # 97 > 65


# # #### Generate RANDOM PASSWORD ####
# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)  # Генерирует Случайную ДЛИННУ ПАРОЛЯ.
#     res = ""
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print(random_password())
# print(random_password())
# print(random_password())
# print(random_password())

#### STRING METHOD #### Python Console --> dir(str)
# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Return First leter CAPITAL.
# print(s.lower())  # all string in ow registr.
# print(s.upper())  # UP registr.
# print(s.swapcase())  # reverse registre
# print(s.title())  # Every world in string UP Letter.

# s = "hello, WORLD! I am learning Python."
# print(s.count("h"))  # Number Of GET ELEMENT.
# print(s.count("h", 1))  # Number Of GET ELEMENT. from 1 element
# print(s.count("h", 0, -4))  # Number Of GET ELEMENT. in reverse ORDER
# print(s.find("Python"))  # Return INDEX FIRST NESTED SUBSTRING

### TASK 3 ###
# print("Задание 3: Строка из 2 СЛОВб Разделленных ПРОБЕЛОМ,\n"
#       "\t Переставьте СЛОВА Местами.\n"
#       "\t Результат Запишите в СТРОКУ и Выведите получившуюся СТРОКУ.\n")
# a = "hello"
# b = "Hi"
# print(a, b)
# ### for (x, y) in a, b:  Too many Values To UNPUCK (expected 2)
# ###     print(y, x)
#
# s = 'one two'
# s2 = s[s.find(' '):] + ' ' + s[:s.find(' ')]  # First Place SPACE.
# s3 = s[s.find(' ') + 1:] + ' ' + s[:s.find(' ')]
# print(f"Source STRING: {s}")
# print(s2)
# print(s3)

#### Task 4:  ####
# print("Задание 4: Дано: s = 'ab12c59p7dq'\n"
#       "Надо: Извлечь ЦИФРЫ в СПИСОК digit, чтобы стало так:\n"
#       "digit == [1, 2, 5, 9, 7]\n")
# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or \
#             i == 6 or i == 7 or i == 8 or i == 9 or i == 0:
#         digits += i
# print(digits)
#
# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if 48 < ord(i) < 58:
#         digits += i
# print(digits)
#
##### NOTHING Print #########
# s = 'ab12c59p7dq'         #
# str1 = ""                 #
# for x in s:               #
#     if type(x) == int:    #
#         str1 += str(x)    #
# print(str1, end=" ")      #
#############################
# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if '0123456789'.find(i) != -1:
#         digits.append(int(i))
# print(digits)

#### Continue Lesson METHOD index
# s = "hello, WORLD! I am learning Python."
# print(s.find("cPython")) # if Not found Return -1
# print(s.find("Python"))
# # s.index("cPython")  # if Not found Return ValueError
# print(s.index("Python"))

#### Task 5 ####
print("Задание 5: Дана СТРОКА СИМВОЛОВ, где Есть ОДНА ОТКР и ЗАКР СКОБКИ."
      "Вывести СИМВОЛЫ Расположенные Внутри этих СКОБОК.")
str2="Дана ст(рока символов, среди которых есть одна открыв)ающаяся"
# if a > b:
#     for x in range(b, a + 1):
#         print(chr(x), end=" ")
# else:
#     for x in range(a, b + 1):
#         print(chr(x), end=" ")
# s3 = str2[str2.find('(') + 1:] + ' ' + str2[:str2.find(')')]
s3 = str2[str2.find('(') + 1:str2.find(')')]
print(s3)