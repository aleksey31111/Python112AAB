##### HOMWORK UNIQUE NAMBER #####
lst = [int(input("--> ")) for i in range(int(input("n: ")))]
###lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
print(lst)
for j in range(len(lst)):
    for i in range(len(lst)):
        if lst[j] == lst[i] and j != i:
            break
    else:
        print(lst[j], end=" ")

### SLICE ###
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s[1:3])  # [3, 5]
# s[1:3] = [20]
# print(s)
# s[4] = [30]
# print(s)

### Method Of LIST ### LIST METHOD = Method Packet 5
###python Console### dir(list)
# print(dir(list))
#
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# print(id(s))
# s.append(99)
# #s.append([99, 1])
# print(s)
# print(id(s))
#
# s.extend([99, 77, 66])
# print(s)

#### EXAMPLE SELF ####
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [range(11) for i in range(11):]
# d=[]
# for i in range(1,11):
#     d.extend([i ** 2])
# print(d)
#
# #### EXAMPLE ####
# b=[1,2,3,4,5,6,7,8,9,10]
# c = []
# for i in range(1, 11)
#     d = i * i
#     c.append(d)
# print(c)

### INSERT ###
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# s.insert(2, 100)
# print(s)

# lst = []
# n = int(input("Количество Элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     lst.append(x)
# print(lst)

#### TerM = 2 ####
# lst = []
# n = int(input("Количество Элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     if x % 3 == 0:
#         # lst.append(x)
#         lst.extend([x])
#         print(lst)
#     else:
#         continue
# print(lst)


### MATCH LIST ###
# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#             c.append(j)
# print(c)  # [2, 1, 4, 3]
# c = []
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a
# .....

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             c.append(j)
# print(c)  # [2, 1, 4, 3]

#### Term ####
# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# for i in range(len(b)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# s.remove(22)
# print(s)
# s.appwnd(99)
# print(s)
# s.extend([11, 77, 66])
# print(s)
#
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# print(s.pop(3))
# print(s.pop())
# print(s.pop(0))
# print(s)
# s.clear()
# print(s)
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# del s[:]
# print(s)
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# del s[2]


# #### Term ####
# print("Введите элементы списка: ")
# a = [int(input("--> ")) for i in range(int(input("n = ")))]
# k = int(input("k = "))
# a.pop(k)
# print(a)

### COUNT ####
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# num = s.count(2)
# print(num)
# print(s)

### INDEX ###
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# ind = s.index(2)
# print(ind)
# print(s)
# ind = s.index(2, 5)
# print(ind)
# print(s)
# ind = s.index(2, 5, -1)
# print(ind)

### COPY ###
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# s_copy = s.copy()
# print(s_copy)
# s.append(120)
# print(s)
# print(s_copy)
# print(id(s))
# print(id(s_copy))
#
# a = [1,2,3]
# b = a
# print("a = ", a)
# print("b = ", b)
# a.append(20)
# print("a = ", a)
# print("b = ", b)
# print(id(a))
# print(id(b))

### REVERSE ###
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# s.reverse()
# print(s)

### SORT ###
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# s.sort()
# print(s)
# s.sort(reverse=True)
# print(s)

### Built in SORTED ###
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# st = sorted(s, reverse=True)
# print(st)

# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len)
# print(s2)
# s2.sort(key=len, reverse=True)
# print(s2)

#### Term ####
# #### Term ####
# print("Введите элементы списка: ")
# a = [int(input("--> ")) for i in range(int(input("n = ")))]
# k = int(input("k = "))
# a.pop(k)
# a.remove(k)
# print(a)
# print(sorted(a, reverse=True))
# ind = a.
