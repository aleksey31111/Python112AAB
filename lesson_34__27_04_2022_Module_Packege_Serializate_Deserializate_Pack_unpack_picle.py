### LESSON 34 ###
#### META CLASS ####
# class MyList(list):
#     def get_length(self):
#         return len(self)
# lst = MyList()
# lst.append(10)
# lst.append(20)
# print(lst, lst.get_length())

# ### Вызов Конструктора Класса ###
# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst = MyList()
# lst.append(10)
# lst.append(20)
# print(lst, lst.get_length())

#
# class MyMetaclass(type):
#     def __new__(mcs, name, base, attr):
#         print("Создание Нового Объекта", name)
#         return super(MyMetaclass, mcs).__new__(mcs, name, base, attr)
#
#     def __init__(cls, name, base, attr):
#         print("Инициализатор Классов", name)
#         super(MyMetaclass, cls).__init__(name, base, attr)
#
#
# class Student(metaclass=MyMetaclass):
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# stud = Student("Анна")
# print("Имя Студента:", stud.get_name())
# print("Тип объекта Student:", type(stud))
# print("Тип Класса Student", type(Student))


##### MODULES ##### .py
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
# class Square:
#     def __init__(self, a):
#         self.a = a
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def get_perimetr(self):
#         return self.a + self.b + self.c

import geometry.rect
import geometry.sq
import geometry.trian


#
# from geometry import rect, sq, trian
#
# # from operator import rect, sq, trian
#
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
#
# s1 = sq.Square(10)
# s2 = sq.Square(20)
#
# t1 = trian.Triangle(1, 2, 3)
# t2 = trian.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())

# from car import electrocar
#
# def main():
#     e_car = electrocar.ElectroCar("Tesla", "T", 2018, 99000)
#     e_car.show_car()
#     e_car.description_battery()
#
#
# if __name__ == '__main__':
#     main()


#### Упаковка Данных ####
### Сериализация ###
### Десериализация ###

## marshal ## .pyc

## picle ##
## json ##
#  dump() - Сохраниет данные в файл.
# dumps() - Сохраняет данные в Память.
# load() - Считывает данные из Файла.
# loads() - Считывает Данные из Памяти.


# import pickle
# filename = "basket.txt"
# shop_list = {
#     "фрукты": ["яблоки", "манго"]
#     "овощи": ["морковь"]
#     "букет": 1000
# }
#
# with open(filename, "wb") as fh:
#     pickle.dump(shop_list, fh)
#
# with open(filename, 'rb') as fh:
#     shop_list_2 = pickle.load(fh)
#
# print(shop_list_2)


# import pickle
#
#
# class Test:
#     a_number = 35
#     a_string = "Hello"
#     a_list = [1, 2, 3]
#     a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
#     a_tuple = (22, 23)
#
#     def __str__(self):
#         return f"Число: {Test.a_number}\nСтрока:{Test.a_string}\n Список: {Test.a_list}\n" \
#                f"{Test.a_dict}\n{Test.a_tuple}"
#
#
# obj = Test()
# my_obj = pickle.dumps(obj)
# print(f"Сериализация в строку: {my_obj} ")
# l_obj = pickle.loads(my_obj)
# print(f"Десериализация в строку: {l_obj} ")
#
#
# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "text"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
#
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
#
# print(item3.__dict__)
# print(item3)


import pickle

class TextReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename)
        self.count = 0

    def read_line(self):
        self.count += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return f"{self.count}: {line}"

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["file"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        file = open(self.filename)
        for i in range(self.count):
            file.readline()
        self.file = file


reader = TextReader('hello.txt')
print(reader.read_line())
print(reader.read_line())

new_reader = pickle.loads(pickle.dumps(reader))
print(reader.read_line())

