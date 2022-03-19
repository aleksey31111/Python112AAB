import re

### LESSON 22 ###
print("Продолжение Регулярные Выражения SPLIT(), FINDALL(), SEARCH().GROUP(), SUB()")
print()
print("Находим ЧИСЛОВЫЙ и СТРОКОВЫЕ Значения: Используя КРУГЛЫЕ СКОБКИ:")
s = "World2016, PS6, AI5"
print("SOURCE String: " + s)
reg = r'([a-z]+)(\d*)'
reg1 = r'([a-z]+\d*)'
print("Несколько КРУГЛЫХ СЕОБОК.")
print(re.findall(reg, s, re.I))
print("Одни КРУГЛЫЕ СКОБКИ.")
print(re.findall(reg1, s, re.I))
print()

print("Поиск  ЛОКАЛЬНОГО IP Адреса")
# 192.168.255.255 или 192.168.0.1
s1 = '127.0.0.1'
reg2 = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
print(re.findall(reg2, s1))
reg3 = r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'
print(re.findall(reg3, s1))
print("Используем Сохраняющие СКОБКИ: ()")
reg4 = r'(\d{1,3}.){3}(\d{1,3})'
print(re.findall(reg4, s1))
print("Используем НЕ Сохраняющие КРУГЛЫЕ СКОБКИ: (?:)")
reg5 = r'(?:\d{1,3}.){3}(?:\d{1,3})'
print(re.findall(reg5, s1))
print()

print(" Method SPLIT(pat, str, количество_Разбиения_СТРОКИ) - Для Разбиения СТРОКИ По Заданномк ШАБЛОНУ.")
s2 = "5 + 7*2 - 4"
print("Получение ТОЛЬКО Цифр:")
reg6 = r'[+*-]'
print(re.split(reg6, s2))
reg7 = r'[(+*\-)]'
print(re.split(reg7, s2))
reg8 = r'\s*[+*-]\s*'
print(re.split(reg8, s2))
print("Получение Цифр и Знаков ОПЕРАЦИИ:")
reg9 = r'\s*([+*-])\s*'
print(re.split(reg9, s2))
print()
print()

# #### Task 1: ####
print("Task 1: Попросите пользователя Ввести Текущую ДАТУ \n \
По Заданному ШАБЛОНУ и Проверте ДАННЫЕ На Соответствин.")
s3 = "29-08-2021"
# s10 = input("Введите ДАТУ (Через ДЕФИС): ")
p = r'(\d\d)-(\d\d)-(\d\d\d\d)'
print("Правильный Вариант: ", re.findall(p, s3))
p1 = r'\d+'
print("Правильный Вариант: ", re.findall(p1, s3))
p2 = r"(?:[\d]{2}[-]){2}(?:\d){4}"
print("Неправильный Вариант: ", re.findall(p2, s3))
p3 = r"(?:[\d]{2}[-]){2}(?:\d){4}"
print("Неправильный Вариант; ", re.findall(p3, s3))
p4 = r"([0][1-9]|[12][0-9]|[3][01])-([0][1-9]|[1][0-2])-(19[0-9]|20[0-9][0-9])"
print("Правильный Вариант: ", re.findall(p4, s3))
s3_1 = "10-12-1921"
p5 = r"([0][1-9]|[12][0-9]|[3][01])-([0][1-9]|[1][0-2])-([1][9][0-9][0-9]|[2][0][0-9][0-9])"
print("Правильный Вариант: ", re.findall(p5, s3_1))

print()
print()

print("### Continue Lesson ###")
print("Отличия Методов findall(pat, str, find_num) И search(pat, str).Metod")
s4 = "Я ищу совпадения в 2021 году. И я их обязательно найду"
reg10 = r'([0-9]+)\s(\D+)'
print(re.search(reg10, s4).group())
reg11 = r'(\d+)\s(\D+)'
print(re.search(reg11, s4).group())
m = re.search(reg10, s4)
print("Найденная Строка: ", m[0])
print("Найденная Цифры: ", m[1])
print("Найденная Буквы: ", m[2])
print(re.findall(reg10, s4))
print(re.findall(reg11, s4)[0])
print()

print("Работа с html 'Option'")
print("Вызов Функции repl_find(m), Методом sub(old_str or pat, new Value, str) \n \
      которая Возвращает <f\"<option value='{count}'>{m.group(1)}</option>\">")
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
print()
print()

print("Find Image. Call () = \\(Number Bracket).")
s5 = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
reg4 = r'<img\s+[^>]*alt\s*=\s*[\'"].+[\'"]>'
print(re.findall(reg4, s5))
reg5 = r'<img\s+[^>]*alt\s*=\s*([\'"])(.+)\1'  # src=[\'"](.+)[\'"]>'
print(re.findall(reg5, s5))
s6 = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
reg6 = r'<img\s+[^>]*src=[\'"](.+)[\'"]>'
print(re.findall(reg6, s6))
reg7 = r'<img\s+[^>]*src=([\'"])(.+)\1>'
print("Обращение к НОМЕРУ: ", re.findall(reg7, s6))
print("(?P<name>....) (?P=name) - Обращение к ИМЕНИ")
reg8 = r'<img\s+[^>]*src=(?P<name>[\'"])(.+)(?P=name)>'
print(re.findall(reg8, s6))
print()

