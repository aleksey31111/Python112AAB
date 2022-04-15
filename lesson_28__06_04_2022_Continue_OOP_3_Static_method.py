### LESSON 28
print("Подсчет Метода __init__ - Сколько Экземпляров Класса Было Созданно.")


class Point:
    __count = 0  # Статическое свойство

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point.__count += 1

    ### Point.get_count(p1)
    # def get_count(self):
    #     return Point.__count

    @staticmethod
    def get_count():
        return Point.__count

    # get_count = staticmethod(get_count)


# p1 = Point(5, 4)
# print(p1.count)
# p2 = Point()
# print(p1.count)
# p3 = Point()
# print(p1.count)

# p1 = Point(10, 8)
# p2 = Point(15, 12)
# print(Point.get_count(p1))

p1 = Point(10, 8)
p2 = Point(15, 12)
p3 = Point(20, 16)
print(Point.get_count())
print(Point.get_count())
print(Point.get_count())
# print(p2.get_count())

# ### STATIC METHOD ###
print("### Другой Пример Статического Метода ###")
print("  - Либо Добавлять Еденицу к Классу Либо Удалять.")
print("static method = Функции")


class Change:
    @staticmethod
    def inc(x):
        return x + 1

    @staticmethod
    def dec(x):
        return x - 1


print(Change.inc(10), Change.dec(10))

# #### Task 1 ####
print("Задание 1 Урока 28: Создайте Класс для Подсчета Максимума\n"
      "из 4-х Аргуметов (3, 5, 7, 9), Минимума, Среднеарифметического,\n"
      "Факториала Аргумента (5). Функциональность Необходимо Реализовать\n"
      "в Виде Статических Методов")


class Point:

    @staticmethod
    def max(a, b, c, d):
        if a > b > c > d:
            return a
        elif b > a > c > d:
            return b
        elif c > a > b > d:
            return c
        else:
            return d

    @staticmethod
    def min(a, b, c, d):
        if a < b < c < d:
            return a
        elif b < a < c < d:
            return b
        elif c < a < b < d:
            return c
        else:
            return d

    @staticmethod
    def average(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(x):
        c = 1
        for i in range(1, x + 1):
            c *= 1
        return c


print(Point.max(3, 5, 7, 9))
print(Point.min(3, 5, 7, 9))
print(Point.average(3, 5, 7, 9))
print(Point.factorial(5))

# #### Example 1 ####
print("Пример 1 Урока 28: Класс Конвертирования Температуры\n"
      "Из Цельсия в Фаренгейт и Наоборот. Класс Должен Иметь\n"
      "Два Статических Метода для каждого Конвертирования.\n"
      "Класс Должен считать Количество Подсчетов Температуры и\n"
      "Возвращать Значение с Помощью Статического Метода")


class Temperature:
    counter = 0

    #### ИНИЦИАЛИЗАТОР Лишний
    # def __init__(self, celsius, fahrenheit):
    #     self.celsius = celsius
    #     self.fahrenheit = fahrenheit
    #     Temperature.counter += 1

    @staticmethod
    def fahrenheit(x):
        Temperature.counter += 1
        return round(x * 1.8 + 32, 3)

    @staticmethod
    def celsius(x):
        Temperature.counter += 1
        return round((x - 32) / 1.8, 2)


print(Temperature.fahrenheit(15))
print(Temperature.celsius(47))
print(Temperature.counter)

class Temperatur:
    count = 0

    #### Инициализатор Лишний.
    # def __init__(self):
    #     print("INICIALIZATOR")
    #     Temperatur.count += 1

    @staticmethod
    def faringeit(x):
        Temperatur.count += 1
        return x * 1.8 + 32

    @staticmethod
    def cels(x):
        Temperatur.count += 1
        return (x - 32) / 1.8


print(Temperatur.faringeit(15))
print(Temperatur.faringeit(30))
print(Temperatur.cels(59))
print(Temperatur.count)


class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def string_to_db(self):
        return f"{self.year}-{self.month}-{self.year}"

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('.'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_validate(date_as_string):
        if date_as_string.count('.') == 2:
            day, month, year = map(int, date_as_string.split('.'))
            return day <= 31 and month <= 12 and year <= 3999


dates = [
    '30.12.2020',
    '30-12-2020',
    '01.01.2020',
    '12.31.2020'
]

for string_date in dates:
    if Date.is_date_validate(string_date):
        date = Date.from_string(string_date)
        string_to_db = date.string_to_db()
        print(string_to_db)
    else:
        print("Неправильная Дата или Формат Строки с Датой.")


string_date = "23.10.2021"
# # day, month, year = map(int, string_date.split('.'))
# # print(day, month, year)
# # date = Date(day, month, year)
date = Date.from_string("23.10.2021")
print(date.string_to_db())
# # date2 = Date.from_string("23.10.2021")
# # print(date2.string_to_db())
#
#
# ### Example 2 ###
print("Пример 2 Урока 28 06.04.2022: Создать Класс, Открытие Счета\n"
      "1) Должен Выводится Счет.\n"
      "2) Фамилия Владельца.\n"
      "3) Баланс Счета\n"
      "4) Начисление Процентов.\n"
      "5) Перевод в Доллары и Евро.\n"
      "6) Возможность Положить, Снять Деньги на Счете.\n"
      "7) Сменить Владельца.\n"
      "8) Закрыть Счет.")
class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value=0):
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f"Счеt #{self.num} принадлежащий {self.surname} был открыт.")
        print('*' * 50)

    def __del__(self):
        print("*" * 50)
        print(f'Счет #{self.num} принадлежащий  {self.surname} был закрыт.')

    @classmethod
    def set_usd_rate(cls,rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

    def edit_owner(self, surname):
        self.surname = surname

    def add_percent(self):
        self.value += self.value * self.percent
        print("Проценты были успешно Начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было Успешно снято.")
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix}")

    def print_balance(self):
        print(f"Текущий баланс: {self.value} {Account.suffix}")

    def print_info(self):
        print("Информация О счете:")
        print('-' * 20)
        print(f"#{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
        print('-' * 20)


acc = Account('12345', 'Долгих', 0.03, 1000)
# # print(Account.suffix)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(2)
acc.convert_to_usd()
Account.set_eur_rate(2)
acc.convert_to_eur()
print()
acc.edit_owner("Дюма")
acc.print_info()
print()
acc.add_percent()
print()
acc.withdraw_money(3000)
acc.withdraw_money(100)
print()
acc.add_money(5000)
acc.withdraw_money(3000)
print()
print("=" * 50)
acc = Account('45451', 'Селезнев', 0.005, 1000)
#
#
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счеt #{self.__num} принадлежащий {self.__surname} был открыт.")
#         print('*' * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f'Счет #{self.__num} принадлежащий  {self.__surname} был закрыт.')
#
#     @classmethod
#     def set_usd_rate(cls,rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.__value * self.__percent
#         print("Проценты были успешно Начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было Успешно снято.")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix}")
#
#     def print_balance(self):
#         print(f"Текущий баланс: {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация О счете:")
#         print('-' * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print('-' * 20)
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
