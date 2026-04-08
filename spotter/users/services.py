from spotter.users.bf_calculator import female_bf_percent, male_bf_percent
from spotter.users.models import UserIntake, UserProfile, UserGender
import uuid

def profile_creation(profile_info: UserIntake) -> UserProfile:
    new_id = uuid.uuid4()
    calculate_bf = 0
    if profile_info.gender == UserGender.Male:
        calculate_bf = male_bf_percent(profile_info.height,profile_info.waist_inches,profile_info.neck_inches)
    if profile_info.gender == UserGender.Female:
        calculate_bf = female_bf_percent(profile_info.height,profile_info.waist_inches,profile_info.neck_inches, profile_info.hip_inches)
    new_user = UserProfile(user_id=str(new_id), health_grade= 0.0, intake_data=profile_info,bf_percent=calculate_bf)
    return new_user
