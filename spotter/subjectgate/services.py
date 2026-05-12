from fastapi import HTTPException
from spotter.subject.models import Subject
from spotter.users.models import MainGoal
from spotter.goals.models import WorkoutStyle

VALID_STYLES = {
    MainGoal.GainMuscle: [WorkoutStyle.body_building],
    MainGoal.LoseWeight: list(WorkoutStyle),
    MainGoal.BuildStrength: [WorkoutStyle.power_lifting, WorkoutStyle.strong_man, WorkoutStyle.olympic_lifting],
    MainGoal.OverallHealth: [WorkoutStyle.calisthenics, WorkoutStyle.body_building, WorkoutStyle.sports_training],
    MainGoal.MaxVert: [WorkoutStyle.sports_training],
    MainGoal.MaxLongJump: [WorkoutStyle.sports_training],
}

def validate_style(subject: Subject) -> None:
    user_goal = subject.subject_user.main_goal
    user_style = subject.subject_goals.training_method

    valid_style = VALID_STYLES.get(user_goal, [])

    if user_style not in valid_style:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid style {user_style}. Must be one of {valid_style}"
        )