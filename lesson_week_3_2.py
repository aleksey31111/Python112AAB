# n = input("Let input namber: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Namber is Not int!")
#         n = input("Let input INT: ")
# if n %2 == 0:
#     print("Число четное")
# else:
#     print("Число Не четное")
#
# i = 0
# while i < 10:
#     # print(i, end="")
#     if i == 3:
#         continue
#         print(i, end=" ")
#     # if i == 5:
#     #     break
#     i += 1
# print("\n CICLE END")


# while True:
#     n = int(input())
#     if not n > 0:
#         break


# nam = int(input("Введите число: "))
# while True:
#     nam1 = int(input("Введите число: "))
#     nam +=nam1
#     print(num)
#     if nam1 == 0:
#         print("Muktiple 0 is not")
#         break
# num = 1
# while True:
#     num1 = int(input("Input Namber: "))
#     if num1 == 0:
#         break
#     num *= num1
# print(num)
# i = 0
# while i < 10:
#     # if i == 5:
#     #     break
#     print(i)
#     i += 1
# else:
#     print("Loop END, 1 =", 1)
# print("OUT CICLE")

#############Внещний Внутренний ЦИКЛ
# i = 1
# while i<5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1


# a = 0
# b = 1
# while a < 10:
#     a += 1
#     while b < 10:
#         print(a, "*", b, "=", a * b)
#         b += 1

################# Multiple Table #############
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end='\t\t')
#         j += 1
#     print()
#     i += 1

# ##### Squer Of Char
# i = 0
# while i < 3:
#     j = 0
#     while j< 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

#############Squer Of "+++++" and "------"
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


##########Diagonal line@@@@@@@@@@@@@
# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1
#
# i = 0
# c = " "
# d = '%'
# j = 0
# while i < 1:
#     j = 0
#     while j < 5:
#         print(c * j, d)
#         j += 1
#     i += 1
#
# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

################### FOR ##################
# for i in "Hello!":
#     print(i)
#
# i = 1
# for color in 'red', 'green', 'yello', 1, 20, 0.3:
#     print(i, "color:", color)
#     i += 1
#
# # print(range(9))
#
# # for(let i = 0; i < 12; i++){}
#
# # range(start, stop, step)
# for i in range(9, 16, 3):
#     print(i, end=" ")
#
# for i in range(9, 0, -1):
#     print(i, end=" ")


# nam = int(input("Введите целое число: "))
# print(range(0, nam))
# i =1
# for i in range(1, nam):
#     for j in range(1,nam):
#         if(i%j==0):
#             print(j)

# a = int(input("введите число"))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")

# i = 11
# for i in range(11,100,i):
#     print(i, end=" ")

# i = 11
# for i in range(10,100):
#     if i%10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')