# print("Find Image. Call () = Number Bracket.")
# s7 = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg8 = r'<img\s+[^>]*src=(?P<q>[\'"])(.+)(?P=q))>'
# #####reg7 = r'<img\s+[^>]*src=([\'"])(.+)\1>'
# print(re.findall(reg6, s6))
# print(re.findall(reg7, s6))
#
print("Меняем Написание ДАТЫ с mm/dd/yyyy на dd/mm/yyyy")
s8 = "Самолет прилетает 10/23/2021. Будем рады вас видеть после 10/24/2021."
print("Source STRING: ", s8)
reg9 = r'\d{2}/\d{2}/\d{4}'
print(re.sub(reg9, r"", s8))
reg10 = r'(\d{2})/(\d{2})/(\d{4})'
print(re.sub(reg10, r"\2.\1.\3", s8))
print(re.sub(reg10, "\\2.\\1.\\3", s8))
print()
print()

print("Search ADDRESS google.com  И  google.ru, Делая Их Запускающимися.")
s9 = "google.com and google.ru"
reg11 = r'(([a-z0-9]{2,}\.)+[a-z]{2,4})'
print(re.sub(reg11, r"http://\1", s9))
reg12 = r'((\w{2,}\.)+[a-z]{2,4})'
print(re.sub(reg12, r"https://\1", s9))
print()
print()
print()

print("##########################################################")
print("########### РЕКУРСИЯ - Вызов Функцией САМОЙ СЕБЯ #########")
print("##########################################################")

print("Понимание РЕКУРСИИ на Примере Функции.")


def elevator(n):
    if n == 0:
        print("Вы в Подвале")
        return
    print("=> ", n)
    elevator(n - 1)  # 5 4 3 2 1
    print(n, end=" ")


# # n1 = int(input("На каком Вы Этаже: "))
n1 = 5
elevator(n1)
print()

print("Introduction  RECURSION")
print("Обычное Нахлждение СУММЫ: Элементов СПИСКА sum_list([1, 3, 5, 7, 9])")


def sum_list(lst):
    res = 0
    for i in lst:
        res += i
    return res


print(sum_list([1, 3, 5, 7, 9]))  # 25
print()

print("РЕКУРСИВНОЕ Нахождение СУММЫ.")


def sum_list(lst):
    if len(lst) == 1:
        print(lst, "=> lst[0]: ", lst[0])
        return lst[0]  # 9
    else:
        print(lst, "=> lst[0]: ", lst[0])
        return lst[0] + sum_list(lst[1:])  # 1 3 5 7


print(sum_list([1, 3, 5, 7, 9]))
print()
print()

print("#####################################################################################")
print(" ##### Function Nam = NUMBER Conversion between different CALCULATION SYSTEM. ###### ")
print("#####################################################################################")
print("Decimal CALCULATION SYSTEM.")


def to_str(n, base):  # (365,10) (36, 10) (3,10)
    convert = "0123456789"
    if n < base:
        return convert[n]  # 3 -> 6 -> 5
    else:
        return to_str(n // base, base) + convert[n % base]  # 5 6


print("Преобразование Числа '365' в ДЕСЯТИЧНКЮ Систему Исчисления:", to_str(365, 10))
print("Преобразование Числа '10' в ДВОИЧНУЮ Систему Исчисления:", to_str(10, 2))
print("Преобразование Числа '8' в ДВОСМЕРИЧНУЮ Систему Исчисления:", to_str(8, 8))

print("### Hex CALCULATION SYSTEM.")


def to_str(n, base):  # (255//16=15)
    convert = "0123456789ABCDEF"
    if n < base:
        return convert[n]  # FF
    else:
        return to_str(n // base, base) + convert[n % base]  # 15-1-ОстатокОтДеления


print("Преобразование Числа '255' в ШЕСТНАДЦАТЕРИЧНУЮ Систему Исчисления:", to_str(255, 16))

print("### Octo CALCULATION SYSTEM.")


def to_str(n, base):  # (15,16)
    convert = "01234567"
    if n < base:
        return convert[n]  # FF
    else:
        return to_str(n // base, base) + convert[n % base]


print(to_str(8, 8))

print("### Binary CALCULATION SYSTEM.")


def to_str(n, base):
    convert = "01"
    if n < base:
        return convert[n]
    else:
        return to_str(n // base, base) + convert[n % base]


print(to_str(10, 2))
print()

print("################################################################")
print("###### Recursive Traversal of a NESTED LIST ########### Recursion")
print("################################################################")
names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
print(names[0])
print(type(names[0]) == list)
print(isinstance(names[0], list))
print(names[1])
print(isinstance(names[1], list))
print(names[1][1])
print(isinstance(names[1][1], list))
print(names[1][1][1])
print(isinstance(names[1][1][0], list))
print()

print("Recursion Bypass")
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

# ##### HOME WORK #####
# # Поиск в Списке СПИСКОВ Без РЕКУРСИИ.
# # ВАЛИДАЦИЯ ТЕЛЕФОНА.
