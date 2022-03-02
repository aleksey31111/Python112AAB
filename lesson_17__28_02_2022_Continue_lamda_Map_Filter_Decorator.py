# ### HomeWork 16 ###
# players = [{'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}]
# print(players)
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
#
# res = sorted(players, key=lambda item: item['last name'], reverse=True)
# print(res)

### LESSON 17 ### Continue: ### Associate DICT and LIST Via " lambda " Function.
# a = {'one': lambda x: x - 1, "two": lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# example = {"one": 12, "two": 13, "three": 14, "four": 15}
# print(example["one"], example["two"])

### Day of Week: ### Call lambda Function ###
# d = {
#     1: lambda: print('Monday'),
#     2: lambda: print('Tuesday'),
#     3: lambda: print('Wednesday'),
#     4: lambda: print('Thursday'),
#     5: lambda: print('Friday'),
#     6: lambda: print('Saturday'),
#     7: lambda: print('Sunday')
# }
# d[1]()
# d[2]()
# d[3]()
# d[4]()
# d[5]()
# d[5]()
# d[7]()


### Task 1 :  Square Circle, Rect, Trapezium Via " lambda ".
# import math
#
# area = {
#     'Circle': lambda r: print(round(math.pi * r ** 2)),
#     'Rectangle': lambda a, b: print(a * b),
#     'Trapezium': lambda a, b, h: print((h * (a + b)) / 2)
# }
# area['Circle'](12)
# area['Rectangle'](2, 5)
# area['Trapezium'](7, 5, 3)

### Lesson ###  lambda With Conditional ( if else )
# print((lambda a, b: a if a > b else b)(15, 13))
# print((lambda a, b: a if a > b else b)(12, 13))

# # ### Task 2: Min from 3 Number Voa " lambda ".
# # print((lambda x,y,z: min(x,y,z)))(6,2,10)
# print((lambda x, y, z: x if (x <= y) and (y <= z) else (y if (y <= x) and (y <= z) else z))(6, 2, 10))
# ### Find max Namber from three Namber Via " lambda ".
# print((lambda q, w, e: q if e <= q >= w else w if q <= w >= e else e)(16, 15, 13))


############### MAP - Loop In  ONE STRING, Use Together lambda ###############
### MAP(FUNC, ITARABLE) ###
# def mul(t):
#     return t * 2
#
#
# s1 = [2, 8, 12, -5, -8]
# s2 = "Hello"
#
# ls1 = list(map(mul, s1))
# ls2 = list(map(mul, s2))
# t1 = tuple(map(mul, s1))
# t2 = tuple(map(mul, s2))
# s1 = set(map(mul, s1))
# s2 = set(map(mul, s2))
# print(ls1)
# print(ls2)
# print(t1)
# print(t2)
# print(s1)
# print(s2)

#
# s1 = [2, 8, 12, -5, -8]
# s2 = (2, 8, 12, -5, -8)
# s3 = {2, 8, 12, -5, -8}
# s4 = {"Hello"}
# print(list(map(lambda k: k*2, s1)))
# print(list(map(lambda k: k*2, s2)))
# print(list(map(lambda k: k*2, s3)))
# print(list(map(lambda k: k*2, s4)))
# print(tuple(map(lambda k: k*2, s1)))
# print(tuple(map(lambda k: k*2, s2)))
# print(tuple(map(lambda k: k*2, s3)))
# print(tuple(map(lambda k: k*2, s4)))
# print(set(map(lambda k: k*2, s1)))
# print(set(map(lambda k: k*2, s2)))
# print(set(map(lambda k: k*2, s3)))
# print(set(map(lambda k: k*2, s4)))
# print(list(map(lambda k: k*2, (2, 8, 12, -5, -8))))
# print(tuple(map(lambda k: k*2, (2, 8, 12, -5, -8))))
# print(set(map(lambda k: k*2, (2, 8, 12, -5, -8))))

