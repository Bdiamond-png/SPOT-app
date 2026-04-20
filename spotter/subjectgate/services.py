from fastapi import HTTPException
from spotter.subject.models import Subject
from spotter.users.models import UserProfile, MainGoal
from spotter.goals.models import GoalsProfile, MainFocus


def goals_feasibility(subject_profile: UserProfile, subject_goals: GoalsProfile,db: Session) -> Subject:
    if subject_goals.goals_summary.training_focus == MainFocus.max_upper_body_strength and subject_profile.intake_data.main_goal == MainGoal.GainMuscle:
        raise HTTPException(
            status_code=400,
            detail="You Main Focus and Main Goals are conflicting"
        )
    else:
        return Subject(subject_user=subject_profile, subject_goals=subject_goals)
