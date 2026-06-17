from spotter.trainer.models import Program
from spotter.subject.services import Subject
from sqlalchemy.orm import Session

def create_new_program(subject_to_program:Subject, db: Session) -> Program:
    pass