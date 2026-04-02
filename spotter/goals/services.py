from spotter.goals.models import GoalsIntake, GoalsProfile

def create_goals(goals_info: GoalsIntake) -> GoalsProfile:
    new_goals = GoalsProfile(goals_summary=goals_info, summary_str=f"User focused on{goals_info.training_focus}, targeting {goals_info.target_muscles} in {goals_info.time_frame} months & correcting lagging {goals_info.lagging_muscles}")
    return new_goals