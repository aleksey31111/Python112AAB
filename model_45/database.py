from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  # creat Requests
from sqlalchemy.orm import sessionmaker  # Work with Network

### BD
DATABASE_NAME = 'students.db'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Session = sessionmaker(bind=engine)  # Сщздает запросы в одной СЕСИИ для Работы сDB
Base = declarative_base()  # Create Table in BD


### Возможность Добавлять Классы в Виде Таблиц Созданной Базы Данных ###
def create_db():
    Base.metadata.create_all(engine)
