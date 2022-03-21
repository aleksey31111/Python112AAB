# ### Continue lesson 23
# ### Recursion Of List: ###
print(")#### Function RECURSION For Direct List:")


def union(s):
    if not s:  # #s= []
        return s
    if isinstance(s[0], list):
        return union(s[0]) + union(s[1:])
    return s[:1] + union(s[1:])  # 'Adam', 'Bob'


names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
print("Выпрямленный список: ", union(names))
print()
print()

print("Recursion For Delete 'Space' or 'TAB'")


def remove(text):
    if not text:
        return ""
    if text[0] == "\t" or text[0] == " ":
        return remove(text[1:])
    else:
        return text[0] + remove(text[1:])


print(remove(" Hello\tWorld "))
print()


# ##################### SORT ##################
# #### Example 1: Sort List ####
#
#
# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos = pos + 1
#     return found
#
#
# lst = [1, 2, 32, 9, 17, 19, 42, 13, 0]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))
# print(seq_search(lst, 2))
# print()
#
# print("#### Sort The List and Search ####")
#
#
# def seq_search(s, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos = pos + 1
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 43]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))
# print(seq_search(lst, 2))
#
# print("#### Binary SEARCH ####")
# print("##### Binary SEARCH Do with Sort List #####")
#
#
# def binary_search(s, item):
#     first = 0
#     last = len(s)-1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2  # 2
#         if s[midpoint] == item:  # 2 == 2
#             found == True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint +1
#
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 43]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))
# print(seq_search(lst, 2))


### Task 1: ###
# from random import randint
# lst = [input("Enter Number:") for i in range(3)]
# print(lst)
# sort_lst = lst.sort()
# def binary_search(s, item):
#     first = 0
#     last = len(s)-1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2  # 2
#         if s[midpoint] == item:  # 2 == 2
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint +1
#
#     return found
#
#
#
# print(binary_search(sort_lst, 3))
# print(binary_search(sort_lst, 13))
# print(binary_search(sort_lst, 2))
#
#
# lst1=sorted([randint(1,99) for i in range(10)])
# ch=int(input('Введите искомое число: '))
# print(lst1)
# def binari_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#     while first <= last and not found:
#         midlpoint = (first + last) // 2  # 4
#         if s[midlpoint] == item:  # 13==3
#             last = midlpoint - 1
#             found = True
#         else:
#             if item < s[midlpoint]:
#                 last = midlpoint - 1
#             else:
#                 first = midlpoint + 1
#     if found:
#         print('Число', item,' присутствует в списке')
#     else:
#         print('Число', item, 'отсутствует в списке')
#
#
# binari_search(lst1, ch)
#
#
# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#     print('Число ', a, 'в списке присутствует')
#
#
# lst = [97, 63, 14, 42, 39, 6, 15, 71, 34, 10]
# a = int(input('Введите число: '))
# binary_search(sorted(lst), a)


# print("Пузырьковая Сортировка - Меньший Элемент Всплывает.")
# import random as r
# import time as t
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#             # print(a)
#         # print("-" * 40)
#
# a = [r.randint(1, 99) for i in range(10)]
#
# # print(a)
# start = t.monotonic()
# bubble(a)
# # print(a)
# res = t.monotonic() - start
# print(round(res,3), "sec")
# print()

### Task 2: ###
### Home Work ###



# print("##### Сортировки СЛИЯНИЕМ #####")
# import random as r
# import time as t
# def merge_sort(a):
#     n = len(a)
#     if n <2:
#         return a
#
#     l = merge_sort(a[:n // 2])
#     r = merge_sort(a[n // 2:n])
#
#     i = j = 0
#     res = []
#
#     while i < len(l) or j < len(r):
#         if not i < len(l):
#             res.append(r[j])
#             j += 1
#         elif not j <len(r):
#             res.append(l[i])
#             i += 1
#         elif l[i] < r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#     return res
#
# # array = [8,2,6,4,5]
# array = [r.randint(1, 99) for i in range(10000)]
# print(array)
# array = merge_sort(array)
# print(array)
# print(round(res,3), "sec")


# print(" Сшотировка ШЕЛЛА.")
#
#
# def shell_sort(s):
#     gap = len(s)
#
#     while gap >0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] >cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2
#         print(gap, "Список: ", s)
#     return(s)
#
#
# a = [10,44,26,14,67,21,9,87]
# print(a)
# shell_sort(a)
# print(a)