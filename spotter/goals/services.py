from spotter.goals.models import GoalsIntake, GoalsProfile
import uuid


def create_goals(goals_info: GoalsIntake) -> GoalsProfile:
    new_goals_id = uuid.uuid4()
    new_goals = GoalsProfile(goals_id=str(new_goals_id), goals_summary=goals_info, summary_str=f"User focused on{goals_info.training_focus.name}, targeting {[muscle.name for muscle in goals_info.target_muscles]} in {goals_info.time_frame} months & correcting lagging {[muscle.name for muscle in goals_info.lagging_muscles]}")
    return new_goals