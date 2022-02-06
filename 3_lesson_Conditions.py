# voron = int(input("Input voron: "))
# if voron == 1:
#    print(voron,"Ворона")
# elif voron == 2 or 3 or 4:
#     print(voron,"вороны")
# elif voron == 0 or 5 or 6 or 7 or 8 or 9:
#     print(voron,"ворон")
# else:
#     print("ошибка ввода данных")

# (Condition) ? TRUE : FALSE -JS
# a, b = 10, 20
# minim = a if a < b else b
# print(minim)
# a, b = 30, 20
# minim = a if a < b else b
# print(minim)
# a, b = 30, 30
#
# print( "a == b" if a == b else "a > b" if a > b else "b >a")
#     # "a == b" " a > b " " b> a"

# На 0 делить нельзя: тернарный оператор

# ОТЛАВЛИВАНИЕ ОШИБОК try except
# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except:
#     print("ЧТО ТО ПОШЛО НЕ ТАК")
# print("Код дальше")
#
# try:
#     n = int(input("Введите целое число: "))
#     m = int(input("Введите целое число: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Value must be number")
#     print("Zerro not divition")
# print("Код дальше")
#
# try:
#     n = int(input("Введите целое число: "))
#     m = int(input("Введите целое число: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Value must be number")
#     print("Zerro not divition")
# else:
#      print("All Ok, you are Input number", n, "and", m)
# finally:
#     print("End the program")
#
# a = input("Input Namber")
# b = input("Input Number")
# try:
#     a=int(a)
#     b=int(b)
# except (TypeError, ValueError):
#     # pass
#     a = str(a)
#     # b = str(b)
# finally:
#     print(a + b)

############CICLE###################
# j = 0
# while j < 5:
#     print("i =", j)
#     j += 1
#
# j = 10
# while j > 5:
#     print("i =", j)
#     j -= 1
#
# i = 0
# while i < 20:
#     i += 1
#     if i % 2 == 0:
#         print(i)
#
# i = 13
# while i <20:
#     i += 1
#     if i%2 == 0:
#         print(i)

# n = int(input("Input namber of star"))
# i = 0
# while n > 0:
#     print("*",end="")
#     n -= 1
# # print(z*'*')


a = int(input("start Range"))
b = int(input("End Range"))
s = 0
while a <= b:
    if a % 2 != 0:
        s += a
    a += 1
print(s)
