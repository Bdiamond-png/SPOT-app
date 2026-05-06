from fastapi import HTTPException
from sqlalchemy import select
from core.database.db_tables import Users, UserGoals
from spotter.subject.models import Subject
from spotter.users.models import UserIntake
from spotter.goals.models import GoalsIntake

def merge_into_subject(user_id: str, db):
    stmt = select(Users).where(Users.id == user_id)
    result = db.execute(stmt)
    subject_user = result.scalars().first()
    stmt = select(UserGoals).where(UserGoals.user_id == user_id)
    result = db.execute(stmt)
    subject_goals = result.scalars().first()
    if subject_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if subject_goals is None:
        raise HTTPException(status_code=404, detail="Goals not found")
    merged_subject = Subject(
        subject_user=UserIntake.model_validate(subject_user),
        subject_goals=GoalsIntake.model_validate(subject_goals),
    )
    return merged_subject