from spotter.users.bf_calculator import female_bf_percent, male_bf_percent
from spotter.users.models import UserIntake, UserGender
from core.database.db_tables import Users
import uuid
from sqlalchemy.orm import Session
def profile_creation(profile_info: UserIntake, db: Session) -> Users:
    new_id = uuid.uuid4()
    calculate_bf = 0
    if profile_info.gender == UserGender.Male:
        calculate_bf = male_bf_percent(profile_info.height,profile_info.waist_inches,profile_info.neck_inches)
    if profile_info.gender == UserGender.Female:
        calculate_bf = female_bf_percent(profile_info.height,profile_info.waist_inches,profile_info.neck_inches, profile_info.hip_inches)
    new_db_user = Users(
        id=str(new_id),
        health_grade= 0.0,
        name=profile_info.name,
        age=profile_info.age,
        gender=profile_info.gender,
        height=profile_info.height,
        weight=profile_info.weight,
        experience_level=profile_info.experience_level,
        main_goal=profile_info.main_goal,
        waist_inches=profile_info.waist_inches,
        neck_inches=profile_info.neck_inches,
        hip_inches=profile_info.hip_inches,
        bf_percent=calculate_bf,
        heath_issues=profile_info.heath_issues,
    )
    try:
        db.add(new_db_user)
        db.commit()
        db.refresh(new_db_user)
    except Exception as e:
        db.rollback()
        raise e
    return new_db_user

