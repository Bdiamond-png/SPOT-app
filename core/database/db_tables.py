from enum import Enum

from sqlalchemy import Column, Integer, Float, String

from spotter.users.models import MainGoal


class UserTable(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    experience_level = Enum(ExperienceLevel)
    main_goal = Enum(MainGoal)
    gender = Column(String)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    health_issues = Column(String)
    waist_inches = Column(Float)




