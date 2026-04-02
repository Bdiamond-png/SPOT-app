from sentry_sdk.integrations.google_genai.utils import extract_tool_calls

from spotter.users.models import UserIntake, UserProfile
from spotter.goals.models import UserBaseLine


def profile_creation(profile_info: UserIntake) -> UserProfile:
    new_user = UserProfile(health_grade= 0.0, intake_data=profile_info)
    return new_user


def goals_creation(goals_info: UserBaseLine) -> NewSubject:
#regression and progression button | left and right
#exercise selection button for variants of eligible exercises
