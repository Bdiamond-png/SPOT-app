from spotter.goals.models import GoalsIntake
import uuid
from sqlalchemy.orm import Session
from core.database.db_tables import UserGoals

def create_goals(user_id: str, goals_info: GoalsIntake, db: Session) -> UserGoals:
    new_goals_id = uuid.uuid4()
    new_goals = UserGoals(
        user_id=user_id,
        id=str(new_goals_id),
        reps_per_compound=goals_info.new_subject.exercise_volume.reps_per_compound,
        reps_per_isolation=goals_info.new_subject.exercise_volume.reps_per_isolation,
        sets_per_compound=goals_info.new_subject.exercise_volume.sets_per_compound,
        sets_per_isolation=goals_info.new_subject.exercise_volume.sets_per_isolation,
        reps_in_reserve_for_compound=goals_info.new_subject.exercise_volume.reps_in_reserve_for_compound,
        reps_in_reserve_for_isolation=goals_info.new_subject.exercise_volume.reps_in_reserve_for_isolation,
        how_many_reps_til_failure=goals_info.til_failure,
        workout_equipment_used=goals_info.new_subject.users_equipment,
        workout_split=goals_info.new_subject.exercise_split,
        workout_style=goals_info.new_subject.training_method,
        user_last_time_consistent=goals_info.new_subject.last_time_consistent,
        workout_days_per_week=goals_info.new_subject.days_per_week,
        main_area_of_focus=goals_info.training_focus.name,
        target_muscles=[m.name for m in goals_info.target_muscles],
        lagging_muscles=[m.name for m in goals_info.lagging_muscles],
        time_frame_to_reach_goals=goals_info.time_frame,
        summary_str=f"User focused on {goals_info.training_focus.name}, targeting {[muscle.name for muscle in goals_info.target_muscles]} in {goals_info.time_frame} months & correcting lagging {[muscle.name for muscle in goals_info.lagging_muscles]}",

    )
    db.add(new_goals)
    db.commit()
    db.refresh(new_goals)
    return new_goals