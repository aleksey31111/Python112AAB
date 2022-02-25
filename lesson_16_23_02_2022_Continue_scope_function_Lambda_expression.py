##### LESSON - 16 ###########
### Comtinue EXPLANATION nonlocal ###
# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()  #  Call nested Function.
#     return [a, b]  # return in outer()
#
#
# print(outer(2, 3, -1, 4))  # 1, 7

### Task 1 ###
# # Local VARIABLE S = 2(ab +bc +ac)
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j  # local Variable.
#
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(c, b))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(2, 6, 8))

# # Globall VARIABLE
# s = 0  # global Variable.
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


# # NONLOCAL VARIABLE
# def rect_paral_square(a, b, c):
#     s = 0   # Enclosed variable
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j  # local Variable
#
#         # return i * j
#
#     rect_square(a, b)  # j*i
#     rect_square(a, c)  # j*i
#     rect_square(c, b)  # j*i
#     # s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(c, b))
#     return 2 * s  # Return in out to Function
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(2, 6, 8))


# #### Замыкание ##### Without ()
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
# print(outer(3)(10))  # Don't Use
# add5 = outer(5) # n=5
# print(add5(10))  # x = 10
# print(add5(10)) # x=10
# add6 = outer(6) # n=6
# print(add6(10))  # n=10

## Use Замыкание ##
# def func1():
#     a = 1  # Enclosed variable
#     b = "line"  # Enclosed Variable
#     c = [1, 2, 3]  # Enclosed Variable
#
#     def func2():
#         nonlocal a, b  # scope for Local Immutable data type.
#         c.append(4)  # local Mutable data type.
#         b = b + "2"  # Immutable data type.
#         a = a + 1  # Immutable data type.
#         return a, b, c  # Nestef Function Result
#
#     return func2  # ONLY Use Return. Return Function_2 in Function_1 with Result.
#
#
# func = func1()
# print(func())


### Task 2 ### Counter CLOSURE
# def func(city):  # Head function.
#     s = 0  # Enclosed variable. Initialize counter
#
#     def func1():  # Nested Function
#         nonlocal s  # scope for immutable data type s
#         if city == 'Москва':
#             s += 1  # increase counter
#         else:
#             s += 1
#         print(city, s)
#
#     return func1
#
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


# #### STUDENT #### Output value by POINT.
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

### Function CLOSURE with Union Function for called functions.
# def func_object(a, b):
#     def add():  # Nested Function 1.
#         return a + b  # Return Enclosed variable
#
#     def sub():  # Nested Function 2.
#         return a - b  # Return Enclosed variable.
#
#     def mul():  # Nested Function.
#         return a * b  # Return Enclosed variable.
#
#     def replace():  # Union Function for Function add, sub, mul.
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     # add()                             # ER
#     # sub()                             # R
#     # mul()                             # O
#     # return add(), sub(), mul()        # R
#     return replace
#
#
# print(func_object(333, 333).add())
# print(func_object(333, 333).sub())
# print(func_object(333, 333).mul())
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
# print("func: ", func(1, 2))
# print("lambda: 11 + 12 = ", (lambda x, y: x + y)(11, 12))
# print("lambda: 111 + 113 = ", (lambda x, y: x + y)(111, 113))

# func1 = lambda x, y: x + y
# print(func1(1, 2))
# print(func("a", "b"))

### Task 3 ###
# print((lambda a, b: a ** 2 + b ** 2)(3, 4))
# summ = lambda a=1, b=2, c=3: a + b + c
# print(summ())
# print(summ(b=10))

# func = lambda *args: args
# print(func(1, 2, 3, 4))
# print(func('a', 'b', 'c'))

# c = (lambda x: x * 2, lambda x: x * 3, lambda x: x * 4)
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
# d = {'a': 10, 'c': 15, 'b': 4}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[0])
# print(list_d)


#### List Action by Request ####
# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[0](12, 6)
# c = a[1](12, 6)
# d = a[2](12, 6)
# e = a[3](12, 6)
# print(b, c, d, e)
#
# #### TYPE LAMBDA ####
# print(type((lambda x, y: x + y)))
