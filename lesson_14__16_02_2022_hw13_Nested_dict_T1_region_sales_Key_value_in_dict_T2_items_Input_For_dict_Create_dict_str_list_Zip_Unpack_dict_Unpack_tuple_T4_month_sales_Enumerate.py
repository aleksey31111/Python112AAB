# ### HW - 13 ################################################
### Term 1 ###
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'NewYork'}
# a = dict()
# a['name'] = d.pop('name')
# a['salary'] = d.pop('salary')
# print(d)
# print(a)
# print()
# print()
# ### Term 2 ###
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'NewYork'}
# d['location'] = d.pop('city')
# print(d)
########################################################################
# #### CONTINUE DICT # INDENT DICT #### 2FOR ####
# a = {
#     "first": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")

#### TERM 1 : REGION Of SELL ####
### SELF ATTEMPT ###
# names = {'name': ['John', 'Tom', 'Anne', 'Fiona']}
# sell = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anna': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# }
# print(names)
# # print(sell)
# for name in names:
#     print(name)
# for x in sell:
#     print(x)
#     for y in sell[x]:
#         print("\t", y, ": ", sell[x][y], sep="")
# manager_name = input("Введите имя менеджера... ")
# # while type(manager_name) != str and manager_name != 'John' or manager_name != 'Tom' or manager_name != 'Anna' or manager_name != 'Fiona':
# # try:
# #     manager_name = str(manager_name)
# #
# # except ValueError:
# #     print("Вы ввели Неверное Имя попробуйте еще раз.")
#         # manager_name = input("Введите имя менеджера... ")
# print(sell[manager_name])
#
# # for manager_name in sell:
# #     print(manager_name)
# #     for regin in sell[manager_name]:
# #         print("\t", regin,": ",sell[manager_name][regin])
# # try:
# #     regin = input("Введите Регион: ")
# #
# # except KeyError:
#
#     print("Вы ввели Неверный Регион попробуйте еще раз.")
# print(sell[manager_name][regin])
# sell_value = input("Введите значение на которое нужно изменить: ")
# sell[manager_name][regin] = sell_value
# print(sell[manager_name][regin])
# print(sell[manager_name])

# seles = {
#     'name': ['John', 'Tom', 'Anne', 'Fiona'],
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'N': 2451}
# }
# l = input('Введите имя продавца:')
# p = input('Введите регион: ')
#
# for i in sales:
#     print(i)
#     for y in sales[i]:
#         print("\t", y, ": ",a[i][y], sep="")

#### GENERATOE DICT   ############
# a = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# b = {key: value for key, value in a.items()}
# print(b)
# b = {value: key for key, value in a.items()}
# print(b)
# a = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# for i, j in a.items():
#     print(i, j)
# for i in a.keys():
#     print(i)
# for i in a.values():
#     print(i)
#####  Term 2: Вывести 2 ключ: значение  ##
# a = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# b = {key: value for key, value in a.items() if value <= 2}
# print(b)
#
# ##### GENERATOR DICT From LIST   ######
# a = {i: i * 5 for i in [10, 20, 30, 40]}
# print(a)
# s = [100, 200, 300, 400]
# a = {i: i * 5 for i in s}
# print(a)
# s = "hello"
# a = {i: i * 5 for i in s}
# print(a)
# #
# v = int(input("->"))
# s = [10, 20, 30, 40]
# a = {i: v * 5 for i in s}
# print(a)


##### TRANSFORM DICT In LIST ###
# figure = {1: 'Rectangle', 2: 'Triangle', 3: "Circle"}
#
# print(list(figure))
# print(list(figure.values()))
# print(list(figure.items()))
# ##### TRANSFORM DICT In TUPLE ###
# print(tuple(figure))
# print(tuple(figure.values()))
# print(tuple(figure.items()))

# ####### Term 3: Transform LIST In DICT (STRING - Key, int - TUPLE Values######
# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four, -20"]
# # lst = ["one", 1, 2, 3, "two", 10, 20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

