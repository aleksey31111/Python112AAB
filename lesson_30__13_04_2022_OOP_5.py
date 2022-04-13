#### Lesson 30
### Continue Previous Lesson
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int,float) and isinstance(self.__y,(int,float))):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int and isinstance(self.__y,float)):
#             return True
#         return False
#
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Coords Must Be Numbers")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Coords Must Be Int")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(7,8), Point(100,200))


# class Rect:
#     def __init__(self, w, h):
#         self.width = w
#         self.height = h
#
#     def show_rect(self):
#         print(f"Прямоугольник;\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, w, h, bg):
#         self.fon = bg
#         super().__init__(w, h)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон: ", self.fon)
#
#
# # class RectBorder(Rect):
# #     def __init__(self, w, h, bg):
# #         self.fon
#
# class RectBorder(Rect):
#     def __init__(self, w, h, border):
#         super().__init__(w, h)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'Рамка: {self.border}')
#
#
# shape1 = RectFon(400, 200, 'yellow')
# shape1.show_rect()


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))


#### Перегрузка Методов ####

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int,float) and isinstance(self.__y,(int,float))):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int and isinstance(self.__y,int)):
#             return True
#         return False
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Coords Must Be Numbers")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coords(self, sp, ep):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Coords Must Be Int")
#
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Coords Must Be Int")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(7,8), Point(100,200))
# line.draw_line()
# line.set_coords((Point(-10,-20)))

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float) and isinstance(self.__y, (int, float))):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int and isinstance(self.__y, int)):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Coords Must Be Numbers")
#
#     def draw(self):
#         raise NotImplementedError("В дочернем Классе Должен Быть Определен mетод draw")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     pass
#     # def draw(self):
#     #     print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование Эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
# for f in figs:
#     f.draw()


### Task 1
# import math
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             # self._width = width
#             # self._length = length
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplemented("В дочернем Классе Должен Быть Определен Метод calc_area(")
#
# class SqTable(Table):
#     def calc_area(self):
#         return  self._width * self._length
#
# class RoundTable(Table)
#     def calc_area(self):
#         return round(math.pi * self._radius)
#
# t = SqTable(20,10)
# print(t.__dict__)
# print(t.calc_area())
#
# r = RoundTable(radius=28)


# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Draw Shess Fig")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в Базовом Классе")
#
#
# class Qeen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен")
#
#
# # q = Chess()
# q = Qeen()
# q.draw()
# q.move()


# ### Example 2 ####
# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# for elem in d:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():2.f} RUB")

# Variants

# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#

# d2 = [Euro(5), Euro(10), Euro(50), Euro(100)]
# for elem in d2:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
#

# class Euro(Currency):
#     rate_to_rub = 85.50
#     suffix = 'EUR'
#     def convert_to_rub(self):
#         rub=self.value*Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#

#### Interface ####
# from abc import ABC, abstractmethod
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("class Child")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("class DisplayChild")
#
# gc = GrandChild()
# gc.display1()
# gc.display2()

### NESTED CLASS ####
# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print("Method Outer Class")
#
#     def outer_obj_method(self):
#         print("Method for comunication")
#
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Method Inner Class", MyOuter.age, self.obj.name)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter("Внешнний")
#
# inner = out.MyInner("Внутренний")
# inner.inner_method()
# print(inner.inner_name)


class Color:
    def __init__(self):
        self.name = 'Green'
        self.lg = self.Lightgreen()

    def show(self):
        print("Name:", self.name)

    class Lightgreen:
        def __init__(self):
            self.name = "Light Green"
            self.code = "024AVC"

        def display(self):
            print('Name', self.name)
            print('Code', self.code)


outer = Color()
outer.show()
g = outer.lg
g.display()
