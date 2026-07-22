from spotter.trainer.models import Program
from spotter.subject.services import Subject
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import HTTPException

def create_new_program(subject_to_program:Subject, db: Session) -> Program:
    target_muscle = subject_to_program.subject_goals.target_muscles[0].name
    result = db.execute(text("""
    SELECT DISTINCT em.movement_pattern_id
    FROM exercise_muscles em
    JOIN muscles m ON em.muscles_id = m.id
    WHERE m.muscle_group = :target_muscle AND em.role = 'primary'
    """), {'target_muscle': target_muscle})
    movement_pattern_id = result.scalar()
    if movement_pattern_id is None:
        raise HTTPException(status_code=500, detail=f"No primary movement pattern found for target muscle: {target_muscle}")
