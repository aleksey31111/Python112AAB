### LESSON 27 ###
## Modified Access
## name - public
## _name - protected
## __name - privat -- getter setter
#### Continue OOP #### Инкапсуляция:

print("Продолжение ООП - 2")
print("Класс <Point1> с Двумя Координатами")


class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point1(111, 222)
# print(p1)
print(p1.__dict__)  # Объект p1
print(p1.x, end='; ')  # Объеке p1.x
print(p1.y)  # Объект p1.y

print("ООП-2 - Инкапсуляция.")
print("Класс <Point2> с Двумя СКРЫТЫМИ Координатами")


class Point2:
    def __init__(self, x, y):
        self.__x = x  # ЗАКРЫТЫЕ Переменные
        self.__y = y  # Закрытая Переменная


p2 = Point2(21, 22)
### print(p2.__x, p2.__y)  # ERROR
### print(p2.x, p2.y)  # ERROR
p2.x = 100
p2.y = "abc"
print(p2.x, p2.y, sep="; ")
p2.__x = 221  # Новая Закрытая Переменнаяю
p2.__y = "abc221"  # Новая Закрытая Переменнаяю
print(p2.__dict__)

print("Написание <Геттеров> и <Сеттеров> для Доступа\n"
      "к Скрытым Данным Типа <<Private>>.")


