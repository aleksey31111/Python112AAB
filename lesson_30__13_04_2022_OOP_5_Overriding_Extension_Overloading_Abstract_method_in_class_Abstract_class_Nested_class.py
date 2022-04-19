#### Lesson 30
### Continue Previous Lesson
print('+' * 90)
print("Пример 1: Переопределение Метода is_digit В set_coords(self,sp,ep) В Родительском Классе Prop,\n"
      "\t\t  Методом set_coords(self,sp,ep) is_int В Дочернем Классе Line(Prop)")
print('+' * 90)


class Point:  # Вспомогательный Класс
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def is_digit(self):
        if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
            return True
        return False

    def is_int(self):
        if isinstance(self.__x, int) and isinstance(self.__y, int):
            return True
        return False


class Prop:  # Родительский Класс для Line в Котором Есть только Инициализатор.
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def set_coords(self, sp, ep):
        if sp.is_digit() and ep.is_digit():
            self._sp = sp
            self._ep = ep
        else:
            print("Координаты Должны Быть Числами.")


class Line(Prop):  # Наследник Класса Prop
    def draw_line(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")

    def set_coords(self, sp, ep):
        if sp.is_int() and ep.is_int():
            self._sp = sp
            self._ep = ep
        else:
            print("Координаты Должны Быть Целочисленными")


line = Line(Point(1, 2), Point(10, 20))
line.draw_line()
line.set_coords(Point(7, 8), Point(100, 200))
line.draw_line()
print()
print('%' * 70)
print("Пример 2: Расширение Родительского Класса.")
print('%' * 70)


class Rect:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def show_rect(self):
        print(f"Прямоугольник;\nШирина: {self.width}\nВысота: {self.height}")


class RectFon(Rect):
    def __init__(self, w, h, bg):
        self.fon = bg
        super().__init__(w, h)

    def show_rect(self):
        super().show_rect()
        print("Фон: ", self.fon)


class RectBorder(Rect):
    def __init__(self, w, h, border):
        super().__init__(w, h)
        self.border = border

    def show_rect(self):
        super().show_rect()
        print(f'Рамка: {self.border}')


shape1 = RectFon(400, 200, 'yellow')
shape1.show_rect()
print()
shape2 = RectBorder(600, 300, "1px solid red")
shape2.show_rect()
print()

print('@' * 99)
print("Пример 3: Наследование От Готового Класса: BuiltIn Object 'List'.")
print('@' * 99)


class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))


v = Vector([1, 2, 3])
print(v)
print(type(v))

print('@' * 99)
print("Пример 4: Перегрузка Методов - Выполнение Функционала в Зависимости От Переданных Данных.\n"
      "\tРисование Двух Прямоугольников <one=Background> <two=1px solid>\n"
      "В Python Перегрузки Методов В Чистом Виде НЕТУ.")
print('@' * 99)


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def is_digit(self):
        if isinstance(self.__x, (int, float) and isinstance(self.__y, (int, float))):
            return True
        return False

    def is_int(self):
        if isinstance(self.__x, int) and isinstance(self.__y, int):
            return True
        return False


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def set_coords(self, sp, ep):
        if sp.is_digit():
            self._sp = sp
            self._ep = ep
        else:
            print("Coords Must Be Numbers")


