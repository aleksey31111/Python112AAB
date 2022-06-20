from faker import Faker  # Модуль для Генерирования Данных в БД

from model_45.database import create_db, Session
from model_45.lesson import Lesson
from model_45.student import Student
from model_45.group import Group


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    lessons_names = ['Математика', 'Программирование', 'Философия', 'Алгоритмы',
                    'Линейная алгебра', 'Статистика', 'Физика']
    group1 = Group(group_name='MDA-7')
    group2 = Group(group_name='MDA-9')
    session.add(group1)
    session.add(group2)

    for key, it in enumerate(lessons_names):
        lesson = Lesson(lesson_title=it)
        lesson.groups.append(group1)
        if key % 2 == 0:
            lesson.groups.append(group2)
        session.add(lesson)

    faker = Faker('ru-Ru')
    group_list = [group1, group2]
    session.commit()

    for _ in range(50):
        full_name = faker.name().split()
        age = faker.random.randint(16, 25)
        group = faker.random.choice(group_list)
        student = Student(full_name, age, group.id)
        session.add(student )

    session.commit()
    session.close()