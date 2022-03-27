print("### Lesson 24 ###")
print("#### Work With File ####")
f = open('text.txt', 'r')  # Relative PATH.
# f = open(r'I:\PythonCours\Python\pythonProject\text.txt', 'r')  # Full PATH

print("AUXULIARY Commands:")
print()
print(f"Output File Contain: print(*f) {print(*f)}")
print()
print(f"DATA about Current File: print(f) {print(f)}")
print()
print(f"Boolearn Value. Open yet File: print(f.closed) {print(f.closed)}")
print()
print(f"MODE Opening File w,r,x/: print(f.mode) {print(f.mode)}")
print()
print(f"Name FILE That Opening: print(f.name) {print(f.name)}")
print()
print(f"Coding of Character in the File that Opening: print(f.encoding) {print(f.encoding)}")
print()
print()

print("Method Of Work with FILE: ")
print("1) Method f.read(): ")
f = open(r'I:\PythonCours\Python\pythonProject\text.txt', 'r')  # Full PATH
# print(f.read())
print(f.read(3))
print(f.read())
print()
print("Method f.close()")
f.close()
print()

print("Использование 'try ... finaly'\n \
      Если Файл не Открывается при Повреждении ФАЙЛА. 'No such file or directory'.")
f = open(r'I:\PythonCours\Python\pythonProject\text.txt', 'r')  # Full PATH
try:
    print(f.read())
finally:
    f.close()
print()

print("Read File By Line:")
f = open(r'I:\PythonCours\Python\pythonProject\test.txt', 'r', encoding="utf8")
print(f.readline())
print(f.readline(8))
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

f.close()

f = open(r'I:\PythonCours\Python\pythonProject\test.txt', 'r', encoding='utf8')
# print(f.readline())
print(f.readline(21))
print(f.readline(5))
f.close()

f = open(r'I:\PythonCours\Python\pythonProject\test.txt', 'r', encoding="utf8")
print(f.readlines(500))
f.close()

f = open(r'I:\PythonCours\Python\pythonProject\test.txt', 'r', encoding="utf8")
print(f.readlines())
f.close()

print("FOREAECH By Read text File.")
f = open(r'I:\PythonCours\Python\pythonProject\test.txt', 'r', encoding='utf8')
for line in f:
    print(line)
f.close()

#### Task 1 ####
print("Задание 1 Урока 24:\n \
      Посчитать Количество СТРОК в Файле.")
print("Variant 1 Task 1 Lesson 24:")
f = open('Task1.txt', 'r')
count1 = len(f.readlines())
print(count1)
f.close()
print()

print("Variant 2 Task 1 Lesson 24. NOT Correct:")
f = open('test.txt', 'r', encoding='utf8')
for line in f:
    count = len(f.readlines())
    print(count)
f.close()
print()

print("Variant 3 Task 1 Lesson 24:")
f = open('text.txt', 'r')
c = 0
for line in f:
    # print(line)
    c += 1
print(c)
f.close()
print()
print()

print("### Continue Lesson: ###")
print("Запись в  Файл: write('file, 'w")
f = open('xyz.txt', 'w')
f.write('Hello\nWorld!')
f.close()
f = open('xyz.txt', 'r')
print(f.read())
f.close()
print()
print("Добавление Записи в Файл: f.write(file, 'a')")
f = open('xyz.txt', 'a')
print(f.write(' New text'))
f.close()
f = open("xyz.txt", "r")
print(f.read())
f.close()
print()

print("Построчная Запись: writelines(lines)")
f = open('xyz.txt', 'a')
lines = ['. This is line 1. ', 'This is line 2.']
print(f.writelines(lines))
f.close()
f = open("xyz.txt", "r")
print(f.read())
f.close()
print()

print("Дозапись Данных: С Помощью Метода write в Цикле for() ")
f = open('xyz.txt', 'a')
lst = [str(i) for i in range(1, 20)]
print(lst)
for i in lst:
    f.write(i + "\t")
f.close()
f = open("xyz.txt", "r")
print(f.read())
f.close()

### Task 2 ###
print("Задание 2 Урока 24: Заменить СТРОКУ в Текстовом ФАЙЛЕ в ТЕКСТЕ:\n \
      Замена строки в текстовом файле;\n \
      Измнить строку в списке;\n \
      Записать список в файл;")
