from fastapi import HTTPException
from spotter.subject.models import Subject
from core.database.db_tables import Users, UserGoals
from sqlalchemy.orm import Session


def goals_feasibility(subject_profile: Users, subject_goals: UserGoals, db: Session) -> Subject:
    if subject_goals is None:
        raise HTTPException(status_code=404, detail="No goals available")
    if subject_profile is None:
        raise HTTPException(status_code=404, detail="No subject profile available")
    if subject_profile.main_goal == subject_goals.training_focus:

