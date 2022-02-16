# ### HW -13 ###
# d = {'name':'Kelly','age':25,'salary':8000,'city':'NewYork'}
# a=dict()
# a['name'] = d.pop('name')
# a['salary'] = d.pop('salary')
#
# #### CONTINUE DICT 2FOR ####
# a={
#     "first":{
#         1:"one",
#         2:"two",
#         3:"three"
#     },
#     "second":{
#         4:"four",
#         5:"five"
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ",a[x][y], sep="")

#### TERM 1 : REGION Of SELL ####
# sell ={'name':['John','Tom','Anne','Fiona'],'partOfEarse':['N':'valueOfSell','S':'valueOfSell','E':'valueOfSell','N':'valueOfSell']}
# sales = {
#     "John":{"N":2056,"S":8463,"E":8441,"N": 2694}
#     "Tom":{"N":2056,"S":8463,"E":8441,"N": 2694}
#     "Anne":{"N":2056,"S":8463,"E":8441,"N": 2694}
#     "Fiona":{"N":2056,"S":8463,"E":8441,"N": 2694}
# }
# l = input('Введите имя продавца:')
# p = input('Введите регион: ')
#
# for i in sales:
#     print(i)
#     for y in sales[i]:
#         print("\t", y, ": ",a[i][y], sep="")

####   ############
# a = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# b = {key: value for key, value in a.items()}
# print(b)
# b = {value: key for key, value in a.items()}
# print(b)
# a = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# for i , j in a.items():
#     print(i,j)
# for i in a.keys
#####  Term 2: Вывести 2 ключ: значение  ##
# a = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# b = {key: value for key, value in a.items() if value <= 2}
# print(b)
#
# #####   ######
# a = {i: i * 5 for i in [10, 20, 30, 40]}
# print(a)
# s = [10, 20, 30, 40]
# a = {i: i * 5 for i in s}
# print(a)
# s = "hello"
# a = {i: i * 5 for i in s}
# print(a)
#
# v = int(input("->"))
# s = [10, 20, 30, 40]
# a = {i: v * 5 for i in s}
# print(a)


##### Get DICT Via FOR ###
# figure = {1: 'Rectangle', 2: 'Triangle', 3: "Circle"}
#
# print(list(figure))
# print(list(figure.values()))
# print(list(figure.items()))

# ####### Term 3: ######
# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four, -20"]
# # lst=[[["one"]:[1,2,3],["two"]:[10,20],]]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

######### ZIP ######
# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# f = {k: v for k, v in zip(b, a)}
# print(f)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# c = [4.0, 5.0, 6.0]
# z = zip(a,b,c)
# z = zip(a,b)

# print(list(zip(range(5), range(100))))
# print(list(zip(range(2, 15), range(100))))

#### Unpack DICT ###
# a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# b = {'a': 11, 'b': 22, 'c': 33, 'd': 44, 'e': 55}
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, "-->", v1)
#     print(k2, "-->", v2)

#### Unpack TUPLE ####
# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

#
# a = ['b', 'c', 'a', 'd']
# b = [3, 2, 1, 4]
# data = list(zip(a, b))
# print(data.sort())
# print(data)
# data1 = list(zip(b, a))
# data1.sort()
# print(data1)
# data2 = sorted(zip(b, a))


##### Term 4 ###### Прибыль по месяцам
# month = ["January", "February", "March"]
# total_sales=[52000.00,51000.00,48000.00]
# production_cost = [46000.00,45900.00,43200.00]
# for sales, cost, m in(zip(total_sales,production_cost,month)):
#     res = sales - cost
#     print("Общая прибыль в", m, "=",res)

#
# one={'apple':0.04,'orange':0.35,'a':0.53, 'pepper':0.53}
# two={'pepper':0.20,'onion':0.55}
# print({**two,**one})
# # print(dict(**two,**one))
# for k, v in {**two,**one}.items():
#     print(k, '->', v)


###################### ENUMERATE ################
# colors = ["red", 'green', 'blue']
# ind = 1
# for color in colors:
#     print(str(ind) + ") " + color)
#     ind += 1
# print()
# for i, color in enumerate(colors, 1):
#     print(str(i) + ") " + color)
# print()
# for color, i in enumerate(colors, 1):
#     print(i,") ",color)

#
# d = {0: 1, 1: 2, 2: 3, 3: 4}
# for i, j in enumerate(d):
#     print(i, ": ", j, sep="")
#
#     d = {0: 1, 1: 2, 2: 3, 3: 4}
#     for i, j in enumerate(d):
#         print(i, ": ", j, sep=:)
#
#         d = {
#             1: {"a": 1, "b": 2, "c": 3, "d": 4},
#             2: {"a": 10, "b": 20, "c": 30, "d": 40},
#         }
#         for i, k in enumerate(d, 1):
#             print(i, ") key=", k, ", value=", d[k], sep="")
#
#         num = [1, 2, 3, 4, 5]
#         itr = iter(num)
#         print(next(itr))
#         print(next(itr, "STOP"))
#         print(next(itr, "STOP"))
#
#         a = [6, 7, 3, 4, 1, 5]
#         b = enumerate(a)
#         c = next(b)
#         c1 = next(b)
#         print(c)
#         print(c1)
#         print(type(c))
