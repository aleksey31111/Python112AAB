# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("---------")
# ##### Rectangle From "*" ######
# w = 13 # int(input("width"))
# h = 3 # int(input("height"))
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#         print(" ", end="")
#         # print("*", end="") if i == 0 or i == h - 1 or j == 0 or j == w - 1 else print(" ", end="")
#     print()
#
# w = 13 # int(input("width"))
# h = 5 # int(input("height"))
# for i in range(h):
#     for j in range(w):
        # if i == 0 or i == h - 1 or j == 0 or j == w - 1:
        #     print("*", end="")
        # else:
        #     print(" ", end="")
    #     print("*", end="") if i == 0 or i == h - 1 or j == 0 or j == w - 1 else print(" ", end="")
    # print()
#

# [ результирующее выражение | цикл | опциональное условие ]
# print("1")
# print(i for i in range(10))
# print("2")
# print([i for i in range(10)])
# print("3")
# for i in range(10):
#     print(i, end=" ")
# print()
# print("4")
# for i in range(10):
#     if i % 2 == 0:
#         print(i, end=" ")
# print()
# print("5")
# print([i for i in range(10) if i % 2 == 0])
# print()
# print("6")
# print([letter * 2 for letter in "Banana"])

####### СПИСКОК == МАССИВ #############
#let arr = [1, 2, 3, 4, 5, 6, 2.3, "Hello"] ## javaScript
###nums = [8, 3, 6]
###print(nums[0])
###nums[-1] = 255
###print(nums)
# print(nums)
# print(type(nums))
# print(type([2, 3.2, "three", True]))

# nums = [8, 3, 6, 9, 7, 3]
# print(nums[0])
# print(nums[1])
# print(nums[5])
# print(nums[-1])
# nums[-1] = 253
# print(nums)
# nums[3] += 100
# print(nums)
###print("Длинна списка", len(nums))
#
# a = [1, 2]
# print(id(a))
# a[1] = 3
# print(a)
# print(id(a))

# s = [1, 2, 3]
# print(s)
# s = list()
# # s = []
# print(s)
###### s[0] = 5
# print(s)
# s = [1, 2, 3]
# print(s)
# s = list("Hello")
# # s[0] = 5
# print(s)
#
# n = [5] * 6
# print(n)
#
# n = range(10)
# print(n)
# n = list(range(10))
# print(n)

n2 = [10, 8, 6, 4]
print(n2)
n = list(range(10))

# print(id(n2))
# n = list(range(10, 2, -2))
# print(id(n))
# if n == n2:
#     print("Списки равны")
# else:
#     print("Списки разные")
#
# if n is n2:
#     print("Списки равны")
# else:
#     print("Списки разные")
#
# a = [0 for i in range(5)]
# print(a)
#
# a = [5 for i in range(5)]
# print(a)
#
# n == 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)
#
# a = [1, 2, 3]
# b = [4, 5]
# b += a
# print(b)
# c = a + b
# print(c)
# print(c * 3)

##### a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("->"))
# print(a)
#


##### Вывод СПИСКА #######
# for i in range(len(a)):
#     a[i] += 5
#     # print(a[i], end=" ")
#     print(a)
# print("*" * 20)
# for i in range(len(a)):
#     a[i] += 5
#     # print(a[i], end=" ")
#     print(a)
# print("*" * 20)
# # a = [a[i] + 5 for i in range(len(a))]
# print([a[i] + 5 for i in range(len(a))])
# print(a)
# print(id(a))

###### Term #####
# n = [0] * int(input("number: "))
# #a = int(input("-->"))
# for i in range(len(n)):
#     if a[i] < 0:
#         a += a[i]
# print(a)

# a = list(range(10, 100, 10))
# print(a)
# for i in range(len(a)):
#     print(a[i] + 2, end=" ")
# print()
# for i in a:
#     print(a[i] + 2, end=" ")
# print()

############ Term 21-41 ##################
# a = [0] * 20
# # print(for i in range(a))
# for i in range(len(a)):
#     print(i if i % 2 == 0 else i % 2 != 0
#     i += i)
#

###########term avarage not 0 ########
# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# s = k = 0
# for i in range(len(a)):
#     s += a[i]
#     if a[i] != 0:
#
#         k += 1
# print("AVARAGE: ", s / k)

########### СРЕЗ ######
## СПИСОК[START:STOP:STEP]
# s = [5, 9, 3, 7, 1, 8]
# print(s[1:3])
#
# s= list(range(1,8))
# print(s[:])
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[4:1:-1]) # print(s[-3:1:-1])
# print(s[2:5:1])