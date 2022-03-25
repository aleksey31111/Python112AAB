print("### Lesson 24 ###")
print("#### Work With File ####")
f = open('text.txt', 'r')
f = open(r'I:\PythonCours\Python\pythonProject\text.txt', 'r')

print(f.closed)
print(f.open)

# try:
#     print(f.read())
# finally:
#     f.close

# print(f.read(3))
# print(f.read())
# f.close()

# f = open(r'I:\PythonCours\Python\pythonProject\test.txt', 'r')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
#
# f.close()


# f = open(r'I:\PythonCours\Python\pythonProject\test.txt', 'r')
# print(f.readline())
# print(f.readline(21))
# print(f.readline(5))
# f.close()

# f = open(r'I:\PythonCours\Python\pythonProject\test.txt', 'r')
# for line in f:
#     print(line)
# f.close()


#### Task 1 ####
# f = open('Task1', 'r')
# count = len(f.readlines())
# f.close()

### Not Correct @@@
# f = open('test.txt', 'r')
# for line in f:
#     count = len(f.readlines())
#     print(count)
# f.close()

### Correct ###
# f = open('Testtext.txt', 'r')
#
# c=0
# for line in f:
#     print(line)
#     c+=1
# print(c)
# f.close()


# ### Continue Lesson:
# print("ReWrite FIle.")
# f = open('xyz.txt', 'w')
# f.write('Hello\nWorld!')
# f.close()
# print("Write FIle.")
# f = open('xyz.txt', 'a')
# print(f.write('New text'))
# f.close()
#
# f = open('xyz.txt', 'a')
# lines = ['This is line 1', 'This is line 2']
# print(f.writelines(lines))
# f.close()


# f = open('xyz.txt', 'a')
# lst = [str(i) for i in range(1, 20)]
# print(lst)
# for i in lst:
#     f.write(i + '\t')
# f.close()

# f.close()

### Task 2 ###
# f = open('Task2.txt', 'w')
# task2 = "Заменить строки телсеа.\n Hello world.\n Hw"
# f.write(task2)
# f.close()
# # for i in 'Text2.txt':
# f = open('Task2.txt', 'r')
# 'Task2.txt'.replace('Hello world.', 'Hello WORLD')
# f.close()
# f =open("Task2.txt", 'r')
# f.readline()
# f.readline()
# print(f.read())
# f.close()

### Variant 2
# f = open('text2.txt', 'w')
# f.write("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq\n"
#         "qqqqqqqqqqqqqqqqqqqqqqqqqqqq\n"
#         "qqqqqqqqqqqqqqqqqqqqqqqq\n"
#         "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
# f.close()
#
# f = open('text2.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
# f = open('test2.txt', 'r')
# rd = f.readlines()
# f = open('text2.txt', 'r')
# rd = f.readlines()
# # print(rd)
# for i in range(len(rd)):
#     if rd[i] == "изменить строку в списке;\n":
#         rd[i] = "Hello World\n"
# # print(rd)
# f.close()
#
# f = open('text2.txt', 'r')
# # for line in f:
# #     print(line)
# print(f.read())
# f.close()
# f = open ( 'text2.txt' , 'w' )
# #f. write...,
#
# f = open('text2.txt', 'w')
# f.writelines(rd)
# f.close()

### Task 3 ###
# f = open("Task3", 'w')
# f.write("Замена строки в текстоыом файле;"
#         "Изменитьстроку в спимке;"
#         "записать спимок в файл;")


### Variant 2
# f = open('text2.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open('text2.txt', 'r')
# rd = f.readlines()
# print(rd)
# print()
# sitr=int(input('Индекс удаляемого элемента--> '))
# try:
#     for i in range(len(rd)):
#         if sitr==i:
#             del rd[i]
# finally:
#     print("Введите нужный индекс")
# print(rd)
# print()
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(rd)
# f.close()
#
# f = open('text2.txt', 'r')
# for line in f:
#     print(line)
# print(f.read())
# f.close()


### Variant 3
# f = open('text2.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open('text2.txt', 'r')
# rd = f.readlines()
# print(rd)
# print()
# sitr=int(input('Индекс удаляемого элемента--> '))
#
# # for i in range(len(rd)):
# if 0 <= sitr < len(rd):
#     # if sitr==i:
#     del rd[sitr]
# print(rd)
# print()
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(rd)
# f.close()
#
# f = open('text2.txt', 'r')
# for line in f:
#     print(line)
# print(f.read())
# f.close()

##### Aditional Methods Work With File #####
# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell()) # Return Current position of Point.
# print(f.seek(1))  # Move the Point to Get Position.
# print(f.read())
# print(f.tell())
# f.close()

# ### Add to Position the TEXT.
# f = open('text.txt', 'r+')
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()
#
# f = open('text.txt', 'w+')
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()


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