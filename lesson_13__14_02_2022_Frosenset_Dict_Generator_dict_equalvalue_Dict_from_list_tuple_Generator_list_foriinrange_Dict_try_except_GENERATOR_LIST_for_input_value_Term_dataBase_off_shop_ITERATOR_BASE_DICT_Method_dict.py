# ############## LESSON 14 ##############
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# a = frozenset({"hello", "world"})
# print(a)
# print("##### GENERATOR FROSENSET #####")
# b = frozenset({i ** 2 % 4 for i in range(10)})
# print(b)
# print(len(b))
# print()
# print()
# print()
############ DICT - СЛОВАРЬ №№№№№№№№№№№№№№№№№
# ls = ["Один", "Два"]
# print(ls[0])
# d = {"one": "Один", "two": "Два", 1: True}  # "gfgre"}
# print(d["one"])
# print(d)
# print(type(d))
# d = {"one": "Один", "two": "Два"}
# print(d)
# print(type(d))
#
# d1 = dict(one="Один", two="Два")
# print(d1)
# print(type(d1))

####### GENERATOR DICT #################
# d3 = dict.fromkeys(['a', 'b'], 100)
# print(d3)

########### DICT from LIST, TUPLE ######
# users = [
#     ['igor@gmail.com', 'Igor']
#     ['anna@gmail.com', 'Anna']
#     ['irina@gmail.com', 'Irina']
# ]
# print(users)
# d_users = dict(users)
# print(d_users)

# users = (
#     ('igor@gmail.com', "Igor")
#     ('anna@gmail.com', "Anna")
#     ('irina@gmail.com', "Irina")
# )
# print(users)
# d_users = dict(users)
# print(d_users)
#
# users = (("a", "b"),)
# print(users)
# d_users = dict(users)
# print(d_users)

######### GENERATOR DICT ###########
# d4 = {i: i ** 2 for i in range(7)}
# print(d4)
# print(d4[5])
# d4[5] = 50
# print(d4)

# d5 = {0: "text1", "one": 45, (1, 2, 3): 'кортеж', 42: [2, 3, 6, 7], True: 1}
# print(d5)
# print(d5[42])
# print(d5[42][1])
# print(d5[(1, 2, 3)])
# print(d5[1, 2, 3])
# # del d5[(1,2,3)]
# del d5[1, 2, 3]
# print(d5)
# print("one" in d5)
# print("teo" in d5)
#
# if 'one' in d5:
#     print("TRUE")
# if 'one' in d5.keys():
#     print("TRUE")

# d5 = {0: "text1", "one": 45, (1, 2, 3): 'кортеж', 42: [2, 3, 6, 7], True: 1}
# key = "four"
# if key in d5:
#     del d5[key]
# print(d5)


##### TRY - EXCEPT ######
# d5 = {0: "text1", "one": 45, (1, 2, 3): 'кортеж', 42: [2, 3, 6, 7], True: 1}
# key = "ONE1"
# # if key in d5:
# #     del d5[key]
# try:
#     del d5[key]
# except KeyError:
# print(d5)


# d6 = {'one':1,'two':2, 'three':3}
# for key in d6:
#     print(key, "-->", d6[key])

############ TERM 1 ##################
# digit_dict = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# s =1
# for key in digit_dict:
#     s *= digit_dict[key]
# print(s)


######### TERM 2 GENERATOR LIST for Input Value ################## GENERATOR DICT
# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# print(d)
#
# d1 = {i: input("->") for i in range(1, 5)}
# print(d1)

############# TERM 3 GENERATOR LIST for Input Value ##########
# d1 = {i: input("->") for i in range(1, 5)}
# print(d1)
# dislike = int(input("Какой элемент исключить:"))
# del d1[dislike]
# print(d1)


#####Term DataBase Of SHOP #######
# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670', 3, 8500],
#     '3': ['AMD FC-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i3-3450', 5, 6400]
# }
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
# while True:
#     n = input("№: ")
#     if n != "0":
#         q = int(input("Количество: "))
#         goods[n][1] = q
#     else:
#         break
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")


#####ITERATOR BASE DICT ###########
# d = {"A": 1, "B": 2, "C": 3}
# x = iter(d)
# print(x)
# print(list(x))


############ METHOD Of DICT #############
# d = {"A": 1, "B": 2, "C": 3}
# # d.clear() # - Удаляет все элементы Из словаря
# # d2 = d # один и тот же адрес
# d2 = d.copy() # Копирует словарь
# print("D =", d)
# print("D2 =", d2)
# d2["B"] = 5
# d["E"] = 7
# print("D =", d)
# print("D2 =", d2)

# d = {"A": 1, "B": 2, "C": 3}
# value = d.get("B") # По значению получаем ключ, Если значения НЕТ Получаем None
# value = d.get("E") # По значению получаем ключ, Если значения НЕТ Получаем None
# value = d.get("E", "FF") # По значению получаем ключ, Если значения НЕТ Получаем None
# print(value)
# print(d)

# d = {"A": 1, "B": 2, "C": 3}
# new = d.items() # Получаем ключи и Значения
# print(new)
# new1 = dict.items(d) # Получаем ключи и Значения
# print(new1)

# d = {"A": 1, "B": 2, "C": 3}
# a = d.keys() #  Доступ по ключам
# print(a)

# d = {"A": 1, "B": 2, "C": 3}
# items = d.pop("B")  # Удаление по Ключу, Возвращает Значение
# print(items)
# item = d.pop("B", 10)  # Удаление по Ключу, Возвращает Значение
# print(item)
# items = d.pop("E", 10)  # Удаление по Ключу, Возвращает Значение
# print(items)
# print(d)

# d = {"A": 1, "B": 2, "C": 3}
# item = d.popitem()
# print(item)
# print(d)
#
# d = {"A": 1, "B": 2, "C": 3}
# item = d.setdefault("E", 5) # Добавляет элемент по умолчанию.
# print(item)
# print(d)

# d = {"A": 1, "B": 2, "C": 3}
# d.update([('A', 7),('R', 7), ('Q',0)])
# print(d)

###### Term ########
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# c = {'b': 5}
# # z = x.copy()
# # z.update(y)
# z =x|y
# print(z)
# print(c)

d = {"A": 1, "B": 2, "C": 3}
v = d.values()