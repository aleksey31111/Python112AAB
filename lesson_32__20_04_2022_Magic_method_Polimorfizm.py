### Lesson 31 ###


# class Clock:
#     __DAY = 86400 # 24 * 60 * 50 Число секунд в Дне.
#
#     def __init__(self, sec: int):
#         if not isinstance(sec,int):
#             raise ValueError("Second Must Be Int")
#
#         self.__sec = sec % self.__DAY
#
#
#     def get_format_time(self):
#         s = self.__sec % 60
#         m = (self.__sec // 60) % 60
#         h = (self.__sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" +str(x)
#
#     def get_seconds(self):
#         return self.__sec
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Right Must Be Type Clock()")
#         return Clock(self.__sec + other.__sec)  # other.get_seconds())
#
#     def __iadd__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Right Must Be Type Clock()")
#         self.__sec += other.get_seconds()
#         return self
#
#     def __eq__(self, other):
#         return self.__sec == other.get_seconds()
#
#     def __ne__(self, other):
#         return not self.__eq__(other)

    # def __lt__(self, other):
    #     return self.__lt__(other)
    #
    # def __le__(self, other):
    #     return self.__le__(other)
    #
    # def __gt__(self, other):
    #     return self.__gt__(other)
    #
    # def __ge__(self, other):
    #     return self.__ge__(other)
# c1 = Clock(100)
# c2 = Clock(200)
# # c4 = Clock(200)
# # c3 = c1 + c2 + c4
# # c4 += c2
# print(c1.get_format_time())
# print(c2.get_format_time())
# if c1 ==c2:
#     print('Время одинаково.')
# if c1 != c2:
#     print("Время Разное")
# if c1 > c2:
#     print("First Time GREATER Second")
# if c1 < c2:
#     print("First Time LESS Second")

# print(c4.get_format_time())
# c1 += c2 +c4
# print(c3.get_format_time())


### Task 1 ###
# def __lt__(self, other):
#     return self.__sec < other.get_seconds()
#
# def __le__(self, other):
#     return self.__sec <= other.get_seconds()
#
# def __gt__(self, other):
#     return self.__sec > other.get_seconds()
#
# def __ge__(self, other):
#     return self.__sec >= other.get_seconds()
#

### Example 1 ###
# class Student:
#     def __init__(self, name,marks):
#         self.name =name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item <= len(self.marks):
#             return self.marks[item]
#         else:
#             # print("Wrong Index")
#             raise IndexError("Неверный Index")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс Должен быть Целым Положительным Числом")
#         # if key >= len(self.marks):
#         #     raise TypeError("Индекс Должен быть Целым Положительным Числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Undex Must Be Whole Number")
#         del self.marks[key]

#
# class Clock:
#     __DAY = 86400 # 24 * 60 * 50 Число секунд в Дне.
#
#     def __init__(self, sec: int):
#         if not isinstance(sec,int):
#             raise ValueError("Second Must Be Int")
#
#         self.__sec = sec % self.__DAY
#
#
#     def get_format_time(self):
#         s = self.__sec % 60
#         m = (self.__sec // 60) % 60
#         h = (self.__sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" +str(x)
#
#     def get_seconds(self):
#         return self.__sec
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Right Must Be Type Clock()")
#         return Clock(self.__sec + other.__sec)  # other.get_seconds())
#
#     def __iadd__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Right Must Be Type Clock()")
#         self.__sec += other.get_seconds()
#         return self
#
#     def __eq__(self, other):
#         return self.__sec == other.get_seconds()
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __lt__(self, other):
#         return self.__sec < other.get_seconds()
#
#     def __le__(self, other):
#         return self.__sec <= other.get_seconds()
#
#     def __gt__(self, other):
#         return self.__sec > other.get_seconds()
#
#     def __ge__(self, other):
#         return self.__sec >= other.get_seconds()
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Key Nust Be str")
#         if item == "hour":
#             return (self.__sec // 3600) % 24
#         elif item == "min":
#             return (self.__sec // 60)/60
#         elif item == "sec":
#             return self.__sec % 60
#         return "Wrong Value"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Key Must Be String")
#         if not isinstance(value, int):
#             raise ValueError("Key Must Be String")
#         s = self.__sec % 60
#         m = (self.__sec // 60)/60
#         h = (self.__sec // 3600) % 24
#         if key == 'hour':
#             self.__sec = s + 60 * m + value * 3600
#         elif key == 'min':
#             self.__sec = s + 60 * value + h * 3600
#         elif key == 'sec':
#             self.__sec


