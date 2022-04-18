# ### LESSON 31 ###
## Nested Class ##
# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = self.Intern()
#         self.intern = self.Head()
#
#     def show(self):
#         print("Employee List")
#         print(self.name)
#     class Intern:
#         def __init__(self):
#             self.name = 'Smith'
#             self.id = '657'
#
#         def display(self):
#             print("Name:", self.name)
#             print("Id:", self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#             self.id = '657'
#
#         def display(self):
#             print("Name:", self.name)
#             print("Degree:", self.id)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.Intern
# d2 = outer.Head
# d1.display()
# d2.display()


# ### 3 Nested class ###
# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print(("Class Outer"))
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print(("Class Inner"))
#
#         class InerClass:
#             def show(self):
#                 print(("Class InnerClass"))
#
#
# outer = Outer()
# outer.show()
# inner1 = outer.inner
# inner1.show()
# inner2 = outer.inner.inner_inner
# # inner2 = inner1.inner_inner
# inner2.show()


# # Example Nested class #
# class Computer:
#     def __init__(self):
#         self.name = 'pccc'
#         self.CPU = 'cpu'
#         self.OS = "os"
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#
#         def model(self):
#             return 'Core-i7'
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())

# ### Nested Class Inheritance ###
# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print('Class Base')
#
#     class Inner:
#         def display1(self):
#             print("Inner of Base Class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("In Subclass")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Inner Of Subclass')
#
#
# a = SubClass()
# a.display()
#
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()

### Task 1 ###
# class Student:
#     def __init__(self,name1,name2):
#         self.name1 = name1
#         self.name2 = name2
#     def print_info(self):
#         print("Name: ", self.name)
#
#     class Notebook:
#         def options(self, videocard, mp, sound):
#             super().__init__()
#             self.videocard = videocard
#             self.mp = mp
#             self.sound = sound
#
#         def
#
# s1 = Student('Roman')
# s2 = Student('Vladimir')
# s1.show()
# s2.show()

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#     def show(self):
#         print(self.name, '==>', self.note.cpu, self.note.model, self.note.memory )
#     class Notebook:
#         def __init__(self):
#             self.model= 'HP'
#             self.cpu= 'i7'
#             self.memory='16'
# s1=Student('Roman')
# s1.show()
# s2 = Student('Vladimir')
# s2.show()

#
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#     def show(self):
#         print(self.name, end=' ')
#         self.note = self.Notebook()
#     class Notebook:
#         def __init__(self):
#             self.model= 'HP'
#             self.cpu= 'i7'
#             self.memory='16'
#
#         def show(self):
#             print(, self.note.cpu, self.note.model, self.note.memory )
#
#
# s1=Student('Roman')
# s1.show()
# s2 = Student('Vladimir')
# s2.show()


# print('#############################################################################################')
# print('#############################################################################################')
# print("\t\t\tМножественное Наследование")
# print('#############################################################################################')
# print('#############################################################################################')
# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' is sleeping')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + ' is playing')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# d = Dog("Buddy")
# d.sleep()
# d.play()
# d.bark()

# # Example 2 #
# class A:
#     def __init__(self):
#         print(("Inicializator A"))
#
#
# class B(A):
#     def __init__(self):
#         print("Inicializator B")
#
#
# class C(A):
#     def __init__(self):
#         print("Inicializator C")
#
#
# class D(B, C):
#     def __init__(self):
#         super().__init__()
#         C.__init__(self)
#         print("Inicializator D")
#         b.__init__(self)
#
# d = D()

# class A:
#     # def __init__(self):
#     #     print(("Inicializator A"))
#     def hi(self):
#         print("A")
#
# class B(A):
#     # def __init__(self):
#     #     print("Inicializator B")
#     def hi(self):
#         print("B")
#
# class C(A):
#     # def __init__(self):
#     #     print("Inicializator C")
#     def hi(self):
#         print("C")
#
# class D(B, C):
#     # def __init__(self):
#         # super().__init__()
#         # C.__init__(self)
#         # print("Inicializator D")
#         # b.__init__(self)
#         pass
#
# d = D()
# d.hi()
# print(D.mro())


# class A:
#     # def __init__(self):
# #         print(("Inicializator A"))
#     def hi(self):
#         print("A")
#
# class AA(A):
#     def hi(self):
#         print("AA")
#
# class B(A):
#     # def __init__(self):
#     #     print("Inicializator B")
#     def hi(self):
#         print("B")
#
# class C(A):
#     # def __init__(self):
#     #     print("Inicializator C")
#     def hi(self):
#         print("C")
#
# class D(B, C):
#     # def __init__(self):
#         # super().__init__()
#         # C.__init__(self)
#         # print("Inicializator D")
#         # b.__init__(self)
#         def call_hi(self):
#             C.hi(self)
#
# d = D()
#
# d.call_hi()
# print(D.mro())

#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y}"
#
#
# class Style:
#     def __init__(self, color="red", width=1):
#         print("Initialize Style")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Init Pos")
#         self._sp = sp
#         self._ep = ep
#         Style.__init__(self, *args)
#
#
# class Line(Pos, Style):
#     def draw(self):
#         print(f"Drawing line: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()



# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y}"
#
#
# class Style:
#     def __init__(self):
#         print("Initialize Style")
#         # super().__init__()
#
#
# class Pos:
#     def __init__(self):
#         print("Init Pos")
#
#         # Style.__init__(self, *args)
#         # super().__init__()
#
# class Line(Pos, Style)
#     def __init__(self, sp: Point, ep: Point, color="red", width=1):
#         self._sp = sp
#         self._ep = ep
#         self.__x = x
#         self.__y = y
#         super().__init__()
#     def draw(self):
#         print(f"Drawing line: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()


# print('%' * 99)
# print('%' * 99)
# print('%' * 99)
# print('\t\t\t\t\t###### Миксины (примеси) )######')
# print('%' * 99)
# print('%' * 99)
# print('%' * 99)
#
# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename,'a') as fh:
#             fh.write(message)
#
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename="subclasslog.txt")
#
#
#
# subclass = MySubClass()
# subclass.display("Эта строка будет Отображаться и Записываться в Файл")



# class Goods:
#     def __init__(self, name, weidht,price):
#         # super(Goods, self).__init__()
#         super().__init__()
#         print(" Initializator Goods")
#         self.name = name
#         self.weight = weidht
#         self.price = price
#
#     def print_info(self):
#         print(f'{self.name},{self.weight},{self.price}')
#
# class MixinLog:
#     ID = 0
#
#
#     def __init__(self):
#         print("Initializator MixinLog")
#         self.ID += 1
#         self.id = self.ID
#
#     def save_sell_log(self):
#         print(f'{self.id}: goods was sell at 00:00 hour.')
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# print(NoteBook.mro())

print('%' * 79)
print("\t\t\tПерегрузка Операторов")
print('%' * 79)
class Clock:
    __DAY = 86400 # 24 * 60 * 50 Число секунд в Дне.

    def __init__(self, sec: int):
        if not isinstance(sec,int):
            raise ValueError("Second Must Be Int")

        self.__sec = sec % self.__DAY


    def get_format_time(self):
        s = self.__sec % 60
        m = (self.__sec // 60) % 60
        h = (self.__sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"



    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" +str(x)

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