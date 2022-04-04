### LESSON 27 ###
## Modified Access
## name - public
## _name - protected
## __name - privat -- getter setter
#### Continue OOP #### Инкапсуляция:
# class Point:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     # def set_x(self, x):  # Install
#     #     self.__x = x
#     #
#     # def get_x(self):  # Take
#     #     return self.__x
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float)
#             return  True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             if (isinstance(x, int) or isinstance(x, float)) and isinstance(y, int):
#                 self.__x = x
#                 self.__y = y
#             else:
#                 print("Coords Must be Int")
#
#     def get_coords(self):
#         return self.__x, self.y
#
#
# p1 = Point(5, 10)
# # print(p1.__x, p1.__y)
# # p1.__x = 100  # p1.x = 100
# # p1.y = 'abc'
# # print(p1.x, p1.y)
# # print(p1.__dict__)
# p1.set_x(100)
# print(p1.get_x())
# p1.set_coords(50, 70)
# print(p1._Poimt__x)


### Task 1 ###

# import math
#
# class Rectangle:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Rectangle.__check_value(x) and Rectangle.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, (int, float)):
#             return True
#         return False
#
#     def set_x(self, x):
#         if Rectangle.__check_value(x):
#             self.__x = x
#
#     def set_x(self, y):
#         if Rectangle.__check_value(y):
#             self.__y = y
#
#     def get_x(self):
#         return self.__x
#
#     def get_x(self):
#         return self.__y
#
#     def get_area(self):
#         return self.__x * self.__y
#
#     def get_perim(self):
#         return 2*(self.__x + self.__y)
#
#     def get_gipp(self):
#         return math.sqrt(self.__x**2 * self.__y**2)
#
#
# r1 = Rectangle(3,4)
# r1.set_x(3)
# r1.set_y(9)
# print(r1.get_y(), r1.get_x())

# import math
# class Rectangle:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Rectangle.__check_value(x) and Rectangle.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, (int, float)):
#             return True
#         return False
#     def set_x(self, x):
#         if Rectangle.__check_value(x):
#             self.__x = x
#
#     def set_y(self, y):
#         if Rectangle.__check_value(y):
#             self.__y = y
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def get_area(self):
#         return self.__x * self.__y
#
#     def get_perim(self):
#         return 2 * (self.__x + self.__y)
#
#     def get_gipp(self):
#         return math.sqrt(self.__x**2 + self.__y**2)
#
#     def print_area(self):
#         # for i in range(self.__x):
#         #     print('*' * self.__y)
#         print('*' * self.__y + '\n') * self.__x
# r1=Rectangle(3,4)
# r1.set_x(3)
# r1.set_y(9)
# print(r1.get_y(), r1.get_x())
# print(r1.get_area())
# print(r1.get_perim())
# print(r1.get_gipp())
# r1.print_area()


# class Point:
#     WIDTH = 5
#     __slots__ = ["__x", "__y"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float)
#             return  True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             if (isinstance(x, int) or isinstance(x, float)) and isinstance(y, int):
#                 self.__x = x
#                 self.__y = y
#             else:
#                 print("Coords Must be Int")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def __getattr__(self, item):
#         return f"In class {__class__.__name__} not attr: {item}"
#
#     def __getattribute__(self, item):
#         if item == "_Point__x":
#             return "Var closed"
#         else:
#             return object.__getattribute__()
#
#     def __setattr__(self, key, value):
#         if key == "WIDTH":
#             raise AttributeError("Not change Val WIDTH")
#         elsr:
#         self.__dict__[key] = value
#
# # p1 = Point(5, 10)
# # p1.zzz =12
# # print(p1.zzz)
# # p1.set_coords(45,20)
# # print(p1._Point__x)
# # print(p1.get_coords())
# # print(p1.__dict__)
# # p1.WIDTH = 7
#
# p1 = Point(5, 10)
# p1.x = 1
# print(p1.z)

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


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def coordX(self, x):
#         print("Setter")
#         if isinstance(x, (int,float)):
#             self.__x = x
#         else:
#             raise  ValueError("Format Not True")
#
#     @coordX.setter
#     def coordX(self):
#         print("Getter")
#         return self.__x
#
#     @coordX.deleter
#     def __del_x(self):
#         print("Del Property")
#         del self.__x
#
#     # coordX = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# # p1.__set_x = 100
# p1.coordX = 100.4
# print(p1.coordX)
# del p1.coordX
# print(p1.__dict__)


### Task 2 ###
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

    @property1
    def old(self):
        return self.__old

    @old.setter
    def name(self, o):
        self.__old = o

    @old.deleter
    def name(self):
        del self.__old


p1 = Person("Irina", 26)
print(p1.__dict__)
p1.name = "Igor"
print(p1.name)
del p1.name
print(p1.name)




p1 = Person("Irina", 26)
print(p1.__dict__)
p1.old = 30
print(p1.old)
del p1.old