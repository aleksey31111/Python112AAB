### Lesson 29 OOP-4

# import re
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_weight(weight)
#         self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("FIO must be String")
#         f = fio.split()  # ['', '', '']
#         # print(f)
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         # print(letters)
#         for s in f:
#             if len(s.strip(letters)) != 0:
#             # if s not in letters:
#                 raise TypeError("В ФИО можно использовать буквы и Дефис")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Возраст дб от 14 до 100")
#
#     @classmethod
#     def verify_weight(cls,w):
#         if not isinstance(w, float) or w <20:
#             raise TypeError("Weight!!!")
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError("Passport must be String!")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Data Not True Format")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Series and Namber Passport Mast Be Numbers!")
#
#     @property
#     def fio(self):
#         return  self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, password):
#         self.verify_ps(password)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.settet
#     def weight(self, weight):
#         self.verify_weight()
#         self.__weight = weight
#
#
#
# p1 = UserDate("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Sobolev Igor Nikolaevich""
# print(p1.fio)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Line:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw_line(self):
#         print(f"Drawing Line: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
# class Rect:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
# class Line:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#             self._sp = sp
#             self._ep = ep
#             self._color = color
#             self._width = width
#     def draw_rect(self):
#         print(f"Drawing Line: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# rect = Rect(Point(20, 40),  Point(10, 20))


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, w, h, color):
#         super().__init__(color)
#         self.__width = w
#         self.__height = h
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self,w):
#         self.__height = h
#
#     def area(self):
#         return self.__width * self.__height
#
#
# rect = Rectangle(10,20,"green")
# print(rect.width)


