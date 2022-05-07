class Cat:
    def __init__(self, animal, name, age):
        self.animal = animal
        self.name = name
        self.age = age

    def info(self):
        return f"Меня Зовут: {self.name}. "

    def old_info(self):
        return f"Мне {self.age} лет. "

    def sound(self):
        return f"{self.name} Мяукает. "


# print(__name__)
__author__ = 'Aleksey'
if __name__ == '__main__':
    print(f"Module {__name__} (author: {__author__})")