############################################################
################ polimorfizm ######################
###########################################################
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_per_rect(self):
#         return 2*(self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_per_sq(self):
#         return 4 * self.a
#
# class Triangle:
#     def __init__(self, a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
# r1 = Rectangle(1,2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
# t1 = Triangle(1,2,3)
# t2 = Triangle(4,5,6)
#
# shape = [r1, r2, s1, s2]
# for g in shape:
#     if isinstance(g, Rectangle):
#         print(g.get_per_rect())
#     else:
#         print(g.get_per_sq())
#
# for g in shape:
#     print(g.get_perimetre)

#
# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return  self.value + int(a)


### Task 2 ###
# class Cat:
#     def __init__(self,name,sound):
#         self.name = name
#         self.sound = sound
#
#     def info(self):
#         return self.name
#
#     def sound(self):
#         return self.sound()
#
# class Dog:
#     def __init__(self,name,sound):
#         self.name = name
#         self.sound = sound
#
#     def info(self):
#         return self.name
#
#     def sound(self):
#         return self.sound()
#
# d = Dog('Cat','Gav')
# c =Cat('Cat','Miyu')
# print(d)
# print(c)
# print(d.info())


### Variant 1 ###
# class Cat:
#     def __init__(self, animal, name, age):
#         self.animal = animal
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я {self.animal}. Меня зовут {self.name}. Мой возраст {self.age}."
#     def sound(self):
#         return f"{self.name} мяукает."
# class Dog:
#     def __init__(self, animal, name, age):
#         self.animal = animal
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я {self.animal}. Меня зовут {self.name}. Мой возраст {self.age}."
#     def sound(self):
#         return f"{self.name} гавкает."
#
# k1 = Cat("кот", "Пушок", 2.5)
# d1 = Dog("собака", "Мухтар", 4)
# lst = [k1, d1]
# # for i in lst:
# for i in (k1, d1):
#     print(i.info())
#     print(i.sound())



### Example 2 ####
# class Human:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#
#     def info(self):
#         print() f"{self.first} {self.last} {self.age}"
#
# class Student(Human):
#     def __init__(self, first, last, age, spec, group,reit):
#         super().__init__(first, last, age)
#         self.spec = spec
#         self.group = group
#         self.reit = reit
#
#     def info(self):
#         super().info()
#         print(f"{self.spec}{self.group}{self.reit}")
# class Teacher(Human):
#     def __init__(self,spec, exp, first, last, age):
#         super().__init__(first, last, age)
#         self.spec = spec
#         self.exp = exp
#
#     def info(self):
#         return f"{self.spec} {self.exp}"
#
# class Graduate(Student):
#     def __init__(self, topic,first, last, age, spec, group,reit):
#         super().__init__(first, last, age, spec, group,reit)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"{self.topic}")
# group = [
# Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
# Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
# Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
# Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
# Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
# Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]

#### variant 2
# class Human:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#
#     def info(self):
#         print(f"{self.first} {self.last} {self.age}")
#
# class Student(Human):
#     def __init__(self, spec, group, reit, first, last, age):
#         super().__init__(first, last, age)
#         self.spec = spec
#         self.group = group
#         self.reit = reit
#
#     def info(self):
#         print(f"{self.spec} {self.group} {self.reit}", end=" ")
#         super().info()
#
#
# class Teacher(Human):
#     def __init__(self, spec, exp, first, last, age):
#         super().__init__(first, last, age)
#         self.spec = spec
#         self.exp = exp
#
#     def info(self):
#         print(f"{self.spec} {self.exp}", end=" ")
#         super().info()
#
#
# class Graduate(Student):
#     def __init__(self, topic, first, last, age, spec, group, reit):
#         super().__init__(first, last, age, spec, group, reit)
#         self.topic = topic
#
#     def info(self):
#         print(f"{self.topic}", end=" ")
#         super().info()
#
#
# group = [
# Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
# Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
# Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
# Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
# Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
# Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()


# class Cat:
#     def __init__(self,name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)

#### Перегрузка Метдов len ####
# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
#
# p = Point(1, 5, 7)
# print(len(p))

# import math
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x +y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self,value):
#         self.__length = value
#
# p1 = Point(2, 8)
# # p1.z = 50
# # print(p1.__dict__)

# import math
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#
# pt = Point(1,2)
# pt2 = Point2D(1,2)
# print("pt =", pt.__sizeof__())
# print("pt2 = ", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


import math
class Point:
    __slots__ = ('x', 'y', '__length')

    def __init__(self,x,y):
        self.x = x
        self.y = y


class Point3D:
    __slots__ = 'z'
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z

pt = Point(1,2)
pt3 = Point3D(10,20,30)
# pt3.z = 30
# print(pt3.z)