class Point:

    def __init__(self, x, y):
        self.__x = self.__y = 0
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y

    #
    def set_x(self, x):  # Установить
        self.__x = x

    def get_x(self):  # Take
        return self.__x

    #### Закрытые МЕТОДЫ ####

    def __check_value(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    ### Изменение Любой Скрытой Переменной Через
    ### И Ограничение На Ввод через СКРЫТЫЙ Метод
    def set_coords(self, x, y):
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print("Координаты Должны Быть Числами.")

    def get_coords(self):
        return self.__x, self.__y

    ### Изменение Любой скрытой Переменной через Метод С Проверкой. ###


#    # def set_coords(self, x, y):
#    #     if (isinstance(x, int) or isinstance(x, float)) and \
#    #             (isinstance(y, int) or isinstance(y, float)):
#    #         self.__x = x
#    #         self.__y = y
#    #
#    # def get_coords(self):
#    #     return self.__x, self.__y


p1 = Point("300", 300)
print(p1.__dict__)
p1.set_x(301)
print(p1.__dict__)
print(p1.get_x())
p1.set_coords(302.221, 302.222)
print(p1.get_coords())
print(p1.__dict__)
# print(p1.__x, p1.__y)

# p1.__x = 311  # p1.x = 100
# p1.__y = 'abc'
# print(p1.__x, p1.__y)
# print(p1.__dict__)

# p1.set_x(100)
# print(p1.get_x())
# p1.set_coords(50, 70)
print(p1._Point__x)
p1._Point__x = 303.222
print(p1.__dict__)
print()

### Class Task 1 ###
print("Задание 1 Урока 27: Создать класс Rectangle,\n"
      "Описывающий ПРЯМОУГОЛЬНИК\n"
      "1 - В Классе Должны Быть Все Необходимые Методы,\n"
      "а так же Методы Вычисления Площади, Периметра и Диагонали\n"
      "и Метод Рисующий Прямоугольник Из Звездочек. ")
import math


class Rectangle:
    def __init__(self, a, b):
        self.__a = self.__b = 0
        if Rectangle.__check_value(a) and Rectangle.__check_value(b):
            self.__a = a
            self.__b = b

    def __check_value(val):
        if isinstance(val, (int, float)):
            return True
        return False

    def set_a(self, a):
        self.__a = a

    def get_a(self):
        return self.__a

    def set_b(self, b):
        self.__b = b

    def get_b(self):
        return self.__b

    def square(self):
        return self.__a * self.__b

    def perimeter(self):
        return self.__a * 2 + self.__b * 2

    def hypotenuse(self):
        return round(math.sqrt(math.pow(self.__a, 2) + math.pow(self.__b, 2)), 3)

    def draw_rectangle(self):
        # for i in range(self.__a):
        #     print("*" * self.__b)
        print(('*' * self.__b + "\n") * self.__a)


r1 = Rectangle(400, 400)
r1.set_a(4)
r1.set_b(5)
print(r1.get_a(), r1.get_b())
print(r1.square())
print(r1.perimeter())
print(r1.hypotenuse())
print(r1.draw_rectangle())
print()

print("Вариант 2. Задания 1 Урока 27")
import math


class Rectangle:
    def __init__(self, x, y):
        self.__x = self.__y = 0
        if Rectangle.__check_value(x) and Rectangle.__check_value(y):
            self.__x = x
            self.__y = y

    def __check_value(z):
        if isinstance(z, (int, float)):
            return True
        return False

    def set_x(self, x):
        if Rectangle.__check_value(x):
            self.__x = x

    def set_y(self, y):
        if Rectangle.__check_value(y):
            self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_area(self):
        return self.__x * self.__y

    def get_perim(self):
        return 2 * (self.__x + self.__y)

    def get_gipp(self):
        return math.sqrt(self.__x ** 2 * self.__y ** 2)

    def print_area_1(self):
        for i in range(self.__x):
            print("+" * self.__y)

    def print_area_2(self):
        print(("=" * self.__y + "\n") * self.__x)


r1 = Rectangle(3, 4)
r1.set_x(3)
r1.set_y(9)
print(r1.get_y(), r1.get_x())
print(r1.get_area())
print(r1.get_perim())
print(r1.get_gipp())
r1.print_area_1()
r1.print_area_2()
print()

print("Вариант 3. Задания 1 Урока 27")
import math


class Rectangle:

    def __init__(self, x, y):
        self.__x = self.__y = 0
        if Rectangle.__check_value(x) and Rectangle.__check_value(y):
            self.__x = x
            self.__y = y

    def __check_value(z):
        if isinstance(z, (int, float)):
            return True
        return False

    def set_x(self, x):
        if Rectangle.__check_value(x):
            self.__x = x

    def set_y(self, y):
        if Rectangle.__check_value(y):
            self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_area(self):
        return self.__x * self.__y

    def get_perim(self):
        return 2 * (self.__x + self.__y)

    def get_gipp(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    def print_area_3(self):
        for i in range(self.__x):
            print('&' * self.__y)

    def print_area_4(self):
        print(('@' * self.__x + '\n') * self.__y)


r1 = Rectangle(3, 4)
# a = int(input("Высота: "))
# b = int(input("Ширина: "))
r1.set_x(12)
r1.set_y(1)
print(r1.get_y(), r1.get_x())
print(r1.get_area())
print(r1.get_perim())
print(r1.get_gipp())
r1.print_area_3()
r1.print_area_4()
print()
r2 = Rectangle(2, 14)
r2.print_area_3()
print()
r3 = Rectangle(6, 10)
r3.print_area_4()
print()
print()

print("######################################")
print("# Дополнительные Магические Методы:  #\n")
print("# 1 - __getattr__() - Уникальный Метод Поиска Аттрибутов #\n")
print("# 2 - __getattribute__() - Метод для Сокрытия Аттрибутов.#\n")
print("# 3 - __setattr__() - Невозможность Изменить Аттрибут.")
print("# 4 - __slots__ - Закрытие Доступа к Переменным.")


class Point:
    WIDTH = 6  # Константа.
    __slots__ = ["__x", "__y", "z"]

    def __init__(self, x, y, ):
        self.__x = self.__y = 0
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y

    def __check_value(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def set_coords(self, x, y):
        if Point.__check_value(x) and Point.__check_value(y):
            if (isinstance(x, int) or isinstance(x, float)) and isinstance(y, int):
                self.__x = x
                self.__y = y
            else:
                print("Coords Must be Int")

    def get_coords(self):
        return self.__x, self.__y

    def __getattr__(self, item):  # item - Передаваемый Аргумент.
        return f"В классе {__class__.__name__} отсутствует атрибут: {item}"

    def __getattribute__(self, item):
        if item == "_Point__x":
            return "Закрытая Переменная."
        else:
            return object.__getattribute__(self, item)

    # def __setattr__(self, key, value):
    #     if key == "WIDTH":
    #         raise AttributeError("Нельзя изменить Значение WIDTH")
    #     else:
    #         self.__dict__[key] = value


p1 = Point(5, 10)
### p1.zzz = 12
# print(p1.zzz)  # Сообщение getattr
print(p1._Point__x)
# print(p1.__dict__)  # Не Работает со __slots__
p1.set_coords(45, 20)
print(p1.get_coords())
# print(p1.__dict__)    # Не Работает со __slots__

# # print(p1.__dict__)
# # p1.WIDTH = 7
#
# p1 = Point(5, 10)
### p1.z = 1  - ERROR - Потомучто Используется __slots__
print(p1.z)
print()

print()
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print("Setter")
#         if isinstance(x, (int,float)):
#             self.__x = x
#         else:
#             raise  ValueError("Format Not True")
#
#     def __get_x(self):
#         print("Getter")
#         return self.__x
#
#     def __del_x(self):
#         print("Del Property")
#         del self.__x
#
#     coordX = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# # p1.__set_x = 100
# p1.coordX = 100.4
# print(p1.coordX)
# print(p1.__dict__)
# del p1.coordX

print("")

print("######################################")
print("coordX = property(__get_x, __set_x) - ")
print("property - Свойство для Доступа к Закрытым Переменным")


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __set_x(self, x):
        print("Сеттер")
        if isinstance(x, (int, float)):
            self.__x = x
        else:
            raise ValueError("Неверный Формат Данных")

    def __get_x(self):
        print("Геттер")
        return self.__x

    def __del_x(self):
        print("Удаление Свойства")
        del self.__x

    coordX = property(__get_x, __set_x, __del_x)
#
#
p1 = Point(5, 10)
# p1.__set_x = 100  # Новое имя __set_x = 100
# print(p1.__dict__)
## p1.coordX = "100" # - проверка
p1.coordX = 100
print(p1.coordX)
# del p1.coordX

del p1.coordX
print(p1.__dict__)
print()

print("######################################################")
print("### Доступ к Закрытым Свойствам через ДЕКОРАТОРЫ 1 ###")
print("######################################################")


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def coordX(self):
        print("Геттер")
        return self.__x

    @coordX.setter
    def coordX(self, x):
        print("Сеттер")
        if isinstance(x, (int,float)):
            self.__x = x
        else:
            raise  ValueError("Format Not True")

    @coordX.deleter
    def coordX(self):
        print("Удаление Свойства")
        del self.__x

p1 = Point(5, 10)
p1.coordX = 100.0
print(p1.coordX)
del p1.coordX
print(p1.__dict__)

print("######################################################")
print("### Доступ к Закрытым Свойствам через ДЕКОРАТОРЫ 2 ###")
print("######################################################")


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        print("Геттер")
        return  self.__x
    @x.setter
    def x(self, x):
        print("Сеттер")
        if isinstance(x, (int, float)):
            self.__x = x
        else:
            raise ValueError("Неверный Формат Данных")
    @x.deleter
    def x(self):
        print("Удаление Свойства")
        del self.__x


p1 = Point(7, 15)
p1.x = 100.9
print(p1.x)
del p1.x
print(p1.__dict__)
print()

### Task 2 ###
print("Задание 2. Урока 27: Создать класс Person\n"
    "с Двумя Закрытыми Свойствами: ИМЯ и ВОЗРАСТ\n"
    "с Использованием Декоратора property\n"
    "Создать Возможность Изменения Этих Свойств,\n"
    "а также Возможность Их Удаления.")


class Person:
    def __init__(self,name,old):
        self.__name = name
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @name.deleter
    def name(self):
        del self.__name

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, o):
        self.__old = o

    @old.deleter
    def old(self):
        del self.__old


p1 = Person("Irina", 26)
print(p1.__dict__)
p1.name = "Igor"
p1.old = 36
print(p1.name)
print(p1.old)
del p1.name
del p1.old
print(p1.__dict__)





p2 = Person("Diana", 26)
print(p2.__dict__)
p2.old = 30
print(p2.old)
del p2.old
print(p2.__dict__)