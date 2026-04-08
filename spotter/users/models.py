from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

from main import user_subject


class ExperienceLevel(Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3

class MainGoal(Enum):
    LoseWeight = 1
    GainMuscle = 2
    BuildStrength = 3
    MaxVert = 4
    MaxLongJump = 5
    OverallHealth = 6


class UserIntake(BaseModel):
    name: str
    age: int
    gender: str
    height: float
    weight: float
    waist_inches: float
    neck_inches:float
    hip_inches:Optional[float] = None
    experience_level: ExperienceLevel
    health_issues: List[str]
    main_goal: MainGoal

class UserProfile(BaseModel):
    user_id: str
    health_grade: float
    intake_data: UserIntake