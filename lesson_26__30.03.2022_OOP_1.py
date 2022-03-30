### LESSON 26 OOP ###
#  class <Name>:
#       свойство (поле) = значение
#
#       def __init__(self):
#           инициализатор
#
#       Методы(): #Функция
#           тело
#
#       атрибут = свойство + метод
#
#
# Специальные методы:
#    Конструктор (__new__)
#    Инициализатор  (__init__)
#    Деструктор





# class Point3D:
#     pass
#
#
# class Point:
#     """Класс для предоставления точек а плоскости"""
#     x = 1
#     y = 1
#
#
#     # def set_coords(self, name):
#     #     print("Hello", name)
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# print(p1.set_coords(5, 10))
# print(p1.__dict__)
#
# p1 = Point()
# p1.x = 100
# p1.y = 300
# p1.set_coords("addmin")
# Point.set_coords(p1, "Elena")
#
# p2 = Point()
# p2.set_coords("Igor")

# print(type(p1))
# print(isinstance(p1, Point))
# print(isinstance(p1, Point3D))
# print(p1.x, p1.y)
# print(p1.__dict__)
# print(getattr(p1, "x"))
# ### print(getattr(p1, "z")) ERROR
# print(getattr(p1, "z", False))
# print(getattr(p1, "z", "No"))
# print(hasattr(p1, "y"))
# print(setattr(p1, "z", 7))
# print(p1.__dict__)
# print(delattr(p1, "z"))
# print(p1.__dict__)
#
#
#
# p2 = Point()
# print(p2.__dict__)
# print(p2.x, p2.y)
# # print(Point.__doc__)
# # print(Point.__name__)
# # print(dir(Point))

#### Task 1 ####
# class Human:
#     name = "name"
#     birthday = "00.00.00"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана {self.country}\nГород {self.city}\nАдрес {self.address}")
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Egor")
# print(h1.get_name())
#
# class Cars:
#     name = 'model'
#     year = "out_year"
#     car_manufactory = "car_manufactory"
#     engine_power = "engine_power"
#     color = ""
#     price = ""
#     def car_info(self):
#         print(f'Название модели: {self.name}\nГод выпуска: {self.year}\n'
#               f'Производитель{self.car_manfactory}'
#               f'\nМощность двигателя {self.engine_power}\n'
#               f'Цвет  {self.color}\nЦена {self.price}')
#     def info_car(self, n, y, w, p, c, pr):
#         self.name = n
#         self.year = y
#         self.car_manufactory = w
#         self.engine_power = p
#         self.color = c
#         self.price = pr
#     def power_auto(selfself, power):
#



#### Example 1 ####
class Person:
    skill = 10

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print_info(self, name, surname):
        # self.name = name
        # self.surname = surname
        # res = 20
        print("Данные сотрудника; ", self.name, self.surname)

    def add_skill(self, k):
        self.skill += k
        print(f"Квалификация сотрудника: {self.name}", self.skill, "\n")


# p1 = Person()
# p1.print_info("Viktor", "Reznik")
# p1.add_skill(3)
# p2 = Person()
# p2.print_info("Anna", "Dolgih")
# p2.add_skill(2)


#### Constructor ####
# class Point:
#     def __new__(cls, *args, **kwargs):
#         print("Constructor")
#         return super().__new__(cls)
#
#     def __init__(self,x ,y):
#         print("Initizalizator")
#
#     def __del__(self):
#         print("Удаление экземпляра: " + self.__class__.__name__)
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# print(p1.__dir__)
# del p1
# # print(p1.x)
# p2 = Point()
# print(p2.__dict__)



# class Point:
#     count = 0  # Static Options
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1
#         # self.count += 1
#
# p1 = Point(5, 10)
#
# p2 = Point(10, 20)
# p3 = Point(10, 20)
#
# print(Point.count)
# print(p1.count)
# print(p2.count)
#
# # print(Point.x)  # Error
# # print(p1.x)
#



class Robot:
    k = 0

    def __init__(self, name):
        self.name = name
        print("Инициализация робота: ", self.name)
        print("Hello! My name is: ", self.name)
        Robot.k += 1

    def __del__(self):
        print(self.name, "Выулючается!")
        Robot.k -= 1

        if Robot.k == 0:
            print(self.name)
        else:
            print("Robots that works: ", Robot.k)


droid1 = Robot("R2-D2")
print("Number Of Robots: ", Robot.k)

droid2 = Robot("C-3P0")
print("Number Of Robots: ", Robot.k)

print("*" * 20)
del droid1
del droid2

print("Численность роботов: ", Robot.k)