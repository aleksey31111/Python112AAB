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
print("Задание 1.")
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
        # pass
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
print('Пример 3. Урока 33')
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
print("Пример 3.1")
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
print("Задание 2. Урока 33.")
print("### Term 2 ### Создать Класс Power, Который Будет Декорировать Функцию.\n"
      "Функция БЬудет Возвращать Результат Умножения Двух Чисел (a=2, b=3),\n"
      "А Класс Возводит Их В Квадрат")
print('+' * 88)


class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        print('Перед вызовом  Функции')
        res = self.func(a, b)
        print('После вызовом  Функции')
        return res, res ** 2


@MyDecorator
def func1(a, b):
    return a * b


print(func1(2, 5))

print('$$ ' * 30)
print("Пример 3.2. Урока 33.")
print("## Класс Как Декоратор, Для Двух Функций с Разным Количеством Аргументов.")
print('$$ ' * 30)


class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Перед вызовом  Функции')
        res = self.func(*args, **kwargs)
        print('После вызовом  Функции')
        return res


@MyDecorator
def func1(a, b):
    return a * b


@MyDecorator
def func2(a, b, c):
    return a * b * c


print(func1(2, 3))
print(func2(2, 3, 5))

print("########### Пример 3.3. Урока 33 ######################")
print("Класс Как Декоратор с Декоратора с Параметрами.")


class MyDecorator:
    def __init__(self, arg):
        self.name = arg

    def __call__(self, func):
        def wrap(a, b):
            print('Перед вызовом  Функции')
            print(self.name)
            func(a, b)
            print('После вызовом  Функции')

        return wrap


@MyDecorator("test2")
def add(a, b):
    print(a * b)


add(2, 5)

print("№№№ " * 20)
print("####### TERM 3 ##############")
print("Задание 3: Создать Класс Power,Который Будет Декорировать Функцию.\n"
      "\tФункция Возвращает Результат Умножения Двух Чисел(a = 2, b = 2),\n"
      "\tА Класс Возводит Их В Степень, Которую Принимает Декоратор.")
print("№№№ " * 20)


class Power:
    def __init__(self, arg):
        self.name = arg

    def __call__(self, func):
        def wrap(*args, **kwargs):
            print('*' * 10)
            res = func(*args, **kwargs)
            print(res)
            print('*' * 10)
            return res ** self.name

        return wrap


@Power(3)
def mult(a, b):
    return a * b


print(mult(2, 2))
print()

print('@!@ ' * 20)
print("Пример 4")
print("Декораторы - Для Декорирования Методов Внутри Класса.")
print('@!@ ' * 20)


def dec(fn):
    def wrap(*args, **kwargs):
        print("*" * 20)
        fn(*args, **kwargs)
        print("*" * 20)

    return wrap


class Person:
    def __init__(self, name, surname):
        self.surname = surname
        self.name = name

    @dec
    def info(self):
        print(f"{self.name} {self.surname}")


p1 = Person("Виталий", "Карасев")
p1.info()
print()

print('@!@' * 25)
print("Пример 5: Декоратор Класса - Задекорировать Класс.\n")
print('@!@' * 25)


def decorator(cls):
    class Wrapper(cls):
        def doubler(self, value):
            return value * 2

    return Wrapper


@decorator
class ActualClass:
    def __init__(self):
        print("Initializator ActualClass")

    def quad(self, value):
        return value * 4


obj = ActualClass()
print(obj.quad(4))
print(obj.doubler(5))
print()

print('# % ' * 20)
print("### Дескриптор ### - Где Определен Аттрибут Класса - \n"
      "\t __get__(), __set__(), __delete__(), __set_name__(). Различают:\n"
      "\t\tnot-data deskriptors - __get__, и data descripter - все или несколько.\n"
      "Создаем Геттеры и Сеттеры.")
print('# % ' * 20)


