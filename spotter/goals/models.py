from pydantic import BaseModel, ConfigDict
from enum import Enum
from typing import List



class WorkoutEquipmentUsed(Enum):
    machines = 1
    bodyweight = 2
    kettlebell = 3
    resistance_bands = 4
    cables = 5
    barbell = 6
    dumbbell = 7
    pull_up_bar = 8
    mixed_workout_equipment = 9

class WorkoutSplit(Enum):
    push_pull_legs = 1
    upper_lower = 2
    full_body = 3
    bro_split = 4
    hybrid_split = 5

class WorkoutStyle(Enum):
    calisthenics = 1
    body_building = 2
    power_lifting = 3
    olympic_lifting = 4
    sports_training = 5
    combat_sports_training = 6
    strong_man = 7

class MainFocus(Enum):
    max_upper_body_strength = 1
    max_upper_body_muscle_growth = 2
    max_endurance = 3
    max_lower_body_strength = 4
    max_lower_body_muscle_growth = 5
    max_jump = 6
    max_sprint = 7

class MusclesGroup(Enum):
    chest = 1
    shoulders = 2
    triceps = 3
    lats = 4
    mid_back = 5
    biceps = 6
    forearms = 7
    glutes = 8
    hamstrings = 9
    quads = 10
    calves = 11
    abs = 12
    low_back = 13
    traps = 14
    hip_flexors = 15
    obliques = 16
    rotator_cuff = 17

class GoalsIntake(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )
    last_time_consistent: int
    days_per_week: int
    reps_per_compound: int
    reps_per_isolation: int
    sets_per_compound: int
    sets_per_isolation: int
    reps_in_reserve_for_compound: int
    reps_in_reserve_for_isolation: int
    users_equipment: WorkoutEquipmentUsed
    exercise_split: WorkoutSplit
    training_method: WorkoutStyle
    time_frame: int
    til_failure: int
    lagging_muscles: List[MusclesGroup]
    target_muscles: List[MusclesGroup]
    training_focus: MainFocus

class GoalsProfile(BaseModel):
    goals_id: str
    goals_summary: GoalsIntake
    summary_str: str