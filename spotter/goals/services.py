from spotter.goals.models import GoalsIntake
import uuid
from sqlalchemy.orm import Session
from core.database.db_tables import UserGoals

def create_goals(user_id: str, goals_info: GoalsIntake, db: Session) -> UserGoals:
    new_goals_id = uuid.uuid4()
    new_goals = UserGoals(
        user_id=user_id,
        id=str(new_goals_id),
        reps_per_compound=goals_info.reps_per_compound,
        reps_per_isolation=goals_info.reps_per_isolation,
        sets_per_compound=goals_info.sets_per_compound,
        sets_per_isolation=goals_info.sets_per_isolation,
        reps_in_reserve_for_compound=goals_info.reps_in_reserve_for_compound,
        reps_in_reserve_for_isolation=goals_info.reps_in_reserve_for_isolation,
        til_failure=goals_info.til_failure,
        users_equipment=goals_info.users_equipment,
        exercise_split=goals_info.exercise_split,
        training_method=goals_info.training_method,
        last_time_consistent=goals_info.last_time_consistent,
        days_per_week=goals_info.days_per_week,
        training_focus=goals_info.training_focus.name,
        target_muscles=[m.name for m in goals_info.target_muscles],
        lagging_muscles=[m.name for m in goals_info.lagging_muscles],
        time_frame=goals_info.time_frame,
        summary_str=f"User focused on {goals_info.training_focus.name}, targeting {[muscle.name for muscle in goals_info.target_muscles]} in {goals_info.time_frame} months & correcting lagging {[muscle.name for muscle in goals_info.lagging_muscles]}",

    )
    db.add(new_goals)
    db.commit()
    db.refresh(new_goals)
    return new_goals