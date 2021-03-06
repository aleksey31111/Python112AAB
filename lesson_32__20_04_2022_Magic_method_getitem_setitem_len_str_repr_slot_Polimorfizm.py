### Lesson 32 ###
print('* ' * 45)
print("Перегрузка Операторов +, -, *, &, //, / /=, *=, %=, +=, -= ")
print('* ' * 45)


class Clock:
    __DAY = 86400  # 24 * 60 * 50 Число секунд в Дне.

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Second Must Be Int")

        self.__sec = sec % self.__DAY

    def get_format_time(self):
        s = self.__sec % 60
        m = (self.__sec // 60) % 60
        h = (self.__sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def get_seconds(self):
        return self.__sec

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Right Must Be Type Clock()")
        return Clock(self.__sec + other.__sec)  # other.get_seconds())

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Right Must Be Type Clock()")
        self.__sec += other.get_seconds()
        return self

    def __eq__(self, other):
        return self.__sec == other.get_seconds()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.__sec < other.get_seconds()

    def __le__(self, other):
        return self.__sec <= other.get_seconds()

    def __gt__(self, other):
        return self.__sec > other.get_seconds()

    def __ge__(self, other):
        return self.__sec >= other.get_seconds()


c1 = Clock(100)
c2 = Clock(200)
# c4 = Clock(200)
# c3 = c1 + c2 + c4
# c4 += c2
print(c1.get_format_time())
print(c2.get_format_time())
if c1 == c2:
    print('Время одинаково.')
if c1 != c2:
    print("Время Разное")
if c1 > c2:
    print("First Time GREATER Second")
if c1 < c2:
    print("First Time LESS Second")
print()

print('@ ' * 40)
print("### Task 1 ### Перегрузите Операторы: '<', '<=', '>', '>='\n"
      "c3 > c1 True; c3 >= c1 True; c3 < c1 False; c3 <= c1 False;")
print('@ ' * 40)


class Clock:
    __DAY = 86400  # 24 * 60 * 50 Число секунд в Дне.

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Second Must Be Int")

        self.__sec = sec % self.__DAY

    def get_format_time(self):
        s = self.__sec % 60
        m = (self.__sec // 60) % 60
        h = (self.__sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def get_seconds(self):
        return self.__sec

    def __lt__(self, other):
        return self.__sec < other.get_seconds()

    def __le__(self, other):
        return self.__sec <= other.get_seconds()

    def __gt__(self, other):
        return self.__sec > other.get_seconds()

    def __ge__(self, other):
        return self.__sec >= other.get_seconds()


c1 = Clock(100)
c3 = Clock(300)
print(f"c1: {c1.get_format_time()}")
print(f"c3: {c3.get_format_time()}")
print(c3 > c1)
print(c3 >= c1)
print(c3 < c1)
print(c3 <= c1)
print()

print('= ' * 46)
print("\t\t\t### Example 1 ###\n"
      "Перегрузка КВАДРАТНЫХ СКОБОК на Получение Определенного Значения __getitem__(self, item)")
print('= ' * 46)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    # s1 = Student("Сергей", [5, 5, 3, 4, 5])
    # print(s1.marks[2])

    def __getitem__(self, item):
        # return self.marks[item]

        # s1 = Student("Сергей", [5, 5, 3, 4, 5])
        # print(s1[-2])

        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            # print("Неверный Индекс")
            raise IndexError("Неверный Индекс")

    # s1 = Student("Сергей", [5, 5, 3, 4, 5])
    # print(s1[2])

    def __setitem__(self, key, value):
        # self.marks[key] = value

        # s1 = Student("Сергей", [5, 5, 3, 4, 5])
        # s1[2] = 4
        # print(s1[2])
        # print(s1.marks)

        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс Должен быть Целым Положительным Числом")
        # if key > len(self.marks):
        #     raise TypeError("Такого Индекса Не Существует")
        if key > len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)

        self.marks[key] = value

    # s1 = Student("Сергей", [5, 5, 3, 4, 5])
    # s1[13] = 10
    # print(s1[13])
    # print(s1.marks)

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Undex Must Be Whole Number")
        del self.marks[key]


s1 = Student("Сергей", [5, 5, 3, 4, 5])
print(s1[2])
s1[10] = 6
print(s1[2])
print(s1[10])
del s1[5]
print(s1.marks)
del s1[5]
print(s1.marks)
del s1[5]
print(s1.marks)
del s1[5]
print(s1.marks)
del s1[5]
print(s1.marks)
print()

print('% ' * 40)
print("\t\t\tПерегрузка словаря")
print('% ' * 40)


class Clock:
    __DAY = 86400  # 24 * 60 * 50 Число секунд в Дне.

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Second Must Be Int")

        self.__sec = sec % self.__DAY

    def get_format_time(self):
        s = self.__sec % 60
        m = (self.__sec // 60) % 60
        h = (self.__sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def get_seconds(self):
        return self.__sec

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Right Must Be Type Clock()")
        return Clock(self.__sec + other.__sec)  # other.get_seconds())

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Right Must Be Type Clock()")
        self.__sec += other.get_seconds()
        return self

    def __eq__(self, other):
        return self.__sec == other.get_seconds()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.__sec < other.get_seconds()

    def __le__(self, other):
        return self.__sec <= other.get_seconds()

    def __gt__(self, other):
        return self.__sec > other.get_seconds()

    def __ge__(self, other):
        return self.__sec >= other.get_seconds()

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ Должен Быть Строкой")
        if item == "hour":
            return (self.__sec // 3600) % 24
        elif item == "min":
            return (self.__sec // 60) % 60
        elif item == "sec":
            return self.__sec % 60

        return "Неверный Ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ Должен Быть Строкой")
        if not isinstance(value, int):
            raise ValueError("Значение должно Быть Целым Числом")
        s = self.__sec % 60
        m = (self.__sec // 60) % 60
        h = (self.__sec // 3600) % 24
        if key == 'hour':
            self.__sec = s + 60 * m + value * 3600
        elif key == 'min':
            self.__sec = s + 60 * value + h * 3600
        elif key == 'sec':
            self.__sec = value + 60 * m + h * 3600


c1 = Clock(80000)
print(c1.get_format_time())
c1['hour'] = 10
c1['min'] = 26
c1['sec'] = 95
print(c1['hour'], c1["min"], c1["sec"])
print("###########################################################")
print("################ polimorfizm ######################")
print("Способность Python Понимать что у чему Относится")
print("###########################################################")


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_per_rect(self):
        return 2 * (self.w + self.h)

    def get_perimeter(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_per_sq(self):
        return 4 * self.a

    def get_perimeter(self):
        return 4 * self.a


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_per_tr(self):
        return self.a + self.b + self.c

    def get_perimeter(self):
        return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
print(f"2 Периметра Прямоугольника: {r1.get_per_rect()}, {r2.get_per_rect()}")

s1 = Square(10)
s2 = Square(20)
print(f"2 Периметр Квадратов: {s1.get_per_sq()}, {s2.get_per_sq()}")

t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)
print(f"2 Периметр Треугольников: {t1.get_per_tr()}, {t2.get_per_tr()}")

shape = [r1, r2, s1, s2, t1, t2]
for g in shape:
    if isinstance(g, Rectangle):
        print(f"Периметр прямоугольника {g.get_per_rect()}")
    elif isinstance(g, Square):
        print(f"Периметр Квадрата: {g.get_per_sq()}")
    elif isinstance(g, Triangle):
        print(f"Периметр Треугольника: {g.get_per_tr()}")

# shape = [r1, r2, s1, s2, t1, t2]
print(f"Периметры Фигур:", end=" ")
for g in shape:
    if isinstance(g, (Rectangle, Square, Triangle)):
        print(f"{g.get_perimeter()}", end=" ")
print()
print()

print(" = " * 30)
print("\t\t\t\t\tЕШ1 ОДИН ПРИМЕР ПРО ПОЛИМОРФИЗМ")
print(" = " * 30)


class Number:
    def __init__(self, value):
        self.value = value

    def total(self, a):
        return self.value + int(a)


class Text:
    def __init__(self, value):
        self.value = value

    def total(self, a):
        return len(self.value + str(a))


t1 = Number(10)
t2 = Text("Python")
print(len("Python"))
print(t1.total(35))
print((t2.total(35)))
print()

print(' # ' * 30)
print(f"\t\t\t\t\t### Task 2 ### Lesson 32\n"
      f"1) Создать Два Класса: Cat и Dog.\n"
      f"2) Реализуйте Методы: info (Информайия О Пмтомце)\n"
      f"\t\t и make_sound() (Какой Звук Издает Данный Питомец).\n"
      f"3) В цикле Выведите Методы Класса.\n"
      f"Variant 1")
print(' # ' * 30)


class Cat:
    def __init__(self, animal, name, age):
        self.animal = animal
        self.name = name
        self.age = age

    def info(self):
        return f"Меня Зовут: {self.name}"

    def sound(self):
        return f"{self.name} Мяукает"

    # def __repr__(self, animal, name, age):
    #     self.animal = animal
    #     self.name = name
    #     self.age = age


class Dog:
    def __init__(self, animal, name, age):
        self.animal = animal
        self.name = name
        self.age = age

    # def __repr__(self):
    #     self.animal  # = animal
    #     self.name  # = name
    #     self.age  # = age

    def info(self):
        return f"Меня зовут: {self.name}"

    def sound(self):
        return f"{self.name} Гавкает"

    # def __repr__(self, animal, name, age):
    #     self.animal = animal
    #     self.name = name
    #     self.age = age


d = Dog('Dog', 'Бахтимур', 10)
c = Cat('Cat', 'Матроскин', 10)
print(d)
print(c)
print(d.info())
for queue in [d, c]:
    print(c.info(), c.sound(), d.info(), d.sound())
print()
print()


### Variant 2 ###
class Cat:
    def __init__(self, animal, name, age):
        self.animal = animal
        self.name = name
        self.age = age

    def info(self):
        return f"Я {self.animal}. Меня зовут {self.name}. Мой возраст {self.age}."

    def sound(self):
        return f"{self.name} мяукает."


class Dog:
    def __init__(self, animal, name, age):
        self.animal = animal
        self.name = name
        self.age = age

    def info(self):
        return f"Я {self.animal}. Меня зовут {self.name}. Мой возраст {self.age}."

    def sound(self):
        return f"{self.name} гавкает."


k1 = Cat("кот", "Пушок", 2.5)
d1 = Dog("собака", "Мухтар", 4)
lst = [k1, d1]
# for i in lst:
for i in (k1, d1):
    print(i.info())
    print(i.sound())
print()
print()

print(' % ' * 30)
print(f"\t\t\t\t\t### Example 2 ####\n"
      f"1) Создать Иерархию Классов:\t"
      f"\tHuman(Человек), Student(Студент), Teacher(Преподаватель), Graduate(Дипломник)\n"
      f"1.1) Создать Список Группы Предсиавителей Данной Иерархии\n"
      f"\tВывести Информацию О Каждом Участнике.\n"
      f"Student(\"Батодалаев\", \"Даши\", 16, \"ГК\", \"Web_011\", 5),\n"
      f"Student(\"Загидуллин\", \"Линар\", 32, \"РПО\", \"PD_011\", 5),\n"
      f"Graduate(\"Шугани\", \"Сергей\", 15, \"РПО\", \"PD_011\", 5, \"Защита персональных данных\"),\n"
      f"Teacher(\"Даньшин\", \"Андрей\", 38, \"Астрофизика\", 110),\n"
      f"Student(\"Маркин\", \"Даниил\", 17, \"ГК\", \"Python_011\", 5),\n"
      f"Teacher(\"Башкиров\", \"Алексей\", 45, \"Разработка приложений\", 20)")
print(" % " * 30)


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def info(self):
        print(f"{self.first} {self.last} {self.age}")


class Student(Human):
    def __init__(self, spec, group, reit, first, last, age):
        super().__init__(first, last, age)
        self.spec = spec
        self.group = group
        self.reit = reit

    def info(self):
        print(f"{self.spec} {self.group} {self.reit}", end=" ")
        super().info()


class Teacher(Human):
    def __init__(self, spec, exp, first, last, age):
        super().__init__(first, last, age)
        self.spec = spec
        self.exp = exp

    def info(self):
        print(f"{self.spec} {self.exp}", end=" ")
        super().info()


class Graduate(Student):
    def __init__(self, topic, first, last, age, spec, group, reit):
        super().__init__(first, last, age, spec, group, reit)
        self.topic = topic

    def info(self):
        print(f"{self.topic}", end=" ")
        super().info()


group = [
    Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
    Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
    Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
    Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
    Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
    Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
]
# s1 = Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5)
# s1.info()
for i in group:
    i.info()
print()

print("#### variant 2 ####")


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def info(self):
        print(f"{self.first} {self.last} {self.age}")


class Student(Human):
    def __init__(self, spec, group, reit, first, last, age):
        super().__init__(first, last, age)
        self.spec = spec
        self.group = group
        self.reit = reit

    def info(self):
        print(f"{self.spec} {self.group} {self.reit}", end=" ")
        super().info()


class Teacher(Human):
    def __init__(self, spec, exp, first, last, age):
        super().__init__(first, last, age)
        self.spec = spec
        self.exp = exp

    def info(self):
        print(f"{self.spec} {self.exp}", end=" ")
        super().info()


class Graduate(Student):
    def __init__(self, topic, first, last, age, spec, group, reit):
        super().__init__(first, last, age, spec, group, reit)
        self.topic = topic

    def info(self):
        print(f"{self.topic}", end=" ")
        super().info()


group = [
    Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
    Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
    Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
    Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
    Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
    Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
]
for i in group:
    i.info()
print()

print(' * ' * 30)
print("Магические Методы - Для Отображения Данныз из Класса\n"
      "__repr__(self) __str__(self)")
print(' * ' * 30)


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"


cat = Cat("Пушок")
print(cat)
print()

print(' ( ' * 30)
print("#### Перегрузка Метдов len ####")
print(' ) ' * 30)


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)


p = Point(1, 7)
print(len(p))
p = Point(1, 5, 7)
print(len(p))
print()

print(" & " * 30)
print("\t\t\t\t\tПерегрузка Коллекции __slots__")
print(' & ' * 30)

import math


class Point:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = math.sqrt(x * x + y * y)

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


p1 = Point(2, 8)
print(p1.length)
# # p1.z = 50
# # print(p1.__dict__)
print()

print(' ! ' * 30)
print("\t\t\tСравнение Сколько Они Занимают Памяти с __sizeof__ и Без")
print(' ! ' * 30)
import math


class Point:
    __slots__ = ('x', 'y')  # , '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = math.sqrt(x * x + y * y)


pt = Point(1, 2)
pt2 = Point2D(1, 2)
print("pt =", pt.__sizeof__())
print("pt2 = ", pt2.__sizeof__() + pt2.__dict__.__sizeof__())
print()

print(' ++ ' * 23)
print("\t\t\t\t\tКолекции __slot__ при Наследовании.\n"
      "\tДочерние Классы Наследуют Колекцию __slot__ Родительского Класса")
print(' ++ ' * 23)
import math


class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point):
    # pass
    __slots__ = 'z'

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


pt = Point(1, 2)
pt3 = Point3D(10, 20, 30)
# pt3.z = 30
print(pt3.x, pt3.y, pt3.z)
# print(pt3.__dict__)