###### Contvert to TYPE " int ".
# s = ['1', '2', '3', '4', 5]
# print(s)
# print(type(s[0]))
# s1 = list(map(int, s))
# print(s1)
# print(type(s1[0]))


########### ROUND in MAP ##############
# areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.000135]
# res = list(map(round, areas))
# print(res)
# res = list(map(round, areas, range(len(areas))))
# print(res)
# res = list(map(round, areas, range(1, 4)))
# print(res)
# res = list(map(round, areas, range(2, len(areas)+1)))
# print(res)
# print(round(5.2345641, 3))


# ### Task 3 : Find Sum of 2 list ###
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))
# print(list(map(lambda x, y: x + y, (1, 5, 8), {2, 6, 1})))

######### Function "filter" Return DATA By Strict Conditional ########
##### Work with 1-element ########
#### FILTER ( FUNC, ITERABLE ) - Return if True.
# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# print(tuple(filter(lambda s: len(s) == 3, t)))

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

### Task 4: Filter 10 random namber. Chose from 10 to 20 ###
# from random import randint, randrange
#
# e = [randrange(100) for i in range(11)]
# print(e)
# print(list(filter(lambda x: 10 < x < 20, e)))
# print(tuple(filter(lambda x: 10 < x < 20, e)))
# print(set(filter(lambda x: 10 < x < 20, e)))

### Task5 ：Exctract Via ANONIMOUS Function Nambers that Division 15 ###
# b = [45, 55, 60, 37, 100, 105, 220]
# res1 = list(filter(lambda i: i % 15 == 0, b))  # True
# res2 = tuple(filter(lambda i: not i % 15, b))  # NOT True
# res3 = set(filter(lambda i: not i % 15, b))  # NOT True
# print(res1, "\n", res2,"\n", res3)

###Lesson odd Nam 0 t0 10 ###
# s = [45, 55, 60, 37, 100, 105, 220]
# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, range(10)))))
# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, s))))
# print([x ** 2 for x in range(10) if x % 2 != 10])

## Task 5: Remain palindrom:
# words = ('madam', 'firm', 'tomato', 'book', 'kiosk', 'mom',)
# print(list(filter(lambda i: i == i[::-1], words)))


################### DECORATORS ####################
######## Recieve another function that Do Anything #########

## Part 1 Oportunity Job Function
# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_hello'")
#     print(func())
#
#
# super_func(hello)

### 2 Case Assignment FUNCTION TO VARIABLE. ###
# def hello():
#     return "Hello, I am func 'hello"
#
#
# test = hello
# print(test)
# print(test())

### DECORATOR ###
############# IDEA By That DECORATIR To WORK. ##########
# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()

# ############ FUNCTION DECORATOR ###########
# def my_decorator(func):
#     def func_wrapper():  # Function Decorator
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# @my_decorator  # Decorator
# def func_test():  # DecoratIor Function
#     print("Hello, I am func 'func_test'")
#
# # func_test()
# @my_decorator
# def hello():
#     print("Hello, I am func 'func_test'")
#
#
# # func_test()
# # hello()
# test1 = my_decorator(func_test)
# test2 = my_decorator(hello)
# test1()
# test2()

### Decorator ###
# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "<\b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "<\i>"
#
#     return wrap
#
#
# @bold  # Use Firdt
# @italic  # Use Second
# def hello():
#     return "text"
#
#
# print(hello())

### Task 5: Decorator ### Output Number Call of Decorator Function and It's CONTENT.
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print("Вызов Функции: ", count)
#
#     return wrap
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

##### DECORATOR With 2 Argument #####
# ### PRINT Full Name ###
# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Data: ", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("My name: ", first, last)
#
#
# print_full_name("Irina", "Lavrova")


##### DECORATOR With MORE Argument #####
# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args: ",args)
#         print("kwargs: ", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "STADY", study, "\n")
#
#
#
#
# print_full_name("Boris", "Elka", "Svetka", study="JavaScript")
# print_full_name("Vlad", "Kate", "Victor")
