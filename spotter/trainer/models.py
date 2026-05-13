from typing import List

from pydantic import BaseModel
from enum import Enum


class MovementPattern(Enum):
    horizontal_pull = 1
    vertical_pull = 2
    horizontal_push = 3
    vertical_push = 4
    squat = 5
    hinge = 6
    unilateral = 7
    isometric = 8
    transverse = 9
    plyometric = 10


class ExerciseDesignation(Enum):
    A = 1
    B = 2

class Exercise(BaseModel):
    name: str
    movement_pattern: MovementPattern
    exercise_designation: ExerciseDesignation
    sets: int
    reps: int

class Circuit(BaseModel):
    exercise_a1: Exercise
    exercise_a2: Exercise
    exercise_b1: Exercise

class Session(BaseModel):
    session_id: str
    abs: str # needs a model
    circuits: List[Circuit]
    cardio: str # needs a model


class Program(BaseModel):
    username: str
    sessions: List[Session]
    progressive_overload: str # needs a model just like abs and cardio
    prehab_movements: List[str] # needs a models just like abs and cardio
    program_length: int