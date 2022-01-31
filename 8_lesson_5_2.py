### LESSON - 5.2 ###
## HOME WORK 24.01.2022##
#
# row = 0
# for row in lst:
#     for col in row:
#         print(col, end="\t")
#     print()
# print("----------------")
# i=0
# for row in row:
#     for row in lst:
#         print(row[i], end="\t")
#     i += 1
#     print()

## HOME WORK 3 ##
# import random as r
# b = int(input("Размер списка: "))
# a = list()
# #for i in range(50):
# # while len(a) != 10:
# while len(a) != 10:
#     # w = r.randint(0, 9)
#     w = r.randint(1, 9)
#     if w not in a:
#         a.extend([w])  # [5, 7]
# print(a)

### Continue MATRIX ###
#### - Создание Матрицы в одну строчку С ПОЯСНЕНИЕМ ####
# import random as r
#
# w, h = 5, 4
# mat = list()
# for y in range(h):
#     m = list()
#     for x in range(w):
#         m.append(r.randint(1, 30))
#     mat.extend([m])
# print(mat)
#
# matrix = [[r.randint(1, 30) for x in range(w)] for y in range(h)]
# print(matrix)
#
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()

#### TERM 1 ####
##### Создать Матрицу 3 на 4. В диапазоне от -20 до 10. #####
##### И вывести количество ОТРМЦАТЕЛЬНЫХ ЭЛЕМЕНТОВ #####
# import random as r
#
# w, h = 3, 4
# mat = [[r.randint(-20, 10) for x in range(w)] for y in range(h)]
# c = 0
# for row in mat:
#     for col in row:
#         if col < 0:
#             c += 1
#         print(col, end="\t\t")
#     print()
# print("Количество отрицательных Элементов: %d" % c)

#### TERM 2 ####
##### СЛУЧАЙНАЯ МАТРИЦА РАЗМЕРОМ 3 НА 4, Цифрами лт 0 до 4. #####
##### Найти произведение Не Нулевых элементов списка #####
# import random as r
#
# w, h = 3, 4
# matrix = [[r.randint(0, 4) for x in range(w)] for y in range(h)]
# c = 1
# for row in matrix:
#     for col in row:
#         if col > 0:
#             c *= col
#         print(col, end='\t\t')
#     print()
# print("Произведение ненулевых элементов: {0}".format(c))

#### TERM 3 ####
##### СЛУЧАЙНАЯ МАТРИЦА РАЗМЕРОМ 3 НА 4, Цифрами лт 0 до 10. #####
##### Поменять местами 1-ю и 2-ю строки, 3-ю и 4-ю строки, 5-ю и 6-ю строки Матрицы. #####
# import random as r
#
# w, h = 6, 6
# matrix = [[r.randint(0, 10) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for col in row:
#         print(col, end='\t\t')
#     print()
# print()
# #
# for row in range(len(matrix)):
#     if row % 2 == 0:
#         row = matrix[row + 1]
#     else:
#         row = matrix[row - 1]
#     for col in row:
#         print(col, end='\t')
#     print()
####place_move = [[print(col, end='\t') for col in row] for row in range(len(matrix)) if row % 2: row = matrix[row + 1]  else: row = matrix[row - 1] ]
###### term 3 - Вариант ПРЕПОДАВАТЕЛЯ ####
# import random as r
#
# w, h = 6, 6
# matrix = [[r.randint(0, 10) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for col in row:
#         print(col, end='\t\t')
#     print()
# print()
# for h in range(len(matrix)):
#     if h % 2 == 0:
#         for w in range(len(matrix[h])):
#             print(matrix[h + 1][w], end='\t\t')
#         print()
#         for w in range(len(matrix[h])):
#             print(matrix[h][w], end='\t\t')
#         print()
# print()

##############################   16 - ПАРА   ##############################################
##### ВЫВОДИЛИСЬ РАБОЧИЕ ДНИ НЕДЕЛИ ######
# 1 2 3 4 5
# 8 9 10 11 12
# 15 16 17 18 19
# 22 23 24 25 26
# 29 30 31
# days = [d for d in range(1, 32)]
# print(days)
# print(len(days))
# weeks = [days[dw:dw + 7] for dw in range(0, len(days), 7)]
# print("7 дней в неделе: ", weeks)
# for row in weeks:
#     for x in row:
#         print(x, end="\t\t")
#     print()
# work_days_weeks = [days[i:i + 5] for i in range(0, len(days), 7)]
# print("Рабочие дни недели: ", work_days_weeks)
# for row in work_days_weeks:
#     for x in row:
#         print(x, end="\t\t")
#     print()
### TERM CICRCLE ###
# from math import pi, sqrt, hypot, fsum, degrees, radians, cos, sin
#
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности: ", round(2 * pi * radius, 2))
#
# lst = [1,5,3,8.4]
# print(sum(lst))
# print(fsum(lst))
#
# print(degrees(3.14159))
# print(radians(180))
#
# print(cos(radians(60)))
# print(sin(radians(60)))

# ### TERM KATET ###
# from math import sqrt, hypot
#
# kat1 = int(input("Катет 1: "))
# kat2 = int(input("Катет 2: "))
# gip = round(hypot(kat1, kat2), 2)
# gipotenuza = round(sqrt((kat1 ** 2) + (kat2 ** 2)), 2)
# gip
# print("Гипотенуза равна: ", gipotenuza)
# print("Гипотенуза равна: ", gip)

################## МОДУЛЬ TIME ####################
from time import time, ctime, localtime, strftime, sleep

seconds = time()
print(seconds)
local_time = ctime(seconds)
print(local_time)
res = localtime(seconds)
print(res)
print(res.tm_hour)
print(strftime("Today is %B %b, %Y", localtime()))
print(strftime("%m/%d/%Y, %H:%M:%S"))

pause = 5
print("Program started...")
sleep(pause)
print(pause, "seconds.")

text = input("Название напоминания: ")
t = float(input("Через сколько минут: "))
t *= 60
sleep(t)
print(text)