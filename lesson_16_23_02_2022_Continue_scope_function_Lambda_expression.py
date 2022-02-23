# ##### LESSON - 16 ###########
# def outer(a1, a2, b1, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # 1, 7


### Task 1 ###
# # Local VARIABLE
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(c, b))
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(2, 6, 8))

# # Globall VARIABLE
# s = 0
#
#
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     global s
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(c, b))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print(s)
# print(rect_paral_square(5, 8, 2))
# print(s)
# print(rect_paral_square(2, 6, 8))
# print(s)


# Globall VARIABLE
# s = 0
#
#
# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i + j
#
#         return i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(c, b)
#     # s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(c, b))
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# print(s)
# print(rect_paral_square(5, 8, 2))
# print(s)
# print(rect_paral_square(2, 6, 8))
# print(s)


#### Замыкание ##### Without ()
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
# print(outer(3)(10))  # Don't Use
# add5 = outer(5)
# print(add5(10))  # x = 10
# print(add5(10))
# add6 = outer(6)
# print(add6(10))

## Use Замыкание ##
# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         b = b + "2"
#         a = a + 1
#         return a, b, c
#
#     return func2  # ONLY Use Return
#
#
# func = func1()
# print(func())


### Task 2 ###
# def func(city):
#     s = 0
#     def func1():
#         nonlocal s
#         if n == 'Москва':
#             s +=1
#         else:
#             s+=1
#         print(n,s)
#     return inner
#
# res = func('Москва')
# res()
# res()
#
# res = func('Сочи')
# res()
# res()
#
# res()


# def func(city):
#     s = 0
#     def func1(n):
#         nonlocal s
#         s +=1
#         print(n,s)
#     return inner
#
# res = func('Москва')
# res()
# res()
#
# res = func('Сочи')
# res()
# res()
#
# res()


#### STUDENT ####
# students = {
#     "Alice": 98,
#     "Bob": 67,
#     "Devid": 85,
#     "Chris": 75,
#     "Ella": 54,
#     "Fiona": 35,
#     "Grace": 69
# }
#
#
# def outer(lower, upper):
#     def inner(exam):
#         return {k: v for (k, v) in exam.items() if lower <= v < upper}
#
#     return inner
#
#
# a = outer(80, 100)
# b = outer(70, 80)
# c = outer(50, 70)
# d = outer(0, 50)
# print(a(students))
# print(b(students))
# print(d(students))
# print(d(students))


# def func_object(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = add
#     # add()                             # ER
#     # sub()                             # R
#     # mul()                             # O
#     # return add(), sub(), mul()        # R
#     return replace
#
# obj1 = func_object(5, 2)
# print(obj1.add())
# obj2 = func_object(5, 2)
# print(obj2.sub())
# obj3 = func_object(5, 2)
# print(obj3.mul())


############## LAMBDA Function - Not Rename ###############
# def func(x1, y1):
#     return x1 + y1
#
#
# print(func(1, 2))
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
# # func1 = lambda x, y: x + y
# # print(func1(1, 2))
# # print(func("a", "b"))

### Task 3 ###
# print((lambda a, b: a ** 2 + b ** 2)(3, 4))

# summ = lambda a=1, b=2, c=3: a +b + c
# print(summ())
# print(summ(b=10))

# func = lambda *args: args
# print(func(1, 2, 3, 4))
# print(func('a', 'b', 'c'))

# c = (lambda x: x * 2, lambda x: x*3, lambda x: x*4)
# for t in c:
#     print(t('abc'))


# def inc1(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# def inc(n):
#     return lambda x: x + n
#
#
# inc2 = (lambda n: (lambda x: x + n))
#
# c = inc1(11)
# print(c(4))
# t = inc2(21)
# print(t(3))
# f = inc(42)
# print(f(2))
# print((lambda n: (lambda x: x + n))(32)(5))


###Task 4 ###
# print((lambda m: (lambda y:(lambda z: m + y +z)))(4)(6)(10))

### Key in Lambda ###
# d = {'a': 10, 'b': 15, 'c': 4}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[0])
# print(list_d)


#### List Action by Request ####
a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
b = a[0](12, 6)
c = a[1](12, 6)
d = a[2](12, 6)
e = a[0](12, 6)
print(b, c, d, e)

#### TYPE LAMBDA ####
print(type((lambda x, y: x + y)))
