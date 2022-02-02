### lesson 10 ###
#### GIT and GITHUB ####
# git clone https://github.com/aleksey31111/Python112AAB
# clone rename
# pull -
# push -
##########


##### FUNCTION #####
# def hello(name, word):  # аргументы
#     print("Hello", name, ". Say ", word, sep="")
#
#
# hello("Irina", "hi")  # параметры
# hello("Ivan", "hello")
#
#
# def get_sum(a, b):
#     print(a + b)
#
#
# get_sum(2, 5)
# a = 2
# b = 5
# get_sum(a, b)
# x = 1
# y = 8
# get_sum(x, y)
#
# n = 1
# m = 8
# get_sum(n, m)
# get_sum("abc", "def")

# def symbol(numbers, ch, char):
#     s= 0
#     for i in range(numbers):
#         if i % 2 == 0:
#             s += ch
#         else:
#             s += char
#         print(s)
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")
# def symbol(num,s1,s2):
#     ch =0
#     # while ch != num:
#     for ch in range(num):
#         if ch % 2 == 0:
#             print(s1,end="")
#         else:
#             print(s2, end="")


# symbol(9, "+", "-")
# symbol(7, "X", "0")

# def get_sum(a, b):
#     print("Строка")
#     return a + b
# print("Строка") # ERROR

# get_sum(2, 5)
# n = 2
# m = 5
# res = get_sum(n,m)
# # get_sum(n,m)
# print(res)

# def maximum(one, two):
#     if one > two:
#         return one
#     elif two > one:
#         return two
#     else:
#         return
#
# m = maximum(9, 9)
# print(m)

# def add(x, y):
#     if x > y:
#         return x - y
#     elif x < y:
#         return x + y
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# m = add(a, b)
# print(m)

# def cube(a):
#     return pow(a, 3)
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         #a, b = b, a + b
#         c = a + b
#         a = b
#         b = c


# fib(15)

def change(lst):
    start = lst.pop()  # 3
    end = lst.pop(0)  # 0
    lst.append(end)
    lst.insert(0, start)
    # a = lst([0])
    # b = lst([-1])
    # lst.removw([0])
    # lst.remove([-1])
    # lst.insert(0, b)
    # lst.append(a)
    return lst


print(change([1, 2, 3]))
print(change([9, 12, 33, 54, 105]))
print(change(['с', 'л', 'щ', 'н']))

# def change(s):
#     a=s[0]
#     b=s[-1]
#     for i in range(len(s)):
#         if i == 0:

# def change(s):
#     s[0], s[-1] = s[-1], s[0]
#     return s
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'щ', 'н']))
