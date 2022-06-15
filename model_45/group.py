from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model_45.database import Base

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String(250), nullable=False)
    student = relationship('Student')

    def __repr__(self):
        return f'Group (ID'
