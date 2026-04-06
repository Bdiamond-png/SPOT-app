from spotter.users.models import UserIntake, UserProfile
import uuid


def profile_creation(profile_info: UserIntake) -> UserProfile:
    new_id = uuid.uuid4()
    new_user = UserProfile(user_id=str(new_id), health_grade= 0.0, intake_data=profile_info)
    return new_user
