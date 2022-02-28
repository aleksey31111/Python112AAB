### HomeWork 16 ###
# players = [{'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
#
# res = sorted(players, key=lambda item: item['last name'], reverse=True)
# print(res)

### LESSON 17 ### Continue:
# a = {'one': lambda x: x - 1, "two": lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

### Day of Week: ###
# d = {
#     1: lambda: print('Monday'),
#     2: lambda: print('Tuesday'),
#     3: lambda: print('Wensday'),
#     4: lambda: print('Thursday'),
#     2: lambda: print('Friday'),
#     3: lambda: print('Saturday'),
#     4: lambda: print('Sanday')
# }
# d[7]()


# ### Task :L  Square Circle, Rect, Trapecii
# import math
#
# area = {
#     'Circle': lambda r: print(math.pi*r**2),
#     'Rectangle': lambda a, b: print(a*b)
#
# }
# area['Circle'](12)
# area['Rectamgle'](2,5)
#
# ### Lesson ###
# print((lambda a,b: a if a>b else b)(12, 15))

# ### Task 2: Min
# print((lambda x,y,z: min(x,y,z)))(6,2,10)
# print((lambda x,y,z: x if (x<=y) and(y<=z) else(y if(y<=x)and(y<=z) else z))(6,2,10))


### MAP(FUNC, ITARABLE) ###
# def mul(t):
#     return t * 2


# s = [2, 8, 12, -5, -8]
# s = "Hello"

# ls = list(map(mul, s))
# t = tuple(map(mul, s))
# s = set(map(mul, s))
# print(ls)
# print(t)
# print(s)

# s = [2, 8, 12, -5, -8]
# print(list(map(lambda k: k*2, s)))
# print(list(map(lambda k: k*2, (2, 8, 12, -5, -8))))

# s = ['1', '2', '3', '4', 5]
# print(s)
# print(type(s[0]))
# s1 = list(map(int, s))
# print(s1)
# print(type(s1[0]))


areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.000135]


# res = list(map(round, areas, 2))
# print(res)
# res = list(map(round, areas, range(1, 7)))
# print(res)
# res = list(map(round, areas, range(1, 4)))
# print(res)
# res = list(map(round, areas, range(1, len(areas)+1)))
# print(res)
# print(round(5.2345641, 3))


### Task 3 : Find Sum of 2 list ###
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y,l1,l2)))


#### FILTER ( FUNC, ITERABLE ) - Return if True.
# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# print(tuple(filter(lambda s: len(s) == 3, t)))

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

### Task 4: Filter 10 random namber. Chose from 10 to 20 ###
# from random import randint
#
# l=[randint(1, 100) for i in range(11)]
# print(l)
# print(list(filter(lambda x: 10<x<20,l)))

### Task5 ：
# l = [45, 55, 60, 37, 100, 105, 220]
# # res = list(filter(lambda i:i%15 == 0, b))
# res = list(filter(lambda i: not i % 15, l))
# print(res)

###Lesson odd Nam 0 t0 10 ###
# l = [45, 55, 60, 37, 100, 105, 220]
# print(list(map(lambda x: x ** 2, filter(lambda x: x%2 != 0, range(10)))))
# print([x ** 2 for x in range(10) if x % 2 != 10])

## Task 5: Temain palindrom:
# l = ('madam', 'firm', 'tomato', 'book', 'kiosk', 'mom',)
# print(list(filter(lambda i: i == i[::-1], l)))


################### DECORATORS #################### Recieve another function
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


# def hello():
#     return "Hello, I am func 'hello"
#
#
# test = hello
# print(test())

### DECORATOR ###
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
# def func_test():  # Decorator Function
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def hello():
#     print("Hello, I am func 'func_test'")
#
#
# func_test()
# hello()
# # test = my_decorator(func_test)
# # test()

### Decorator ###
# def bold(fn):
#     def wrap():
#         return "<b>"+ fn()+ "<\b>"
#     return wrap()
# def italic(fn):
#     def wrap():
#         return  "<i>"+fn()+"<\i>"
#     return wrap
#
# @bold
# @italic
# def hello():
#     return "text"
#
# print(hello())


### Task 5: Decorator ###
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count +1
#         fn()
#         print("Вызов Функции: ", count)
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()


# ### PRINT Full Name
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
#     print("My name", first, last)
#
#
# print_full_name("Irina", "Lavrova")
def args_decorator(fn):
    def wrap(*args, **kwargs):
        print("args: ",args)
        print("kwargs: ", kwargs)
        fn(*args, **kwargs)

    return wrap

@args_decorator
def print_full_name(a,b,c,study="Python"):
    print(a,b,c,"STADY", study,"\n")


print_full_name("Boris","Elka","Svetka",study="JavaScript")
print_full_name("Vlad","Kate","Victor")