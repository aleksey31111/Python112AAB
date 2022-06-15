from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from model_45.database import Base


association_table = Table('association', Base.metadata,
                          Column('lesson_id', Integer, ForeignKey('lessons.id')),
                          Column('group_id', Integer, ForeignKey('groups.id')))

class Lesson(Base):
    __tablename__ = 'Lesson'

    id = Column(Integer, primary_key=True)
    lesson_ttle = Column(String(250), nullable=False)
    student = relationship("Group")
    groups = relationship("Group", secondary=association_table, backref='group_lesson')

    def __repr__(self):
        return f'Subject (ID: {self.id} {self.lesson_ttle}) '