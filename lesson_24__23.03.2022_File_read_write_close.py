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
del_str = 2  #int(input('Индекс удаляемого элемента--> '))

if 0 <= del_str < len(rd):
    del rd[del_str]
print(rd)
f.close()

f = open('text2.txt', 'w')
f.writelines(rd)
f.close()

f = open('text2.txt', 'r')
for line in f:
    print(line)
print(f.read())
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
print(f.tell()) # Return Current position of Point.
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

print(" ### Add to CHAR Position the TEXT. 'w+' ")
f = open('text.txt', 'w+')
print(f.write("I am learning Python"))
# print(f.seek(3))
print(f.write("-new string-"))
print(f.tell())
f.close()


### Use Read and Write Together. CONTEXT MANAGER.

# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789'))


# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:6])


### variable = Name File.
# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     # return lt
#     return '  '.join(lt)'
#
# with open('file_name', 'w') as f:
#     f.write(get_line(lst))
#
# # print('Done')
# print(get_line(lst))


#### Task 4 ####
# file_name = 'res_1.txt'
# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
# lst = nums.split('  ')
# print(lst)
# print(len(lst))


# def longest_world(file):
#     with open(file, 'r') as text:
#         w = text.read().split(' ')
#         # print(w)
#         max_length = len(max(w, key=len))
#         # print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         # print(res)
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_world('test3.txt'))
#
# print("Same:")
#
# with open('test3.txt', 'r') as text:
#     # lst = list(map(str,))
#     lst = text.read().split(' ')
#     m = max(len(word) for word in lst)
#     print([i for i in lst if len(i) == m])