print("1 Open.")
task2 = "Замена строки в текстовом файле;\nИзменить строку в списке;\nЗаписать список в файл;"
f = open("Task2.txt", "w")
f.write(task2)
f.close()

# f = open("Task2.txt", "r")
# print(f.read())
# f.close()

# f = open('Task2.txt', 'w')
# 'Task2.txt'.replace('Измнить строку в списке;\n', 'Hello WORLD!\n \\')
# f.close()
# f =open("Task2.txt", 'r')
# print(f.readlines())
# f.close()

print("2 Open.")
f = open('Task2.txt', 'r')
rd = f.readlines()
print(rd)
for i in range(len(rd)):
    if rd[i] == "Изменить строку в списке;\n":
        rd[i] = "Hello World!\n"
print(rd)
f.close()

print("3 Open.")
f = open("Task2.txt", "w")
f.writelines(rd)
f.close()

print("4 Open.")
f = open("Task2.txt", "r")
for line in f:
    print(line)
f.close()

### Task 3 ###
print("Задание 3: Удаление СТРОКИ Из ФАЙЛА По ЕЕ Индексу в ТЕКСТЕ:\n\
      Замена строки в текстовом файле;\n \
      Измнить строку в списке;\n \
      Записать список в файл;")
print("Variant 1")
f = open('Task3.txt', 'w')
f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
f.close()

f = open('Task3.txt', 'r')
rd = f.readlines()
print(rd)
print()
del_str = 2  # int(input('Индекс удаляемого элемента--> '))

if 0 <= del_str < len(rd):
    del rd[del_str]
else:
    print("Индекс Введен Не Верно.")
print(rd)
f.close()

f = open('Task3.txt', 'w')
f.writelines(rd)
f.close()

f = open('Task3.txt', 'r')
for line in f:
    print(line)
# print(f.read())
f.close()

# print("Variant 2")
# print("Open 1")
# f = open("Task3.txt", 'w')
# f.write = "Замена строки в текстовом файле;\nИзменить строку в списке;\nЗаписать список в файл;"
# f.close()
#
# print("Open 2")
# f = open("Task3.txt", "r")
# rd_lines = f.readlines()
# str_del = "2"
# for i in range(len(rd_lines)):
#     if i == str_del:
#         del rd_lines[i]
# f.close()
#
#
#
# print("Open 3")
# f = open("Task3.txt", "w")
# f.writelines(rd_lines)
# f.close()
#
# print("Open 4")
# f = open("Task3.txt", "r")
# print(f.readlines())
# f.close()


##### Aditional Methods Work With File #####
f = open('text.txt', 'r')
print(f.read(3))
print(f.tell())  # Return Current position of Point.
print(f.seek(1))  # Move the Point to Get Position.
print(f.read())
print(f.tell())
f.close()
print()

print(" ### Add to CHAR Position the TEXT. 'r+' ")
f = open('text.txt', 'r+')
print(f.write("I am learning Python"))
print(f.seek(3))
print(f.write("-new string-"))
print(f.tell())
f.close()
f = open("text.txt", "r")
print(f.read())
f.close()
print()

print(" ### Add to CHAR Position the TEXT. 'w+' ")
f = open('text.txt', 'w+')
print(f.write("I am learning Python"))
# print(f.seek(3))
print(f.write("-new string-"))
print(f.tell())
f.close()
f = open("text.txt", "r")
print(f.readlines())
f.close()
print()

print("### Use Read and Write Together. CONTEXT MANAGER. ###")
print(("SINTAXIS 'with open('text.txt', 'w+') as f:' "))
with open('text.txt', 'w+') as f:
    print(f.write('0123456789'))
with open('text.txt', 'r') as f:
    print(f.readlines())

print("Печать От 0 до 6 СИМВОЛА Строки, Включая 6 Символ.")
with open('text.txt', 'r') as f:
    for line in f:
        print(line[:6])
print()

print("### Single Variable = Name File. ###")
print("Example 1: Convert List to String:")
file_name = 'res_1.txt'
lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
# with open('res_1.txt', 'w') as f:
#     f.write("")
print(f"Source List Float Namber: {lst}")


def get_line(lt):
    lt = list(map(str, lt))
    # return lt
    return '  '.join(lt)


# print(get_line(lst))
with open(file_name, 'w') as f:
    f.write(get_line(lst))

