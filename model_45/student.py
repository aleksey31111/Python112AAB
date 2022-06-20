from sqlalchemy import Column, ForeignKey, Integer, String

from model_45.database import Base


class Student(Base):
    __tablename__ = 'student'  # Имя таблицы

    # Набор полей
    id = Column(Integer, primary_key=True)  # Поле ID
    surname = Column(String(250), nullable=False)  # Поле surname; nullable=False -
    # - Поля Одязательные для заполнения
    name = Column(String(250), nullable=False)  # Поле name
    patronymic = Column(String(250), nullable=False)  # Поле patronymic
    age = Column(Integer)  # Поле age
    group = Column(Integer, ForeignKey('groups.id'))  # Поле group
                                # Внешний ключ Связанный с Полем groups.id

    def __init__(self, full_name, age, id_group):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.age = age
        self.group = id_group

    def __repr__(self):
        return f"Студент (ФИО: {self.surname} {self.name} {self.patronymic})" \
               f"Возраст: {self.age}, ID группы: {self.group}"
