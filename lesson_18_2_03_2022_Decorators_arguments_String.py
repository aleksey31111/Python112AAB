##### LESSON 18
## CONTINUE
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

#
# def args_decorator(arg1, arg2):  # Igor Nefedov
#     print("Arguments: ", arg1, arg2)
#
#     def wrapper(func1):
#         def wrap(func_arg1, func_arg_2):
#             print("Arguments of Function: ", func_arg1, func_arg_2)
#             func1(func_arg1, func_arg_2)
#             # return func1(func_arg1, func_arg_2)
#             return func1(arg1, arg2)
#
#         return wrap
#
#     return wrapper
#
#
# @args_decorator("Igor", "Nefedov")
# def func(first, last):
#     print("My name is: ", first, last)
#
#
# print("Irina", "Lavrova")


### Decorator 2
#
# def args_decorator(decorator_text):
#     def wrapper(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#         return wrap
#     return wrapper
#
#
#
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world(text):
#     print(text)
#
# @args_decorator(decorator_text="Hi, ")
# def hello_world(t2):
#     print(text, "and", t2)
#
# hello_world("world")
# hello("Igor", "Irina")


# ### Task 1 :
# def multiply(a):


# ##### Restrict ####
# def typed(*args, **kwargs):
#     print(*args)
#     print(**kwargs)
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     print("Некорректный тип данных")
#                     raise TypeError("Некорректный тип данных")
#             for k in range(len(kwargs)):
#                 raise TypeError("Некорректный тип данных")
#             for k in kwargs:
#                 if type(f_args[i]) != args[i]:
#                     print("Некорректный тип данных")
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x * y * z
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello"):
#     return x + y + z
#
#
# # print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Hello"))
# # print(typed_fn2("Hello, ", "world", "!"))
# # print(typed_fn2("Hello, ", "world", 2))
# print(typed_fn3("Hello, ", "world!  ", z=2))


# ### Decorator with param and without
# def decor(tx=None, dec_text=""):
#     def wrapper(func):
#         def wrap(*args):
#             print(dec_text, end="")
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#     # return wrapper
#
#
# @decor
# def hello_world2(text):
#     print(text)
#
#
# hello_world2("Hi!")
#
#
# @decor(dec_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# hello_world("hello")


###########################  Work with string data "STR" #################
####### print(01)  # Error
# print(int('19'))
# #######print(int('19.5'))  # Error
# print(int(19.5))
# print(int("100", 2)) # Convert Type to Binary
# print(int("100", 8)) # Convert Type to octo
# print(int("100", 10)) # Convert Type to 10
# print(int("100", 16)) # Convert Type to 16

# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12
#
# print(0b10010)
# print(0o22)
# print(0x12)


########### CODING ASCII ##############
### 128 - character

########### CODING UNICODE ############
### STANDART Coding
## - UTF-8
## - UTF-16
## - UTF-32


#### string ####
# q = 'pYT'
# w = "hon"
# e = q + w
# print(e)
# print(e * 3)
# print(e * -3)

# s = 'agshdjeu'
# print(s[slice(2, 5)])
# print(s[slice(5,None,-1 )])
# print(s[slice(None,None,-1 )])

# s='python'
# s=s[:3]+'t'+s[4]
# print(s)

def change_char_to_str(s, old, new):
    s2 = ""
    i = 0
    while i < len(s):
        if s[i] == old:
            s2 = s2 + new
        else:
            s2 = s2 + s[i]
        i = i + 1

    return s2


str1 = "Я изучаю Nuthon. Мне нравится Nuthon.  Nuthon очень интерестный"
str2 = change_char_to_str(str1, "N", "P")
print("str1 =", str1)
print("str2 =", str2)
# for i in str1:
#     if i == "N":
#         str2.append.str1[:i] + "P" + str1[i + 1::]
# print(str1)
