# ### 7 LESSON ###
# import random as r
# # from random import choice as r
# # from random import *
# city_list = ['Москва', 'Новосибирск', 'Воронеж','Сочи', 'Екатеринбург']
# print(r.choice(city_list))
# # choice -Возвращает случайное значение из списка
# #print(r.randint) # Возвращает случайное целое число
#
# s3 = [20, 30, 40, 50, 60, 70, 80, 90]
# print(r.choices(s3))
# print(r.choices(s3, k = 3))
# print(r.choices(s3, k = 5))
#
# r.shuffle(s3)
# print(s3)
#
# print(r.uniform(10.5, 25.5)) # случайное вещественное число
# print(round(r.uniform(10.5, 25.5), 2)) # случайное вещественное число
#
# ### ГЕНЕРАЦИЯ СЛУЧАЙНЫХ ЧИСЕЛ №№№
# mas1 = [i for i in range(10)]
# print(mas1)
#
# mas1 = [r.randint(0, 10) for i in range(10)]
#
# mas1 = [r.randrange(0, 10) for i in range(10)]
#
# ###  Функция АГРЕГИРОВАНИЯ №№№
# lst = [5, 3, 2, 4, 1]
# print(len(lst)) # - с разными типами данных
# print(min(lst)) # -  с разными типами данных
# print(max(lst)) # - с разными типами данных
# print(sum(lst)) # - с числами
#
# # sum = [5, 3, 2, 4, 1] # - ошибка
# print(min(sum))
# # print(sun(sum)) # - ошибка

# import random as r
# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)
# maximal = max(mas)
# mas.remove(maximal)
# print(mas)
# mas.insert(0, maximal)
# print(mas)

# import random as r
# mas = [r.randint(-20, 20) for i in range(10)]
# mas.sort(reverse=True)

# import random as r
# mas = [r.randint(-20, -10) for i in range(10)]
# min(mas)
# for i in index(len(0), min)):
#     min.remove(i)

############################################################################## INCORRECT
# from random import randint  # Задание произвольного массива
# n = [randint(0, 100) for i in range(10)]
# print(n)
# c = min(n)
# s=0
# for i in range(len(n)):
#     if n[i]==c:
#         s=i
# print(c)
# print(s)
# for i in range(len(n)):
#     if i<s:
#         n.remove(n[i])
# print(n)
########################################################################## INCORRECT


### TERM ###
# from random import randint  # Задание произвольного массива
# n = [randint(0, 100) for i in range(10)]
# print(n)
# c = min(n)
# print(c)
# s = n.index(c)
# print(s)
# # del n[0:s]
# # print(n)
# print(n[s:])

###
# x = list('1a2b3')
# print(x)
# print('a' in x)
# print('e' in x)
# print()
# print('a' not in x)
# print('e' not in x)

###  Порверка пустоно списка ###
# lst = []
# if len(lst) == 0:
#     print("Список пустой")
# if not lst:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")
import random as r

n1 = 5
n2 = 4
a = [r.randint(0, 10) for i in range(n1)]
b = [r.randint(0, 20) for j in range(n2)]
print("Первый список: ", a)
print("Второй список: ", b)
c = a + b
print("Третий список: ", c)
c = list()
for i in range(len(a)):
    if a[i] not in c:
        c.append(a[i])
for i in range(len(b)):
    if b[i] not in c:
        c.append(b[i])
print("Элементы общие обоих списков без повторений: ", c)

################################### ERROR
# from random import randint  # Задание произвольного массива
# a = [randint(0, 10) for i in range(5)]
# b= [randint(0, 10) for i in range(4)]
# print(a)
# print(b)
# c = a+b
# print(c)
# f=0
# d=[]
# e=[]
# for i in range(len(c)):
#     f=c[i]
#     k=0
#     for j in c:
#         if f == j:
#             k+=1
#     if k==1:
#         d.append(c[i])
#     else:
#         e.append(c[i])
# print(d)
# print(e)
############################## ERROR


### Element common for duo list

# import random as r
# n1 = 5
# n2 = 4
# a = [r.randint(0, 10) for i in range(n1)]
# b = [r.randint(0, 20) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
# c = list()
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы щбоих списков без повторений: ",c)

# list4=[]
# for elem in list3:
#     if list3.count(elem) != 1 and elem not in list4:
#         list4.append(elem)
#     if list3.count(elem) == 1:
#         list4.append(elem)
# print(list4)

# list5=[]
# for elem in list:
#     if elem in list2 and elem not in list5:
#         list5.append(elem)
# print(list5)

### MIN MAX FOR FUO LIST ###


# m = [
#     [1, 2, 3, 4, 7, 9],
#     [5, 6, 7, 8, 2],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(m[1][2]) # 7
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     for col in row:
#         print(col, end="\t\t")
#     print()
import random as r

# m = [[1, 2, 3, 4, 7, 9], [5, 6, 7, 8, 2], [9, 10, 11, 12]]
# print(m)
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col]**2, end="\t\t")
#     print()
# print()

# matrix = [[1, 2, 3, 4, 7, 9], [5, 6, 7, 8, 2], [9, 10, 11, 12]]
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(col**2, end="\t\t")
#     print()
# print()
# squared =  [[col ** 2 for col in row] for row in matrix]
#     for row in squared:
#         for col in row:
#             print(col, end="\t\t")
#         print()

# w, h = 5, 3
# squared =  [[0 for col in range(w)] for row in range(h)]
# for row in squared:
#     for col in row:
#         print(col, end="\t\t")
#     print()


# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

### матрица четные - по убыванию, не четные - по возрастанию ###
mas = [[2, 5, 8], [5, 8, 2], [8, 7, 1], [0, 7, 1], [9, 11, 6]]
for row in mas:
    for col in row:
        print(col, end="\t")
    print()
print()
for i in range(len(mas)):
    if i % 2 == 0:
        mas[i].sort(reverse=True)
    else:
        mas[i].sort()
print()
for row in mas:
    for col in row:
        print(col, end="\t")
    print()