# ## __get__()   __set__()   __delete__()    __set_name__()
# ### not-data deskriptors - __get__
# ### data descripter - все или несколько
class StringD:
    def __init__(self, value=None):
        if value:
            self.set(value)

    def set(self, value):
        self.__value = value

    def get(self):
        return self.__value


class Person:
    def __init__(self, name, surname):
        self.name = StringD(name)
        self.surname = StringD(surname)

    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, value):
    #     self.__name = value
    #
    # @property
    # def surname(self):
    #     return self.__surname
    #
    # @surname.setter
    # def surname(self, value):
    #     self.__surname = value


p = Person("Ivan", "Petrov")
print(p.name.get(), p.surname.get())
p.name.set("Petr")
p.surname.set("Petrov")
print(p.name.get(), p.surname.get())
# print(p.name)

###########
print('# % ' * 20)
print("### Дескриптор ### - Где Определен Аттрибут Класса - \n"
      "\t __get__(), __set__(), __delete__(), __set_name__().. Различают:\n"
      "\t\tnot-data deskriptors - __get__, и data descripter - все или несколько.\n"
      "Пишем Дескриптор.\n"
      "-def __set_name__(self, owner, name): - owner=Person(), name=ClassPropertyName\n"
      "--self.__name = name\n"
      "-def __get__(self, instance, owner): - instance=ClassInstance, owner=Person()\n"
      "--return instance.__dict__[self.__name]\n"
      "-def __set__(self, instance, value):\n"
      "--instanse>__dict__[self.__name] = value")
print('# % ' * 20)


class ValidString:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.__name} должно быть строкой")
        instance.__dict__[self.__name] = value


class Person:
    name = ValidString()
    surname = ValidString()

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


p = Person("Ivan", "Petrov")
print(p.name, p.surname)
print()

print("& * " * 20)
print("##  TASK 4 ##")
print("Задание 4: Создать Дескриптор Класса Order, Который Задает Имя Товара,\n"
      "\tЕго Цену и Количествою В Дескрипторе Должна Быть Реализована\n"
      "\tПроверка На Ввод Положительных Значений Цены и Количества.\n"
      "-def __set_name__(self, owner, name): - owner=Person(), name=ClassPropertyName\n"
      "--self.__name = name\n"
      "-def __get__(self, instance, owner): - instance=ClassInstance, owner=Person()\n"
      "--return instance.__dict__[self.__name]\n"
      "-def __set__(self, instance, value):\n"
      "--instanse>__dict__[self.__name] = value")

print("& * " * 20)


class NonNegative:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        # if not isinstance(value, int):
        #     raise ValueError(f"{self.__name} должно быть Целым Числом")
        if value < 0:
            raise ValueError(f"Значение должно быть Положительным")
        instance.__dict__[self.__name] = value


class Order:
    price = NonNegative()
    quantity = NonNegative()

    def __init__(self, name, price, quantity):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


a = Order("apple", 5, 10)
print(a.total())

print("#### Variant 2 #####")
class NonNegative2:
    def __set_name__(self, owner, name):
            self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.__name} должно быть POS")
        instance.__dict__[self.name] = value


class Order:
    name = NonNegative()
    number = NonNegative()
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def total(self):
        return self.__price * self.__quantity


a = Order("Bycicle", 100, 1000)
print(a.total())
print()

print("!@! " * 20)
print("#### TERM 5 ##### Создать Дескриптор Для Класса Point3D\n"
      "\t( Создание Точки В Трехмерном Пространстве ) С Проверкой На Ввод\n"
      "\tКоординат Точки Только Целочисленных Значений.")
print("!@! " * 20)
class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if not isinstance(coord, int):
            raise TypeError(f"coordinate {coord} Must be int")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
#         # return  instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
#         # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)

class Point3D:
    x =Integer()
    y = Integer()
    z = Integer()

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


p1 = Point3D(1,2,3)
print(p1.__dict__)
