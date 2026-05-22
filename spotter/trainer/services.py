from spotter.trainer.models import Program
from spotter.subject.services import Subject
from sqlalchemy.orm import Session

def create_new_program(subject_to_program:Subject, db: Session) -> Program:


# Based on everything you've designed — the tree, the circuit rules,
# the consistency logic — write out the ordered steps the function needs
# to execute to build a Program from a Subject.
#