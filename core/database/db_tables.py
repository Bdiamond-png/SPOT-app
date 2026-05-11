from sqlalchemy import Enum as SAEnum
from sqlalchemy import Column, Integer, Float, String, ForeignKey, ARRAY
from core.database.db_setup import Base
from spotter.users.models import MainGoal, ExperienceLevel, UserGender
from spotter.goals.models import MainFocus, WorkoutStyle, WorkoutSplit, WorkoutEquipmentUsed, MusclesGroup
from pydantic import ConfigDict

class Users(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    experience_level = Column(SAEnum(ExperienceLevel))
    main_goal = Column(SAEnum(MainGoal))
    gender = Column(SAEnum(UserGender))
    age = Column(Integer, nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    health_issues = Column(ARRAY(String))
    waist_inches = Column(Float, default=0)
    bf_percent = Column(Float, default=0)
    neck_inches = Column(Float, default=0)
    hip_inches = Column(Float, default=0)
    health_grade = Column(Float, nullable=False)


muscle_enum_type = SAEnum(MusclesGroup, name='muscle_enum_type')

class UserGoals(Base):
    __tablename__ = "user_goals"
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    training_focus = Column(SAEnum(MainFocus))
    training_method = Column(SAEnum(WorkoutStyle))
    time_frame = Column(Integer, nullable=False)
    til_failure = Column(Integer, nullable=False)
    lagging_muscles = Column(ARRAY(muscle_enum_type))
    target_muscles = Column(ARRAY(muscle_enum_type))
    last_time_consistent = Column(Integer, default=0)
    days_per_week = Column(Integer, default=0)
    reps_per_compound = Column(Integer, default=0)
    reps_per_isolation = Column(Integer, default=0)
    sets_per_compound = Column(Integer, default=0)
    sets_per_isolation = Column(Integer, default=0)
    exercise_split = Column(SAEnum(WorkoutSplit))
    users_equipment = Column(SAEnum(WorkoutEquipmentUsed))
    reps_in_reserve_for_compound = Column(Integer, default=0)
    reps_in_reserve_for_isolation = Column(Integer, default=0)
    summary_str = Column(String)