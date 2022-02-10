# ### Continue Corteg ####
# t =(10, 11, [1, 2, 3], [4, 5, 6], ["hellow", "world"])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append('hello')
# print(t, id(t))
#

# def func(ls):
#     empty = []
#     for i in ls:
#         if i not in empty:
#             empty.append(i)
#     print(empty)
#     return (reversed(empty))
#
#
# print(func([1, 2, 3, 3, 2]))
# print(func(2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0))

# def func(s):
#     ls = []
#     [ls.append(i) for i in reversed(s) if i not in ls]
#
#
# print(func([1, 2, 3, 3, 2]))
# print(func(2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0))


# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z) # Распаковка Кортежа
#
# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# n,a,i = user
# print(n, a, i)


# t = (1, 2, 3)
# print(t)
# # del t[0]
# del t

# lst = [1, 2, 3,4,5]
# print(type(lst))
# print(lst)
# tp = tuple(lst)
# print(type(tp))
# print(tp)
# lst = list(tp)
# ...


# countries = (
#     ("Germany", 80.2, (("Berlin", 3.326), ("Gambutg", 1.718))), ("France", 80.2, (("Parzh", 3.326), ("Marsel", 1.718)))
# )
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "Население =", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород:", city_name, "Население =", city_population)

#################### МНОЖЕСТВО - SET №№№№№№№№№№№№№№№№№№№№№№№№№№№
# s = {1, 2, 1, 2, 3, 2, 3}
# print(type(s))
# print(s)
# print(len(s))
#
# a = set()
# print(type(a))
# a = set("hello")
# print(a)
# a = set(123)
# print(a)
#
# c = ["hello", "hi", "hi"]
# a = set(c)
# print(a)


############# GENERATOR SET #########
# s = {x for x in range(10) if x % 2 == 0}
# print(s)
# print(list(s))

# def to_set(x):
#     a = set(x)
#     # b = len(a)
#     return a, len(a)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t= {"red","green","blue"}
# print("green" not in t)
# for i in t:
#     print(i, end=" ")

##### CONDITIONS INONE STRING ################
# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' in i}
# print(a)
# a = {'A' + i[1:] if i[0] == 'A' else "B" + i[1:] for i in r if i[1] == 'c'}
# print(a)

############### CHANGE SET ##############
# a = {0, 1, 2, 3}
# a.add(4)
# print(a)
# num = 2
# if num in a:
#     a.remove(num)
# print(a)
#
# a.discard(6)
# print(a)
#
# a.pop()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c= a.union(b)
# c = a | b
# print(c)
# a |= b
# print(a)
# c = a & b
# print(c)
# a &= b
# print(c)
# c = a - b
# print(c)
# a ^= b
# print(a)
# a <= b
# print(a)
# a < b
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# res1 = s1 ^ s2 ^ s3 ^ s4 ^ s5 ^ s5 ^ s7
# print(res1)
# res2 = max(res1)
# res3 = min(res1)
# print(res2)
# print(res3)


str1 = 'Hello'
str2 = 'How are you'
res = set(str1) & set(str2)
for i in res:
    print(i, end=" ")
