### Lesson 25: 28 Marth 2022 yers. ###
### Work with Several File with Replace:
# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия - ")
#         fw.write(line)


### Work with 'Path' and 'Directory' ###
### Moduls: os, os.path ###

import os
# print("Тукущая директория: ", os.getcwd())
# print(os.listdir())
# print(os.listdir(".."))
# print(os.listdir(".idea"))
# os.mkdir("folder")  # Создает Директорию по Указанному Пути.
# os.makedirs("nested1/nested2/nested3")  # сОЗДАЕТ НАБОР ВЛОЖЕННЫХ ДИРЕКТОРИЙ ПО УКАЗАННОМУ ПУТИ
# os.remove("xyz.txt") # уДАЛЯЕТ фАЙЛ.
# os.rename("nested1", "test")  # Переименовывает папку
# os.rename("test.txt", "test/test1.txt")
# os.renames("text.txt", "text/text1.txt")
# os.rmdir("folder")
# os.rmdir("text")


# for root, dirs, files in os.walk('nested1', topdown=False):
#     print("Root: ", root)
#     print("Subdirs: ", dirs)
#     print("Files: ", files)

for root, dirs, files in os.walk('Work2', topdown=False):
    print("Root: ", root)
    print("Subdirs: ", dirs)
    print("Files: ", files)


for root, dirs, files in os.walk('Work'):
    if not os.listdir(root):
        os.rmdir(root)
        print(f"Директория {root} удалена.")
import os
import os.path

# /home/Work/test.txt - linux, Mac
# D:\Python112\Work\F5
#
print(os.path.split(r"i:\PythonCours\Python\pythonProject\Work2\F5\1.txt"))
# print(os.path.split(r"i:\PythonCours\Python\pythonProject\Work2\F5"))
# print(os.path.split(r"i:\PythonCours\Python\pythonProject\Work2\F5")[0])
# print(os.path.split(r"i:\PythonCours\Python\pythonProject\Work2\F5")[1])
# print(os.path.split(r"i:\PythonCours\Python\pythonProject\Work2\F5\1.txt")[0])
# print(os.path.split(r"i:\PythonCours\Python\pythonProject\Work2\F5\1.txt")[1])
#
print(os.path.dirname(r"i:\PythonCours\Python\pythonProject\Work2\F5\1.txt"))
# print(os.path.basename(r"i:\PythonCours\Python\pythonProject\Work2\F5\1.txt"))
#
# print(os.path.join(r"i:\PythonCours\Python\pythonProject", "Work2", "F5", "1.txt"))

#### Task 2 ####
### Create Folders with Files. ###
# dirs = ['Work/F1', 'Work/F2/F21']
# for d in dirs:
#     os.makedirs(d)
#
# files = {
#     'Work': ['w.txt'],
#     'Work/F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     'Work/F2/F21': ['f211.txt', 'f212.txt']
# }
#
# for d, fl in files.items():
#     for file in fl:
#         file_path = os.path.join(d, file)
#         open(file_path, 'w').close()
#         print(file_path)
#         print()


# print("### wALK OFF Dir")
# file_with_text = ['Work/w.txt', 'Work/F1/f12.txt', 'Work/F2/F21/f211.txt', "Work/F2/F21/f212.txt"]
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f"some sample text for {file} FILE")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("*" * 40)
#
#
# print_tree("Work", topdown=False)
# print_tree("Work", topdown=True)


### wALK OFF reverse ###
# file_with_text=['Work/w.txt', 'Work/F1/f12.txt','Work/F2//F21/f211.txt', 'Work/F2/F21/f212.txt']
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f'some sample text for {file} file')
#     for root, dirs, files in os.walk('Work', topdown=False):
#         print('Root: ', root)
#         print('Subdirs: ',dirs)
#         print('Files: ', files)
#         print()
#     for root, dirs, files in os.walk('Work', topdown=True):
#         print('Root: ', root)
#         print('Subdirs: ',dirs)
#         print('Files: ', files)
#         print()

# print("Varificate Exists file")
# print(os.path.exists(r"i:\PythonCours\Python\pythonProject\Work"))
# print("Get Size of Bites")
# print(os.path.getsize("i:\PythonCours\Python\pythonProject\Work/F1/f12.txt"))
# # Last Access To File.
# print(os.path.getatime('i:\PythonCours\Python\pythonProject\Work/F2//F21/f211.txt'))
# # Last Modified File
# print(os.path.getmtime('i:\PythonCours\Python\pythonProject\Work/F2//F21/f211.txt'))
# # Time Created File
# print(os.path.getctime('i:\PythonCours\Python\pythonProject\Work/F2//F21/f211.txt'))
#
# import time
#
# path = r"i:\Musik\Alisa\Sound\#10_Seychas pozdnee chem ti dumaesh (2003g.)\#10_02_Nebo slavyan.mp3"
# size = os.path.getsize(path)
# ksize = size // 1024
# print(f"Размер {ksize} Kb")
#
# c = os.path.getctime(path)
# b = time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c))
# # time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime())
# print(b)
#
# print("Task 4:")
# n_f = "i:\PythonCours\Python\pythonProject\lesson_24__23.03.2022_File_read_write_close.py"
# if os.path.exists(n_f):
#     d, name = os.path.split(n_f)
#     a = os.path.getctime(n_f)
#     print(f"{name} ({d}) - last access time {a} sec")
#
# else:
#     print(f"File {n_f} Not Found")
# print("Name File: ", n_f[-46:])
# print("Dirs name: ", n_f[-20:-10])
# print(os.path.getatime(n_f))

#### Variant 2 ####
# a = input("Введите имя файла: ")
# ok = os.path.exists(a)
# if ok:
#     name = os.path.basename(a)
#     print(name)
#     print(os.path.dirname(a))
#     tim = os.path.getatime(name)
#     b = time.strftime("%d.%M.%Y %H:%M:%S", time.localtime(tim))
#     print(b)
# else:
#     print("Такого файла нет")

#### Variant 3 ####
# if os.path.exists(str2):
#     for root, dirs, files in os.walk(str2):
#         print(files, dirs, root, ' - ', os.path.getctime(str2))
# else:
#     print("Not")



### Continue Lesson ###
# print(os.path.isfile(r'i:\PythonCours\Python\pythonProject\Work/F2/F21/f211.txt'))
# print(os.path.isdir(r'i:\PythonCours\Python\pythonProject\Work/F2/F21'))