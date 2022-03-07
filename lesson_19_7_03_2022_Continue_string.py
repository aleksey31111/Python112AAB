### LESSON 19 ###
#### CONTINUE String ####
##### Prefix #####
###### r - for String
# print('I\'m learning\nPython')
# print('C:\\file.txt')
# print(r'C:\file')
# #### print(r'C:\file\') print(r'C:\file\\')  ERROR
# print(r'C:\file\\'[:-1])
# print(r'C:\file"+"\\')
# print('C:\\file\\')

###### b(B) - Byte format


# ###### f(F) - String
# name = "Дмитрий"
# age = 25
# print("Иеня зовут", name, ". Мне", age, "лет.", sep="")
# print("Иеня зовут" + name + ". Мне" + age + "лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")
#
# ####  Insert MODULE ####
# import math as m
#
# print(f"Значение числа pi: {m.pi:.2f}")
# x=13
# y =3
# print(f"13/3 = {round(13 / 3, 2)}")
# print(f"{x}/{y} = {round({x} / {y}, 2)}")
#
# a= [1,2,3,4,5,6]
# print(f"Second ELEMENT Of List {a[3] * 2}")
#
#
# ###### Many String Format ######
# name = "frend"
# prof="programmer"
# lang = "Python"
#
# message = (
#     f"Hello {name}."
#     f"You are {prof}."
#     f"On language {lang}."
# )
# print(message)
#
# a=74
# print(f"{{74}}")
# print(f"{{{{{74}}}}}")
#
# print(f"{{74}}")
#
# #### fr - literal format and not format string.
# d = "my_doc"
# f="data.txt"
# print(fr"home\{d}\{f}")

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
# "Hello1"
# s1 = "Hello"
# print(s)


### DESCRIPTION DOCUMENTAITION FUNCTION. ###
# def square(n):
#     """Принимает число n, Возврашает число n"""  # First POSITION For DOCUMENTAION.
#
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)

# ### CONTINUE ###
# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет Площадь ЦИЛИНДРА.
#
#     Вычисляет площадь ЦИЛИНДРА На основании его Высоты и Радиуса основания.
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
#
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# my_str = "Test string for me"
# # my_str = "学习"
# arr = [ord(x) for x in my_str]
# print("ASCII коды", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("AVERAGE: ", arr)
# arr += [x for x in [ord(x) for x in (input("-> ") + " "[:3])] if x not in arr]
# print(arr)
# if arr[-1] in arr[-1]:
#     print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


#### FUNCTION CHR ####
# print(chr(97))
# print(chr(40))
# print(chr(21731))


### Task 3 ###
# a=122
# b=97
# str1 = ""
# for x in range(chr(97),chr(122)):
#     print(x,end=" ")

# a = 97
# b = 122
# str1 = ''
# for x in range(b, a + 1):
#     str += (chr(x) + ' ')
# print(str)

# a = 122
# b = 97
# for x in range(b, a + 1):
#     print(chr(x), end=" ")


# a = 97
# b = 122
#
# if a > b:
#     for x in range(b, a + 1):
#         print(chr(x), end=" ")
# else:
#     for x in range(a, b + 1):
#         print(chr(x), end=" ")


#### COMPARE STRING ####
# print("apple" == "Apple")
# print("apple" > "Apple") # 97 > 65


# #### RANDOM PASSWORD ####
# from random import randint
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)  # гЕНЕРИРУЕМ сЛУЧАЙНУЮ длинну пароля.
#     res = ""
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res = res + random_char
#     return res
#
# print(random_password())
# print(random_password())
# print(random_password())
# print(random_password())

#### STRING METHOD ####
# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Return First leter CAPITAL.
# print(s.lower())  # all string in ow registr.
# print(s.upper())  # UP registr.
# print(s.swapcase())  # reverse registre
# print(s.title())  # Every world in string UP Letter.
#
#
# print(s.count("h"))  # Number Of GET ELEMENT.
# print(s.count("h",1))  # Number Of GET ELEMENT. from 1 element
# print(s.count("h",0,-4))  # Number Of GET ELEMENT. in reverse ORDER
# print(s.find("Python"))  # Return INDEX FIRST NESTED SUBSTRING

# ### TASK 5 ###
# # a = "hello"
# # b="Hi"
# # print(a,b)
# # for x, y in a,b:
# #     print(y,x)
#
# s = 'one two'
# s2 = s[s.find(' ') +1:] + ' ' + s[:s.find(' ')]
# print s2

#### Task 6 ####
# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if 48 < ord(i) < 58:
#         digits += i
# print(digits)


# s='ab12c59p7dq'
# str1=""
# for x in s:
#     if type(x)!=int:
#         str1 += x
#         print(str1, end=" ")


# s='ab12c59p7dq'
# digits = []
# for i in s:
#     if '0123456789'.find(i) != -1:
#         digits.append(int(i))
# print(digits)


#### Continue Lesson
s = "hello, WORLD! I am learning Python."
s.find("cPython") # if Not found Return -1
s.index("cPython")  # if Not found Return ValueError


#### Task 6