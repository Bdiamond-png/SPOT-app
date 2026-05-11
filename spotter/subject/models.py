from pydantic import BaseModel
from pydantic import ConfigDict
from spotter.users.models import UserIntake
from spotter.goals.models import GoalsIntake


class Subject(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        from_attributes=True
    )
    subject_user: UserIntake
    subject_goals: GoalsIntake
    