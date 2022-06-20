import os
from sqlalchemy import and_, or_, not_, desc, func, distinct
from database import DATABASE_NAME, Session

from model_45 import create_database_45 as db_creator
from model_45.lesson import Lesson,association_table
from model_45.student import Student
from model_45.group import Group
if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
    # print(session.query(Lesson).all())
    # print('*' * 60)
    # for it in session.query(Lesson):
    #     print(it)
    # print('*' * 60)
    # print(session.query(Lesson).count())
    # print('*' * 60)
    # print(session.query(Lesson).first())
    # print('*' * 60)
    # print(session.query(Lesson).get())
    # print('*' * 60)
    # for it in session.query(Lesson).filter(and_(Lesson.id>=3,Lesson.lesson_title.like('Ф%'))):
    #     print(it)
    # print("*" * 60)
    # for it in session.query(Lesson.lesson_title, Group.group_name).filter(and_
    # (association_table.c.lesson_id == Lesson.id, association_table.c.group_id ==
    #  Group.id, Group.group_name == 'MDA-9')):
    #     print(it)
    # print("*" * 60)
    # for it in session.query(Lesson).filter(or_(Lesson.id>=3,Lesson.lesson_title.like('Ф%'))):
    #     print(it)
    # print("*" * 60)
    # for it in session.query(Lesson).filter(not_(Lesson.id>=3),not_(Lesson.lesson_title.like('М%'))):
    #     print(it)
    # print("*" * 60)
    #
    # print(session.query(Lesson).filter(Lesson.lesson_title is None).all())
    # print('*' * 60)
    #
    # print(session.query(Lesson).filter(Lesson.lesson_title is not None).all())
    # print('*' * 60)
    #
    # print(session.query(Lesson).filter(Lesson.lesson_title.in_(['Математика', 'Линейная алгебра'])).all())
    # print('*' * 60)
    # print(session.query(Lesson).filter(Lesson.lesson_title.notin_(['Математика', 'Линейная алгебра'])).all())
    # print('*' * 60)
    #
    # print(session.query(Student).filter(Student.age.between(16, 17)).all())
    # print('*' * 60)
    #
    # print(session.query(Student).filter(not_(Student.age.between(17, 24))).all())
    # print('*' * 60)
    #
    # for it in session.query(Student).filter(Student.age.like("1%")).limit(4).offset(3):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(Student).order_by(Student.surname):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(Student).order_by(desc(Student.surname)):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(Student).join(Group).filter(Group.group_name == 'MDA-7'):
    #     print(it)
    # print("*" * 60)

    #
    # for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(
    #     Group.group_name).having(func.count(Student.surname) < 25):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(distinct(Student.age)):
    #     print(it)
    # print("*" * 60)
    #
    # for it in session.query(Student.age).distinct():
    #     print(it)
    # print("*" * 60)

    # for it in session.query(Lesson):
    #     print(it)
    #
    #
    # i = session.query(Lesson).get(7)
    # i.lesson_title = "Информатика"
    # session.add(i)
    # session.commit()
    # for it in session.query(Lesson):
    #     print(it)
    # print("*" * 60)

    # for it in session.query(Lesson):
    #     print(it)
    # print("*" * 60)
    #
    # session.query(Lesson).filter(Lesson.lesson_title('%м%')).update({'lesson_title': "M"}, \
    # synchronize_session='fetch)'
    # session.commit()
    # for it in session.query(Lesson):
    #     print(it)
    # print("*" * 60)



    # for it in session.query(Lesson):
    #     print(it)
    # print("*" * 60)
    # session.add(Lesson(lesson_title="Физика"))
    # session.commit()
    # for it in session.query(Lesson):
    #     print(it)
    # print("*" * 60)


    # for it in session.query(Lesson):
    #     print(it)
    # print("*" * 60)
    # i = session.query(Lesson).filter(Lesson.lesson_title == "Физика").one()
    # # print(i)
    # session.delete(i)
    # session.commit()
    # for it in session.query(Lesson):
    #     print(it)
    # print("*" * 60)


    # for it in session.query(Student).filter(text("surname like 'М%'")).\
    # order_by(text("name, id desc")):
    #     print(it)
    # print("*" * 60)





################### COPY ##########################
# import os
#
# from models.database import DATABASE_NAME, Session
# import create_database as db_creator
#
# from models.lesson import Lesson, association_table
# from models.student import Student
# from models_45.group import Group
#
# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()
###########################################################


###### Flask #############
#pip install Flask