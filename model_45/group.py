from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship  # Межтабличные отношения Не Влияя на ДБ

from model_45.database import Base

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)  # Поле ID Первичный ключ
    group_name = Column(String(250), nullable=False)
    student = relationship('Student')  # Связь Student.group С Group.id

    def __repr__(self):
        return f"Группа (ID: {self.id}, Название: {self.group_name})"
