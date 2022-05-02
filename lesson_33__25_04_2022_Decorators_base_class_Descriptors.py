print("# ### LESSON 33 ###")
print(' #' * 40)
print("# #\t\tФунктор - объект Классов которые Можно Выполнять Как Фкнкции\t\t # #")
print(' #' * 40)


class Counter:
    def __init__(self):
        self.__count = 0

    def __call__(self, *args, **kwargs):
        self.__count += 1
        print(self.__count)


c1 = Counter()
c1()
c1()
c2 = Counter()
c2()
print()

print(' %' * 39)
print("Вариант 1. Пример 1 Урока 33")
print("# ###\t Функтор - Убирает Заданноые Символы В начале И конце Строки \t### #")
print(' %' * 39)


class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError("Аргумент Должен Быть Строкой")
        return args[0].strip(self.__chars)


s1 = StripChars("?:!.; ")
print(s1(" Hello World! "))
print(s1("?:Hello: World.; "))
print()
print("Вариант 2. Пример 1 Урока 33")


class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, a):
        if not isinstance(a, str):
            raise ValueError("Аргумент Должен Быть Строкой")
        return a.strip(self.__chars)


s1 = StripChars("?:!.; ")
print(s1(" Hello World! "))
print(s1("?:Hello: World.; "))
print()

print('$ ' * 43)
print("\tПример 2. Урока 33.")
print("### Вложенные Функции Замыкание  Убирает Заданные Символы В Начале и Конце Строки ###")
print('$ ' * 43)


def strip_chars(char):
    def wrap(string):
        if not isinstance(string, str):
            raise ValueError("Аргумент Должен Быть Строкой")
        return string.strip(char)

    return wrap


s1 = strip_chars("?:!.; ")
print(s1(" Hello World! "))
print(s1("?:Hello: World.; "))
print()

print('* ' * 45)
print("### Term 1 ### Сортировка на Функторах\n"
      "1) - Создайте Функтор для Определения Порядка Сортировки Списка p,\n"
      "\tСостоящей Из Объектов Класса Person:[('Иванов', 'Игорь', 28),\n"
      "\t('Петров', 'Степан', 21), ('Сидоров', 'Антон', 25), ('Петров', 'Анатолий', 11),\n"
      "\t('Иванов', 'Иван', 28)].\n"
      "То есть, вызывая Функтор (SortKey) с Названием Поля SortKey(\"surname\"),\n"
      "\tСортировка Выполнялась Бы По Этому Свойству.\n"
      "Если Указать Сразу Два Значения: SortKey(\"surname\", \"forename\"),\n"
      "\tТо Сортировка Делалась Бы По Фамилии, Но При Их Равенстве - По Имени")
print('* ' * 45)


class Person:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.forename = name
        self.age = age

    @property
    def data(self):
        return self.surname, self.forename, self.age


class SortKey:
    def __init__(self, *args):
        self.__method = args

    def __call__(self, lst):
        pass
        lst.sort(key=lambda i: [i.__dict__[key] for key in self.__method])


p = [Person('Иванов', 'Игорь', 28),
     Person('Петров', 'Степан', 21),
     Person('Сидоров', 'Антон', 25),
     Person('Петров', 'Анатолий', 11),
     Person('Иванов', 'Иван', 23)]
print("Без Сортировки")
for i in p:
    print(i.data)
print()
print("Сортировка По Фамилии")
s1 = SortKey('surname')
s1(p)
for i in p:
    print(i.data)
print()
print("Сортировка По Фамилии и Имени")
s2 = SortKey('surname', 'forename')
s2(p)
for i in p:
    print(i.data)
print()
print("Сортировка По Фамилии и Возрасту")
s3 = SortKey('surname', 'age')
s3(p)
for i in p:
    print(i.data)
print()

print("!! " * 20)
print("# ###\t\t класс как декоратор \t\t### #")
print("!! " * 20)


class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('Перед вызовом  Функции')
        self.func()
        print('После вызовом  Функции')


@MyDecorator
def func1():
    print('func')


func1()

