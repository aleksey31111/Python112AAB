### Return 2 value ###
# def is_greater(x,y)
#     if x>y:
#         return True
#     else:
#         return False
#     print(is_greater(10, 5))
#     print(is_greater(10, 5))

####Check Password ####
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     # else:
#     #     return False
#
#     # return
#     return False
#
#
# p = input("Enter Password:")  # 123An456
# # print(check_password)
# if check_password(p):
#     print("Это Надежный пароль: ")
# else:
#     print("Это Не Надежный пароль: ")

####### Позиционные Аргументы ######
# def get_sum(a=5, b=3, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5, ))
# print(get_sum(1, 5, d=2))
# print(get_sum(d=2))

### Term 1 ###
# def set_param():
#     for i in set_param:
#
#
# set_param(10,"+")
# set_param(5,"*")
# set_param(15,"#")
# set_param(7)
# set_param()

# def set_param(x=20, y='-'):
#     print(x*y)
#
#
# set_param(10,"+")
# set_param(5,"*")
# set_param(15,"#")
# set_param(7)
# set_param()


##### Проверка логина и Пароля #####
# def check_password(username, password, min_length=9, check_user=True):
#     if len(password) < min_length:
#         print("пАРОЛЬ СЛИШКОМ КОРОТКИЙ")
#         return False
#
#
# check_password('igor', '12345')
# check_password('igor', '12345', 4)
# check_password('igor', '12345', 12)

# def check_password(username, password, min_length=9, check_user=True):
#     if len(password) < min_length:
#         print("пАРОЛЬ СЛИШКОМ КОРОТКИЙ")
#         return False
#     elif check_user and username in password:
#         print("Пароль содержит Имя Пользователя")
#         return False
#     else:
#         print("Пароль для пользователя", username, "Прошел все проверки")
#         return True
# check_password('igor', '12345')
# check_password('igor', '12345', 4)
# check_password('igor', '12345', 12)
# check_password('igor', '12345igor')
# check_password('igor', '12345name')

#### Term 2 ###
# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s


# print("Сумма четных цифр: ")
# print((digit_sum(9874023)))
# print((digit_sum(38271)))
# print((digit_sum(123456789)))
#
# print("Сумма Не Четных цифр: ")
# print((digit_sum(9874023, even=False)))
# print((digit_sum(38271, even=False)))
# print((digit_sum(123456789, even=False)))

# def check_password(username):
#
#     username=str(username)
#     sum=0
#     sum1=0
#     for i in username:
#         c=int(i)
#         if c%2==0:
#             sum+=c
#         else:
#             sum1+=c
#     print('Сумма четных элементов: ', sum)
#     print('Сумма нечетных элементов: ', sum1)


# def func(a, ln=None):
#     if ln is None:
#         ln = []
#     ln.append(a)
#     return ln
#
#
# print(func(1, ln=[2, 3]))
# print(func(2)) # 1, 2
# print(func(3)) # 1, 2, 3


# a=5
# b=5
# print(id(a))
# print(id(b))
#
# print(a == b) # value
# print(a is b) # address

##### Целое #####
a = 1
print(id(a))
a += 1
print(a)
print(id(a))

# ##### Список #### Изменяемый тип данных
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt1))
#
# print(lt1 == lt2) # value
# print(lt1 is lt2) # address

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))
# lt1.pop(1)
# print(lt1)
# print(id(lt1))
# lt1[1] = "Hello"
# print(lt1)
# print(id(lt1))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1 = [4, 5]
# lt1 += [4, 5]


####  Строки #### Неизменяемый тип данных
# s = "Hello"
# print(id(s))
# s += 'World' # s = s + World
# print(s)
# print(id(s))
#
# s = "Hello"
# s1 = "Hello"
# print(id(s))
# s = s[1:-1]
# print(s)
# print(id(s))
# ....

##### Функция с типами данных #####
# def add_number(n):
#     print("Внутри функции: ", n, "=", id(n))
#     n += 1
#     print("После присвоения: ", n, "=", id(n))
#     return n
#
# x = 1
# print(x, "=", id(x))
# add_number(x)
# print(a, "=", id(x))

# def add_number(n):
#     print("Внутри функции: ", n, "=", id(n))
#     n += 1
#     print("После присвоения: ", n, "=", id(n))
#
#
# x = 1
# print(x, "=", id(x))
# add_number(x)
# print(x, "=", id(x))

# def add_number(n):
#     print("Внутри функции: ", n, "=", id(n))
#     n += [4]
#     print("После присвоения: ", n, "=", id(n))
#     return n
#
# x = [1,2,3]
# print(x, "=", id(x))
# add_number(x)
# print(x, "=", id(x))

# def add_number(n):
#     print("Внутри функции: ", n, "=", id(n))
#     n = n + [4]
#     print("После присвоения: ", n, "=", id(n))
#
#
# x = [1,2,3]
# print(x, "=", id(x))
# add_number(x)
# print(x, "=", id(x))


#################### TUPLE == КОРТЕЖ ##################### Не Изменяемый
# lst = [10, 20, 30]
# tp = (10, 20, 30)
# print(lst.__sizeof__())
# print(tp.__sizeof__())
#
# a = ()
# print(type(a))
#
# b = tuple()
# print(type(b))
# a = (1, 2, 3, 4, 5)
# print(a)
# print(type(a))
# b = 1, 2, 3
# print(b)
# print(type(b))
#
# print(tuple((1, 2, 3, 4)))
#
# t = ()
# print(type(t))
# t = (1,)
# print(type(t))
# t = tuple('hello')
# print(t)
# print(type(t))
#
# a = tuple((1, 2, 3, 4, 5))
# print(a)
# print(a[1:3])
# print(a[3])


##### Создание КОРТЕЖА #####
# s1 = tuple([int(input("->"))for i in range(1, 3)])
# print(s1)
# s1 = tuple(int(input("->"))for i in range(1, 3))
# print(s1)

import random
# s1 = [random.randint(0, 100) for i in range(10)]
# s1 = tuple(random.randint(0, 100) for i in range(10))
# s = s1
# print(s1)
# import math
# s1 = tuple(math.pow(i, 2) for i in range(2, 13))
#
# print(s1, end=" ")

##### homework #####
# t1 = tuple("hello")
# t2 = tuple(" world")
# t3 = t1 + t2
# print(t3)
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('l'))
# # print(t3.index('a'))
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print("Такого символа НЕТ")
#
# for i in t3:
#     if i == " ":
#         continue
#     print(i, end=" ")