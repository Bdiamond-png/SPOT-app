from sentry_sdk.integrations.google_genai.utils import extract_tool_calls

from spotter.users.models import UserIntake, UserProfile


def profile_creation(profile_info: UserIntake) -> UserProfile:
    new_user = UserProfile(health_grade= 0.0, intake_data=profile_info)
    return new_user
