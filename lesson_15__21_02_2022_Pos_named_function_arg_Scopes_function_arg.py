############### LESSON 15 #############
### TASK 1 ###
# def func(*args):
#     # a = zip(args1)
#     # return zip
#     return {i: 1 for i in args}
#
#
# print(func(1,2,3,4))


### TASK 2 ###


# def func(*args):
#     avarage = sum(args)/len(args)
#     for i in args:
#         if i< avarage:
#             print(i)
#     print(avarage,i,end=" ")
#
# func(1,2,3,4,5,6,7,8,9)
# func(3,6,1,9,5)

# def func(*a):
#     r = (sum(a) / len(a))
#     d = []
#     for i in a:
#         if i < r:
#             d.append(i)
#     print(r)
#     return d
#
#
# func(1, 2, 3, 4, 5, 6, 7, 8, 9)
# func(3, 6, 1, 9, 5)

### pos arg with args ###
# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))

### STUDENT ###
# def func(student, *scores):
#     a = ("Student name: " + student)
#     # # s = []
#     # # print(a)
#     # # print(*scores)
#     # for score in scores:
#     #     s.append(score)
#     #     # print(score,end=", ")
#     print(a, *s, end=" ")
# print(*s) #, end=", ")
# b = a
# return b


# print(func("Igor", 100, 95, 88, 92, 99))
# print(func("Rick", 69, 96, 20, 33))


### TERM 3 Together REVERS ODD### Include func
# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2 != 0):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))


#### FUNCTION Argument DICT #####
# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='python'))

## EXAMPLE ##
# def info(**data):
#     for key,value in data.items():
#         print(key, "is", value)
#     print()


# info(firstname="Irina", lastname = "Saunal", age=22, phone=1124564789)
# info(firstname="Igor", lastname="Wood", email="igor@mail.ru",age=22,phone=1124564789, country="Russia")


### Term 4 ###
# def db(**kwargs):
#     my_dict.update(**kwargs)
#
#
# my_dict = {"one":"first"}
# db(k1=22,k2=31,k3=11,k4=91)
# db(name='Bob',age=31,weight=61,eyes_color="grey")
# print("my_dict =", my_dict)

### Spec * - pos arg, ** - named arg ###
# def func(a, *args, b=False, **kwargs):
#     return a, args, b, kwargs
#
#
# print(func(1, 2, 3, 4, x=11, y=12, z=13, b=True))

### From Named arg     #####
# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
# func1(1,2,3,4,5,6)
# func2(one=123, two=456)


#### 2 DICT ###
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {**x, 'one': 1, 'two': 2, **y}
# print(z)


#### SCOPE - область видимости ###
# # global var - out from func
# # local var - in from func
# name = "Tom"
#
#
# def hi():
#     global name
#     name = "Sam"
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bye()
# print(name)

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()
# print(i)


##### FOLDER 12 #####  BUILT-IN
# max=5
# print(max)


### Scope ###
# def add_two(a):
#     x = 2
#     return a + x
#
#
# print(add_two(3))

#
# def add_two(a):
#     x = 2
#     # return a + x
#     def add_some():
#         print(" x = " + str(x))
#         return a + x
#     return add_some()
#
#
# print(add_two(3))


# x =4
# def fun():
#     print(x+3)
#
#
# fun()


# import builtins
# names=dir(builtins)
# for t in names:
#     print(t)

#
# def outer_func():
#     def inner_func():
#         print("hello, World!")
#     inner_func()
#
#
# outer_func()


# def outer_func(who):
#     print(who)
#
#     def inner_func():
#         print("hello,", who)
#
#     inner_func()
#
#
# outer_func("World!")


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумма внутренней функции:", a + b)
#
#     print("Значение внешней переменной a:", a)
#     fun2(4)
#
#
# fun1()

#
# x = 25
#
#
# def fn():
#     global t
#     a = 30
#     # t = a
#     print("global:", x)
#
#     def inner():
#         a = 35
#         print(a)
#
#     inner()
#     print(a)
#     t = a
#
#
# fn()
# z = x + t
# print(z)


def fn1():
    x1 = 25

    def fn2():
        x1 = 35

        def fn3():
            nonlocal x1
            x1 = 55

        fn3()
        print("fn2.x1 = ", x1)

    fn2()
    print("fn1.x1 = ", x1)
fn1()