print("### Другая Реализация ###")
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        print('Перед вызовом  Функции')
        res = self.func(a, b)
        print('После вызовом  Функции')
        return res


@MyDecorator
def func1(a, b):
    return a * b


print(func1(2, 5))
print()

print('+' * 88)
print("### Term 2 ### Создать Класс Power, Который Будет Декорировать Функцию.\n"
      "Функция БЬудет Возвращать Результат Умножения Двух Чисел (a=2, b=3),\n"
      "Ф Класс Возводит Их В Квадрат")
print('+' * 88)
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        print('Перед вызовом  Функции')
        res = self.func(a, b)
        print('После вызовом  Функции')
        return res, res**2


@MyDecorator
def func1(a, b):
    return a * b


print(func1(2, 5))


#####
# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print('Перед вызовом  Функции')
#         res = self.func(*args, **kwargs)
#         print('После вызовом  Функции')
#         return res
#
#
# @MyDecorator
# def func1(a, b):
#     return a * b
#
# @MyDecorator
# def func2(a, b, c):
#     return a * b * c
#
#
#
# print(func1(2, 5))
# print(func1(2, 5, 1))
#


###########
#
# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print('Перед вызовом  Функции')
#             func(a, b)
#             print('После вызовом  Функции')
#         return wrap
#
#
# @MyDecorator("test2")
# def add(a, b):
#     print(a * b)
#
#
# add(2, 5)


####### TERM 3 ##############
# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             print('*' * 10)
#
#             res = func(*args, **kwargs)
#             # print(res)
#             print('*' * 10)
#             return res ** self.name
#
#
# @Power(3)
# def mult(a, b):
#     return a * b
#
#
# mult(2, 5)


################################
# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#     return wrap


# class Person:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.forename = name


########################
# def decorator(cls):
#     class Wrapper(cls):
#         def Doubler(self, value):
#             return value * 2
#     return Wrapper
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Initializator ActualClass")
#
#     def quad(self, value):
#         return value
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(5))
#
# #### Дескриптор #####
# ## __get__()   __set__()   __delete__()    __set_name__()
# ### not-data deskriptors - __get__
# ### data descripter - все или несколько
# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#

# class Person:
#     def __init__(self, name, surname):
#         self.__name = StringD(name)
#         self.__surname = surname

# @property
# def name(self):
#     return self.__name
#
# @name.setter
# def name(self,value):
#     self.__name = value
#
# @property
# def surname(self):
#     return self.__name
#
# @surname.setter
# def surname(self, value):
#     self.__surname = value
#
#
# p = Person("Ivan", "Petrov")
# print(p.name.get())


###########
#
#
# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
#
#
# p = Person("Ivan", "Petrov")


##########  TASK 4 ##########
#
#
# class ValidString:
#     def __set_name__(self, owner, number, price):
#         self.__number = number
#         self.__price = price
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__number]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int):
#             raise ValueError(f"{self.__number} должно быть int")
#         if value < 0:
#             raise ValueError(f"{self.__number} должно быть >= 0")
#         instance.__dict__[self.__number, self.__price ] = value
#
#
# class Order:
#     name = ValidString()
#     number = ValidString()
#     def __init__(self, name, number, price):
#         self.__name = name
#         self.__number = number
#         self.__price = price
#
#
# p = Order("apple", 5, 10)
# print(p.number(6))

#### Variant 2 #####
# class NonNegative:
#     def __set_name__(self, owner, name):
#             self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#     def __set__(self, instance, value):
#         if value < 0:
#                 raise ValueError(f"{self.__name} должно быть POS")
#         instance.__dict__[self.name] = value
#
#
# class Order:
#     # name = ValidString()
#     # number = ValidString()
#     def __init__(self, name, number, price):
#         self.__name = name
#         self.__number = number
#         self.__price = price
#
#     def total(self):
#         return self.__price *self.__number


#### TERM 5 #####
# class Integer:
#     @classmethod
#     def verify_coord(cls, coord):
#         if not isinstance(coord, int):
#             raise TypeError(f"coordinate {coord} Must be int")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return  instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
# class Point3d:
#     x =Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3d(1,2,3)
# print(p1.__dict__)
