### Lesson 29 OOP-4
print("Пример 1 Урока 29 11.04.2022: Соответствие Данных Пользователя.\n"
      "Совмещение Проверки И Инициализации.")

import re


class UserDate:
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_weight(weight)
        self.verify_ps(ps)

        self.__fio = fio
        self.__old = old
        self.__password = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if not isinstance(fio, str):
            raise TypeError("ФИО должно быть строкой")
        f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
        # print(f)
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")
        letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
        # print(letters)  # ВолковИгорьНиколаевич
        for s in f:
            if len(s.strip(letters)) != 0:
                # if s not in letters:
                raise TypeError("В ФИО можно использовать буквы и Дефис")

    @classmethod
    def verify_old(cls, old):
        if not isinstance(old, int) or old < 14 or old > 100:
            raise TypeError("Возраст дб от 14 до 100")

    @classmethod
    def verify_weight(cls, w):
        if not isinstance(w, float) or w < 20:
            raise TypeError("Вес должен быть Вещественным Числом от 20кг и Выше")

    @classmethod
    def verify_ps(cls, ps):
        if not isinstance(ps, str):
            raise TypeError("Паспорт Должен Быть Строкой.!")
        s = ps.split()  # ['1234', '567890']
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный Формат Данных.")
        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и Номер Паспорта Должны Быть Числами.")

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, ps):
        self.verify_ps(ps)
        self.__password = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    def print_info(self):
        print('=' * 30)
        print(self.__fio)
        print(self.__old)
        print(self.__password)
        print(self.__weight)
        print('+' * 45)


p1 = UserDate("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
p1.print_info()
p1.fio = "Sobolev Igor Nikolaevich"
print(p1.fio)
p1.print_info()
p1.old = 30
p1.password = '4567 123456'
p1.weight = 70.2
p1.print_info()
print(p1.__dict__)

print("Variant 2. Примера 1 Урока 29.")
print("Пример 1 Урока 29 11.04.2022: Соответствие Данных Пользователя.")
import re


class UserDate:
    def __init__(self, fio, old, ps, weight):
        # self.verify_fio(fio)
        # self.verify_old(old)
        # self.verify_weight(weight)
        # self.verify_ps(ps)

        self.fio = fio
        self.old = old
        self.password = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if not isinstance(fio, str):
            raise TypeError("ФИО должно быть строкой")
        f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
        # print(f)
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")
        letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
        # print(letters)  # ВолковИгорьНиколаевич
        for s in f:
            if len(s.strip(letters)) != 0:
                # if s not in letters:
                raise TypeError("В ФИО можно использовать буквы и Дефис")

    @classmethod
    def verify_old(cls, old):
        if not isinstance(old, int) or old < 14 or old > 100:
            raise TypeError("Возраст дб от 14 до 100")

    @classmethod
    def verify_weight(cls, w):
        if not isinstance(w, float) or w < 20:
            raise TypeError("Вес должен быть Вещественным Числом от 20кг и Выше")

    @classmethod
    def verify_ps(cls, ps):
        if not isinstance(ps, str):
            raise TypeError("Паспорт Должен Быть Строкой.!")
        s = ps.split()  # ['1234', '567890']
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный Формат Данных.")
        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и Номер Паспорта Должны Быть Числами.")

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, ps):
        self.verify_ps(ps)
        self.__password = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    def print_info(self):
        print('=' * 30)
        print(self.__fio)
        print(self.__old)
        print(self.__password)
        print(self.__weight)
        print('+' * 45)


p1 = UserDate("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
p1.print_info()
p1.fio = "Sobolev Igor Nikolaevich"
print(p1.fio)
p1.print_info()
p1.old = 30
p1.password = '4567 123456'
p1.weight = 70.2
p1.print_info()
print(p1.__dict__)
print()
print()

print("Наследование 1.")
print("Аргументы в Классе Point Используют Вспомогательный Класс Line")


class Point:  # Вспомогательный кЛАСС
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"


class Line:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def draw_line(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")


line = Line(Point(1, 2), Point(10, 20))
line.draw_line()
line = Line(Point(1, 2), Point(10, 20), 'Blue', 20)
line.draw_line()
# rect = Point(Point(20, 40),  Point(10, 20))


print("###########################################################")
print("Наследование 2.")
print("Класс Point Вспомогательные Класс. Line, Rect.\n"
      "Переопределенный Инициализатор Line.\n"
      "Использование Объявления Переменной Protected, Public, Private")
print('-' * 60)


class Point:  # Вспомогательный кЛАСС
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"


class Prop:  # Родительский Класс.
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        print(("Инициализатор Базового Класса Prop"))
        self.sp = sp
        self._ep = ep
        self.__color = color
        self.__width = width

    def get_width(self):
        return self.__width

    def get_color(self):
        return self.__color


class Line(Prop):
    def __init__(self, *args):
        super().__init__(*args)
        print("Переопределенный Инициализатор Line")
        # Prop.__init__(self, *args)
        self.width = 5

    def draw_line(self):
        print(f"Рисование Линии: {self.sp}, {self._ep}, {self.get_color()}, {self.get_width()}")


class Rect(Prop):
    def draw_rect(self):
        print(f"Рисование Прямоугольника: {self.sp}, {self._ep}, {self.get_color()}, {self.get_width()}")


line = Line(Point(1, 2), Point(10, 20))
print(line.__dict__)
# line.draw_line()
# rect = Rect(Point(20, 40),  Point(10, 20))
# rect.draw_rect()
# print(line._width)

# print(issubclass(Prop, object))
# print(issubclass(Line, Prop))
# print(issubclass(Rect, Prop))

print("Продолжение Темы \"Наследование\"")
print("Определение \"Геттеров\" и \"Сеттеров\" в Классе Инициализации свойств")
print("Инициализация в Дочернем Классе с Присвоением Свойств Родительского:\n"
    "def __init__(self, w, h, color): super().__init__(color)")
class Figure:  # Родительский Класс.
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c


class Rectangle(Figure):
    def __init__(self, w, h, color):
        super().__init__(color)
        self.__width = w
        self.__height = h

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError("Вы Ввели Отрицательную Ширину Координаты Прямоугольника.")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError("Вы Ввели Отрицательную Высоту Координаты Прямоугольника.")

    def area(self):
        return self.__width * self.__height


rect = Rectangle(10, 20, "green")
print(rect.area())
print(rect.width)
print(rect.height)
print(rect.color)
rect.color = 'black'
print(rect.color)
