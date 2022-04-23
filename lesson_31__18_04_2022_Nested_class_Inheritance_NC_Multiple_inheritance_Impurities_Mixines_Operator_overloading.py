# ### LESSON 31 ###
## Nested Class ##
class Employee:
    def __init__(self):
        self.name = 'Employee'
        self.intern = self.Intern()
        self.head = self.Head()

    def show(self):
        print("Employee List")
        print(self.name)

    class Intern:
        def __init__(self):
            self.name = 'Smith'
            self.id = '657'

        def display(self):
            print("Name:", self.name)
            print("Id:", self.id)

    class Head:
        def __init__(self):
            self.name = 'Alba'
            self.id = '007'

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.id)


outer = Employee()
outer.show()

d1 = outer.intern
d2 = outer.head
d1.display()
d2.display()
print()

print('@' * 77)
print("Example 2: Three Nested Class")
print('@' * 77)


# ### 3 Nested class ###
class Outer:
    def __init__(self):
        self.inner = self.Inner()

    def show(self):
        print("Class Outer")

    class Inner:
        def __init__(self):
            self.inner_inner = self.InnerClass()

        def show(self):
            print(("Class Inner"))

        class InnerClass:
            def show(self):
                print(("Class InnerClass"))


outer = Outer()
outer.show()
inner1 = outer.inner
inner1.show()
# inner2 = outer.inner.inner_inner
inner2 = inner1.inner_inner
inner2.show()
print()

print('@' * 87)
print("# # Example Nested class #")
print('@' * 87)


class Computer:
    def __init__(self):
        self.name = 'PC001'
        self.os = self.OS()
        self.cpu = self.CPU()

    class OS:
        def system(self):
            return "Windows 10"

    class CPU:
        def make(self):
            return 'Intel'

        def model(self):
            return 'Core-i7'


comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
my_os = Computer.OS()
my_cpu = Computer.CPU()

print(comp.name)
print(my_os.system())
print(my_cpu.make())
print(my_cpu.model())
print()

print('@' * 67)
print("# ### Nested Class Inheritance ###")
print('@' * 87)


class Base:
    def __init__(self):
        self.db = self.Inner()

    def display(self):
        print('Class Base')

    class Inner:
        def display1(self):
            print("Inner of Base Class")


class SubClass(Base):
    def __init__(self):
        print("In Subclass")
        super().__init__()

    class Inner(Base.Inner):
        def display2(self):
            print('Inner Of Subclass')


a = SubClass()
a.display()

# b = a.db
b = SubClass.Inner()
b.display1()
b.display2()
print()

print('^' * 57)
print("### Task 1 ### Lesson 31 lekture 61:\n"
      "1 - Создать класс Student, Содержащий Имя и Распечатывать Инфо\n"
      "2 - Вложенный класс, Содержащий Инфо о Ноутбуке с Тех Хар-миЖ Модель, Процесор и Память.")
print('^' * 57)


class Student:
    def __init__(self, name):
        self.name = name
        self.note = self.Notebook()

    def show(self):
        print(f"{self.name} ==> {self.note.cpu} {self.note.model} {self.note.memory}")

    class Notebook:
        def __init__(self):
            # super().__init__()
            self.model = 'HP'
            self.cpu = 'i7'
            self.memory = '16'


s1 = Student('Roman')
s2 = Student('Vladimir')
s1.show()
s2.show()
print("Variant 2")


class Student:
    def __init__(self, name):
        self.name = name
        self.note = self.Notebook()

    def show(self):
        print(self.name, end="")
        self.note.show()

    class Notebook:
        def __init__(self):
            self.model = 'HP'
            self.cpu = 'i7'
            self.memory = '16'

        def show(self):
            print(f"==> {self.cpu} {self.model} {self.memory}")


s1 = Student('Roman')
s1.show()
s2 = Student('Vladimir')
s2.show()
print()

print('#############################################################################################')
print("\t\t\tМножественное Наследование")
print('#############################################################################################')


class Creature:
    def __init__(self, name):
        self.name = name


class Animal(Creature):
    def sleep(self):
        print(self.name + ' is sleeping')


class Pet(Creature):
    def play(self):
        print(self.name + ' is playing')


class Dog(Animal, Pet):
    def bark(self):
        print(self.name + " is barking")


d = Dog("Buddy")
d.sleep()
d.play()
d.bark()
print()

print('$' * 82)
print("# # Example 2 # Конфликты с Одинаковыми Именами В Множественном Наследовании. №")
print('$' * 82)


class A:
    # def __init__(self):
    #     print(("Инициализатор Класса A"))
    def hi(self):
        print("A")


