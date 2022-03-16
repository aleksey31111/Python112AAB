import re

### LESSON 22 ###
s = "World2016, PS6, AI5"
print("SOURCE String: " + s)
reg = r'([a-z]+)(\d*)'
reg1 = r'([a-z]+\d*)'
print(re.findall(reg, s, re.I))
print(re.findall(reg1, s, re.I))
print()

print("Поиск IP Адреса")
# 192.168.255.255 или 192.168.0.1
s1 = '127.0.0.1'
reg2 = r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'
reg3 = r'(?:\d{1,3}.){3}(?:\d{1,3})'
print(re.findall(reg2, s1))
print(re.findall(reg3, s1))

print(" Method")
s2 = "5 + 7*2 - 4"
reg4 = r'\s*([+*-])\s*'
print(re.split(reg4, s2))

#### Task 1: ####
print("Task 1: ")
s3 = "01-08-2021"
# p = r"(?:)([^00][1"
p = r"([0][1-9]|[12][0-9]|[3][01])-([0][1-9]|[1][0-2])-([1][9][0-9]|[2][0][0-9][0-9])"
print(re.findall(p, s3))

print("### Continue Lesson ###")
s4 = "Я ищу совпадения в 2021 году. И я их обязательно найду"
reg5 = r'([0-9]+)\s(\D+)'
print(re.search(reg5, s4).group())
m = re.search(reg5, s4)
print("Найденная Строка: ", m[0])
print("Найденная Строка: ", m[1])
print("Найденная Строка: ", m[2])
print(re.findall(reg5, s4))
print(re.findall(reg5, s4)[0])
print()

text = """
Самара
Москва
Тверь
Уфа
Казань
"""
count = 0


def repl_find(m):
    global count
    count += 1
    return f"<option value='{count}'>{m.group(1)}</option>"


print(re.sub(r"\s*(\w+)\s*", repl_find, text))

print("Find Image. Call () = Number Bracket.")
s6 = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
reg6 = r'<img\s+[^>]*src=[\'"](.+)[\'"]>'
reg7 = r'<img\s+[^>]*src=([\'"])(.+)\1>'
print(re.findall(reg6, s6))
print(re.findall(reg7, s6))

print("(?P<name>....) (?P=name)")
print("Find Image. Call () = Number Bracket.")
s7 = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
reg8 = r'<img\s+[^>]*src=(?P<q>[\'"])(.+)(?P=q))>'
#####reg7 = r'<img\s+[^>]*src=([\'"])(.+)\1>'
print(re.findall(reg6, s6))
print(re.findall(reg7, s6))

print("Cont Less")
s8 = "Самолет прилетфет 10/23/2021. Будем рады вас видеть после 10/24/2021."
# reg9 = r'\d{2}/\d{2}/\d{4}'
reg10 = r'(\d{2})/(\d{2})/(/d{4})'
# print(re.sub(reg9, r"\2. \1. \3", s8))
print(re.sub(reg10, r"\2. \1. \3", s8))

print("Search ADDRESS")
s11 = "google.co and google.ru"
reg11 = r'(([a-z0-9]{2,}\.)+[a-z]{2,4})'
print(re.sub(reg11, r"http://\1", s11))

print("РЕКУРСИЯ - Вызов Функции САМОЙ СЕБЯ")


def elevator(n):
    if n == 0:
        print("Вы в Подвале")
        return
    print("=> ", n)
    elevator(n - 1)  # 5 4 3 2 1
    print(n, end=" ")


# n1 = int(input("На каком Вы Этаже: "))
n1 = 5
elevator(n1)

print("Introduction  RECURSION")


def sum_list(lst):
    res = 0
    for i in lst:
        res += 1
    return res


print(sum_list([1, 3, 5, 7, 9]))  # 25


def sum_list(lst):
    if len(lst) == 1:
        print(lst, "=> lst[0]: ", lst[0])
        return lst[0]  # 9
    else:
        print(lst, "=> lst[0]: ", lst[0])
        return lst[0] + sum_list(lst[1:])  # 1 3 5 7


print(sum_list([1, 3, 5, 7, 9]))


##### Function Nam + System Enumeration. ######
def to_str(n, base):  # (365,10) (36, 10) (3,10)
    convert = "0123456789"
    if n < base:
        return convert[n]  # 3 -> 6 -> 5
    else:
        return to_str(n // base, base) + convert[n % base]


print(to_str(365, 10))

print("###Confert 16")


def to_str(n, base):  # (15,16)
    convert = "0123456789ABCDEF"
    if n < base:
        return convert[n]  # FF
    else:
        return to_str(n // base, base) + convert[n % base]  # 15


print(to_str(255, 16))

print("###### NESTED LIST########### Recursion")
names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
print(names[0])
print(type(names[0]) == list)
print(isinstance(names[0], list))
print(names[1])
print(isinstance(names[1], list))
print(names[1][1])
print(isinstance(names[1][1], list))
print(names[1][1][0])
print(isinstance(names[1][1][0], list))

print("Recursion Обход")

names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']


def count_items(lst):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += count_items(item)
        else:
            count += 1
    return count


print(count_items(names))


##### HOME WORK #####
# Поиск в Списке СПИСКОВ Без РЕКУРСИИ.
# ВАЛИДАЦИЯ ТЕЛЕФОНА.