class Line(Prop):
    def draw_line(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")

    # Возможность Задавать Только Одну Коордиеату Из Двух <ep>
    def set_coords(self, sp: Point, ep: Point = None):
        if ep is None:
            if sp.is_int():
                self._sp = sp
            else:
                print("Координаты Должны Быть Целочисленными.")
        else:
            if sp.is_int() and ep.is_int():
                self._sp = sp
                self._ep = ep
            else:
                print("Координаты Должны Быть Целочисленными.")


line = Line(Point(1, 2), Point(10, 20))
line.draw_line()
line.set_coords(Point(7, 8), Point(100, 200))
line.draw_line()
line.set_coords((Point(-10, -20)))
line.draw_line()
print()

print("№" * 66)
print("Пример 5: Абстрактные Методы При Наследовании Классов - Абстрактное Наследование\n"
      "\t    def draw(self):raise NotImplementedError(\"В дочернем Классе Должен Быть Определен mетод draw\")")
print("№" * 66)


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def is_digit(self):
        if isinstance(self.__x, (int, float) and isinstance(self.__y, (int, float))):
            return True
        return False

    def is_int(self):
        if isinstance(self.__x, int and isinstance(self.__y, int)):
            return True
        return False


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def set_coords(self, sp, ep):
        if sp.is_digit():
            self._sp = sp
            self._ep = ep
        else:
            print("Coords Must Be Numbers")

    def draw(self):
        raise NotImplementedError("В дочернем Классе Должен Быть Определен mетод draw")


class Line(Prop):
    def draw(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")


class Rect(Prop):
    # pass
    def draw(self):
        print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")


class Ellipse(Prop):
    def draw(self):
        print(f"Рисование Эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")


figs = list()
figs.append(Line(Point(0, 0), Point(10, 10)))
figs.append(Line(Point(10, 10), Point(20, 10)))
figs.append(Rect(Point(50, 50), Point(100, 100)))
figs.append(Ellipse(Point(-10, -10), Point(10, 10)))

for f in figs:
    f.draw()
print()

### Example 6. Task 1 ###
print("Пример 6. Задача 1:\n"
      "\t1 - Создать Класс:\n"
      "\t\t1.a - <Стол>;\n"
      "\t2 - И Дочерние:\n"
      "\t\t2.a - <Прямоугольный Столы>;\n"
      "\t\t2.b - <Круглые Столы>;\n"
      "Через Инициализатор <Базового Класса>:\n"
      "\tA - Передавайте Размен Поверхности Стола:\n"
      "\t\tA.1 - для <Прямоугольного Стола>:\n"
      "\t\t\tA.1.a - Ширина и Длинна;\n"
      "\t\tB.1 - для <Круглого Стола>:\n"
      "\t\t\tB.1.a - Радиус;\n"
      "В дочерних Классах Реализуйте Метод Вычисления <Площади Поверхности Стола>.")

import math


class Table:
    def __init__(self, width=None, length=None, radius=None):
        if radius is None:
            # self._width = width
            # self._length = length
            if length is None:  # Перегрузка Методов
                self._width = self._length = width
            else:
                self._width = width
                self._length = length
        else:
            self._radius = radius

    def calc_area(self):  # Абстрактный Метод
        raise NotImplemented("В дочернем Классе Должен Быть Определен Метод calc_area(")


class SqTable(Table):
    def calc_area(self):
        return self._width * self._length


class RoundTable(Table):
    def calc_area(self):
        return round(math.pi * pow(self._radius, 2), 3)


t = SqTable(20, 10)
print(t.__dict__)
print(t.calc_area())
t2 = SqTable(20)
print(t2.__dict__)
print(t2.calc_area())
t3 = RoundTable(radius=20)
print(t3.__dict__)
print(t3.calc_area())

# r = RoundTable(radius=28)
print()

print('&' * 87)
print("\tАбстрактный Класс - Класс который Содержит Хотя Бы Один <Абстрактный Метод>\n"
      "from abc import ABC, abstractmethod")
print('&' * 87)
from abc import ABC, abstractmethod


class Chess(ABC):
    def draw(self):
        print("Нарисовал Шахматную Фигуру.")

    @abstractmethod
    def move(self):
        # pass
        print("Метод move() в Базовом Классе")


# q = Chess()


class Queen(Chess):
    def move(self):
        super().move()
        print("Ферзь перемещен")


# q = Chess()
q = Queen()
q.draw()
q.move()

# ### Example 7. Task 2 ####
print("Пример 7. Задание Урока 2:\n"
      "1 - Создать Базовый Абстрактный Класс <Валюта> для Работы с Денежными Суммами\n"
      "\t1.a - Определить Методы Перевода Значения в Рубли и Вывода на Экран.\n"
      "\t\tРеализуйте Производные Классы <Доллар> и <Евро>\n"
      "\t\tc Собственными Методами Перевода в Рубли и Вывода на Экран.\n"
      "Решите Самостоятельно, какими Свойствами Будет Обладать\n"
      " Каждый Из Классов, и какие Методы Следует Сделать Абстрактными.")

from abc import ABC, abstractmethod


class Currency(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def convert_to_rub(self):
        pass

    def print_value(self):
        print(self.value, end=" ")


class Dollar(Currency):
    rate_to_rub = 74.16
    suffix = 'USD'

    def convert_to_rub(self):
        rub = self.value * Dollar.rate_to_rub
        return rub

    def print_value(self):
        super().print_value()
        print(Dollar.suffix, end=" ")


class Euro(Currency):
    rate_to_rub = 87.33
    suffix = 'EUR'

    def convert_to_rub(self):
        rub = self.value * Euro.rate_to_rub
        return rub

    def print_value(self):
        super().print_value()
        print(Euro.suffix, end=' ')


d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
for elem in d:
    elem.print_value()
    print(f"= {elem.convert_to_rub():.2f} RUB")

d2 = [Euro(5), Euro(10), Euro(50), Euro(100)]
for elem in d2:
    elem.print_value()
    print(f'= {elem.convert_to_rub():.2f} RUB')

#### Interface ####
print('^' * 81)
print("\t\t\t ИНТЕРФЕЙС - Абстрактный Класс в котором Не Один Метод Не Реализован.\n"
      "\t\t\t ИНТЕРФЕЙСЫ - публичны и не Имеют ПЕРЕМЕННЫХ В КЛАССЕ ")
print('^' * 81)

from abc import ABC, abstractmethod


class Father(ABC):
    @abstractmethod
    def display1(self):
        pass

    @abstractmethod
    def display2(self):
        pass


class Child(Father):
    def display1(self):
        print("class Child")


class GrandChild(Child):
    def display2(self):
        print("class DisplayChild")

gc = GrandChild()
gc.display1()
gc.display2()
print()

### NESTED CLASS ####
print('<' * 71)
print("\t\tВложеный Класс. Метод для связи outer_obj_method в Родительском Классе,\n"
      "\t\tи Переменная obj Во Вложенном Классе.")
print('^' * 71)
class MyOuter:
    age = 18

    def __init__(self, name):
        self.name = name

    @classmethod
    def outer_class_method(cls):
        print("Метод Внешнего Класса")

    def outer_obj_method(self):
        print("Метод для Связи")


    class MyInner:
        def __init__(self, inner_name, obj):
            self.inner_name = inner_name
            self.obj = obj

        def inner_method(self):
            print("Метод Внутреннегр Класса", MyOuter.age, self.obj.name)
            MyOuter.outer_class_method()
            self.obj.outer_obj_method()


out = MyOuter("Внешнний")
inner = out.MyInner("Внутренний", out)
inner.inner_method()
# print(inner.inner_name)

print('!' * 72)
print("Вложенные Классы - Видимость <Вложенного Класса>,\n"
      "Через Переменную <self.lg = self.Lightgreen()")
print('!' * 72)
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
