from pydantic import BaseModel

from spotter.goals.models import GoalsProfile
from spotter.users.models import UserProfile


class Subject(BaseModel):
    subject_user: UserProfile
    subject_goals: GoalsProfile
    