print('Done Example 1. ')
print(f"Out List Of String In The FILE from List Float Namber: {get_line(lst)}")
# print(get_line(lst))
print()

#### Task 4 ####
print("Задание 4: В Текстовом ФАЙЛЕ Хранятся ВЕЩЕСТВЕННЫЕ ЧИСЛА.\n\
      Вывести Их На Экран и Вывести Их Количество.")
print("Variant 1")
file_name = 'res_2.txt'
lst2 = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
print(f"Source List: {lst2}.")


# with open(file_name, 'r') as f:
#     nums = f.read()


def get_list_for_res_2(lt):
    lt = list(map(str, lt))
    # return lt
    return '   '.join(lt)


with open(file_name, 'w') as f:
    f.write(get_list_for_res_2(lst2))

with open(file_name, 'r') as f:
    print(f"Get file 'res_2.txt' {f.readlines()}")

with open(file_name, 'r') as f:
    nums = f.read()

print(nums)
lst = nums.split('   ')
print(lst)
print(len(lst))

print("Variant 2")
file_name = 'res_1.txt'
with open(file_name, 'r') as f:
    nums = f.read()
print(nums)
lst = nums.split('  ')
print(lst)
print(len(lst))

#### Task 5 ####
print("Задание 5: Написать Функцию, Которая Выводит СЛОВО Из Файла,\n\
 Имеющее МАКСИМАЛЬНУЮ ДЛИНУ(или СПИСОК СЛОВ Если Таковых Несколько).\n\
 ['методами', 'символов', 'попыткой']")
print()
with open("Task5.txt", 'w', encoding="utf8") as f:
    f.write("Стандартная библиотека включает большой набор полезных\n\
            переносимых функций, начиная с возможностей для работы с\n\
            текстом и заканчивая средствами для написания сетевых\n\
            приложений. Дополнительные возможности, такие как\n\
            математическое моделирование, работа с оборудованием,\n\
            написание веб-приложений или разработка игр, могут\n\
            реализовываться посредством обширного количества\n\
            сторонних библиотек, а также интеграцией библиотек,\n\
            написанных на Си или C++, при этом и сам интерпретатор\n\
            Python может интегрироваться в проекты, написанные на\n\
            этих языках[25]. Существует и специализированный\n\
            репозиторий программного обеспечения, написанного\n\
            на Python, — PyPI[45]. Данный репозиторий предоставляет\n\
            средства для простой установки пакетов в операционную\n\
            систему и стал стандартом де-факто для Python[46].\n\
            По состоянию на 2019 год в нём содержалось более 175\n\
            тысяч пакетов[45].\n\
            Python стал одним из самых популярных языков, он используется\n\
            в анализе данных, машинном обучении, DevOps и веб-разработке,\n\
            а также в других сферах, включая разработку игр.\n\
            За счёт читабельности, простого синтаксиса и отсутствия\n\
            необходимости в компиляции язык хорошо подходит для\n\
            обучения программированию, позволяя концентрироваться\n\
            на изучении алгоритмов, концептов и парадигм.\n\
            Отладка же и экспериментирование в значительной\n\
            степени облегчаются тем фактом, что язык является\n\
            интерпретируемым . [47][25] Применяется язык многими\n\
            крупными компаниями, такими как Google или Facebook[25].\n\
            По состоянию на октябрь 2021 года Python занимает первое\n\
            место в рейтинге TIOBE популярности языков программирования\n\
            с показателем 11,27%[48]. «Языком года» по версии TIOBE\n\
            Python объявлялся в 2007, 2010, 2018 и 2020 годах[49]. ")


def longest_world(file):
    with open(file, 'r', encoding="utf8") as text:
        w = text.read().split()
        # print(w)
        # print("Находим Слово Из Максимального Значение\n\
# Количества Символов в Слове")
        # max_length = max(w, key=len)
        max_length = len(max(w, key=len))
        # print(max_length)
        res = [word for word in w if len(word) == max_length]
        # print(res)
        if len(res) == 1:
            return res[0]
        return res


print(longest_world('Task5.txt'))
print()

print("Same: Task 5, but More LESS")
with open('test3.txt', 'r', encoding="utf8") as text:
    # lst = list(map(str, text.read().split()))
    lst = text.read().split(' ')
    # print(lst)
    m = max(len(word) for word in lst)
    # print(m)
    print([i for i in lst if len(i) == m])