######### ZIP ###### CREATE DICT From 2 list (equal lenght
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = dict(zip(a, b))
# print(d)
# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# f = {k: v for k, v in zip(b, a)}
# print(f)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# c = ('Mart', 'Aprile', 'May')
# d = (3, 4, 5)
# e = {'June', 'Jul', 'Aug'}
# f = {5, 6, 7}
# z = zip(a, b)
# y = zip(c, d)
# w = zip(e, f)
# print(z)
# print(type(z))
# print(list(z))
# print(tuple(y))
# print(set(w))
# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# c = [4.0, 5.0, 6.0]
# z = list(zip(a, b, c))
# print(z)
# z = dict(zip(a, b))
# print(z)
# print(list(zip(range(5), range(100))))  # Спиок кортежей с разными значениями
# print(list(zip(range(2, 15), range(100))))  # Спиок кортежей с разными значениями

#### Unpack DICT ###
# a = [1, 2, 3, 4, 5]
# b = ['a', 'b', 'c', 'd', 'e']
# for i in zip(a, b):
#     print(i, end=" ")
# print()
# a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# b = {'a': 11, 'b': 22, 'c': 33, 'd': 44, 'e': 55}
# for i in zip(a, b):
#     print(i, end=" ")
# print()
# for i in zip(a.items(), b.items()):
#     print(i, end=" ")
# print()
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, "-->", v1, end=" ")
#     print(k2, "-->", v2, end=" ")
# print()
#### Unpack TUPLE From Pairs ####
# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

#### Sort List From list(zip())
# a = ['b', 'c', 'a', 'd']
# b = [3, 2, 1, 4]
# data = list(zip(a, b))
# print(data.sort())
# print(data)
# data1 = list(zip(b, a))
# data1.sort()
# print(data1)
# data2 = sorted(zip(b, a))


##### Term 4 ###### Прибыль по месяцам
# month = ["January", "February", "March"]
# total_sales = [52000.00, 51000.00, 48000.00]
# production_cost = [46000.00, 45900.00, 43200.00]
# for sales, cost, m in (zip(total_sales, production_cost, month)):
#     res = sales - cost
#     print("Общая прибыль в", m, "=", res)

############ UNPUCK DICT ########
# one = {'apple': 0.04, 'orange': 0.35, 'a': 0.53, 'pepper': 0.53}
# two = {'pepper': 0.20, 'onion': 0.55}
# print({**two, **one})
# # print(dict(**two,**one))
# for k, v in {**two, **one}.items():
#     print(k, '->', v)
#

###################### ENUMERATE ################
# colors = ["red", 'green', 'blue']
# ind = 1
# for color in colors:
#     print(str(ind) + ") " + color)
#     ind += 1
# print()
# colors = ["red", 'green', 'blue']
# for i, color in enumerate(colors, 1):
#     print(str(i) + ") " + color)
# print()
# colors = ["red", 'green', 'blue']
# for color, i in enumerate(colors, 1):
#     print(i, ") ", color)

#
# d = {"a": 1, "b": 2, "c": 3, "d": 4}
# for i, j in enumerate(d, 5):
#     print(i, ": ", j, sep="")
# d = {"a": 1, "b": 2, "c": 3, "d": 4}
# for i, j in enumerate(d.values(), 5):
#     print(i, ": ", j, sep="")
# d = {"a": 1, "b": 2, "c": 3, "d": 4}
# for i, (j, q) in enumerate(d.items(), 5):
#     print(i, ": ", j, "\t->\t", q, sep="")
#
# #
# d = {"a": 1, "b": 2, "c": 3, "d": 4}
# for i, j in enumerate(d):
#     print(i, ": ", j, sep="")
#
# d = {
#     1: {"a": 1, "b": 2, "c": 3, "d": 4},
#     2: {"a": 10, "b": 20, "c": 30, "d": 40},
# }
# for i, k in enumerate(d, 1):
#     print(i, ") key=", k, ", value=", d[k], sep="")
#

######  ITER #######
# num = [1, 2, 3, 4, 5]
# itr = iter(num)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr, "STOP"))
# print(next(itr, "STOP"))
#
a = [6, 7, 3, 4, 1, 5]
b = enumerate(a)
print(b)
c = next(b)
print(c)
c = next(b)
print(c)
c1 = next(b)
print(c1)
#         print(c)
#         print(c1)
#         print(type(c))