class B(A):
    # def __init__(self):
    #     print("Инициализатор Класса B")
    def hi(self):
        print("B")


class C(A):
    # def __init__(self):
    #     print("Инициализатор Класса C")
    def hi(self):
        print("C")


class D(B, C):
    # def __init__(self):
    #     # super().__init__()
    #     C.__init__(self)
    #     print("Инициализатор Класса D")
    #     B.__init__(self)
    pass


d = D()
d.hi()
print(D.mro())
print()

print('$' * 82)
print("Variant 2")
print("# # Example 2 # Конфликты с Одинаковыми Именами В Множественном Наследовании. №")
print('$' * 82)


# class A:
#    # def __init__(self):
#    #     print(("Inicializator A"))
# def hi(self):
#     print("A")

class B:
    # def __init__(self):
    #     print("Inicializator B")
    def hi(self):
        print("B")


class C:
    # def __init__(self):
    #     print("Inicializator C")
    def hi(self):
        print("C")


class D(B, C):
    # def __init__(self):
    # super().__init__()
    # C.__init__(self)
    # print("Inicializator D")
    # b.__init__(self)
    pass


d = D()
d.hi()
print(D.mro())
print()

print('$' * 82)
print("Variant 3")
print("# # Example 2 # Конфликты с Одинаковыми Именами В Множественном Наследовании. №")
print('$' * 82)


class A:
    # def __init__(self):
    #         print(("Inicializator A"))
    def hi(self):
        print("A")


class AA:
    def hi(self):
        print("AA")


class B(A):
    # def __init__(self):
    #     print("Inicializator B")
    def hi(self):
        print("B")


class C(AA):
    # def __init__(self):
    #     print("Inicializator C")
    def hi(self):
        print("C")


class D(B, C):
    # def __init__(self):
    # super().__init__()
    # C.__init__(self)
    # print("Inicializator D")
    # b.__init__(self)
    def call_hi(self):
        C.hi(self)

    pass


d = D()
d.call_hi()
print(D.mro())
# d.call_hi()
# print(D.mro())
print()

print('!' * 32)
print("# # Example 2 # Поимер Множественного Наследования. ")
print('!' * 32)


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y}"


class Style:
    def __init__(self, color="red", width=1):
        print("Инициализатор Style")
        self._color = color
        self._width = width


class Pos:
    def __init__(self, sp: Point, ep: Point, *args):
        print("Инициализатор Pos")
        self._sp = sp
        self._ep = ep
        Style.__init__(self, *args)


class Line(Pos, Style):
    def draw(self):
        print(f"Рисование Линии: {self._sp}, {self._ep}, {self._color}, {self._width}")


l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
l1.draw()

print("Variant 2")


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y}"


class Style:
    def __init__(self):
        print("Инициализатор Style")
        # super().__init__()


class Pos:
    def __init__(self):
        print("Инициализатор Pos")
        super().__init__()


class Line(Pos, Style):
    def __init__(self, sp: Point, ep: Point, color="red", width=1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width
        super().__init__()

    def draw(self):
        print(f"Drawing line: {self._sp}, {self._ep}, {self._color}, {self._width}")


l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
l1.draw()

print('%' * 99)
print('\t\t\t\t\t###### Миксины (примеси) - Предоставление Методов )######')
print("\t\t\t\t\t Миксины - Родительский Класс")
print('%' * 99)


class Displayer:
    @staticmethod
    def display(message):
        print(message)


class LoggerMixin:
    def log(self, message, filename="logfile.txt"):
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        Displayer.display(message)
        self.log(message)


class MySubClass(LoggerMixin, Displayer):
    def log(self, message, filename=''):
        super().log(message, filename="subclasslog.txt")


subclass = MySubClass()
subclass.display("Эта строка будет Отображаться и Записываться в Файл")
print()

print('%' * 99)
print("Пример Миксинов")
print('%' * 99)


class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        #         super().__init__()
        print("Инициализатор Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name},{self.weight},{self.price}')


class MixinLog:
    ID = 0

    def __init__(self):
        print("Инициализатор MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f'{self.id}: товар был продан в 00:00 часрв.')


class NoteBook(Goods, MixinLog):
    pass


n = NoteBook("HP", 1.5, 35000)
n.print_info()
n.save_sell_log()
print(NoteBook.mro())

print('%' * 79)
print("\t\t\tПерегрузка Операторов")
print('%' * 79)


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


# c1 = Clock(100)
c2 = Clock(200)
c4 = Clock(200)
# c3 = c1 + c2 + c4
c4 += c2
# print(c1.get_format_time())
# print(c2.get_format_time())
print(c4.get_format_time())
# print(c3.get_format_time())
