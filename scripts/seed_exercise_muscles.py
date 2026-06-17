from sqlalchemy import text
from collections import defaultdict
from core.database.db_setup import sessionLocal

db = sessionLocal()

movement_pattern_muscle_groups = {

"horizontal_push": [
    ("chest", "primary"),
    ("shoulders", "assisting"),
    ("triceps", "assisting"),
    ("rotator_cuff", "stabilizer"),
],

"horizontal_pull": [
    ("mid_back", "primary"),
    ("lats", "assisting"),
    ("biceps", "assisting"),
    ("forearms", "assisting"),
    ("rotator_cuff", "stabilizer"),
],

"vertical_push": [
    ("shoulders", "primary"),
    ("triceps", "assisting"),
    ("chest", "assisting"),
    ("abs", "stabilizer")
],

"vertical_pull": [
    ("lats", "primary"),
    ("mid_back", "assisting"),
    ("biceps", "assisting"),
    ("forearms", "assisting"),
    ("abs", "stabilizer"),
],

"squat": [
    ("quads", "primary"),
    ("glutes", "assisting"),
    ("hamstrings", "assisting"),
    ("calves", "stabilizer"),
    ("abs", "stabilizer"),
    ("low_back", "stabilizer"),
],

"hinge": [
    ("glutes", "primary"),
    ("hamstrings", "primary"),
    ("low_back", "assisting"),
    ("lats", "stabilizer"),
    ("forearms", "stabilizer"),
    ("abs", "stabilizer"),
]
}

try:
    muscle_lookup = defaultdict(list)
    result = db.execute(text("SELECT id, muscle_group FROM muscles"))
    for row in result:
        muscle_lookup[row.muscle_group].append(row.id)

    pattern_lookup = {}
    result = db.execute(text("SELECT id, name FROM movement_pattern"))
    for row in result:
        pattern_lookup[row.name] = row.id


    for pattern_name, muscle_list in movement_pattern_muscle_groups.items():
        pattern_id = pattern_lookup[pattern_name]

        for group_name, role in muscle_list:
            muscle_ids = muscle_lookup[group_name]
            for muscle_id in muscle_ids:
                db.execute(text("""
                INSERT INTO exercise_muscles (movement_pattern_id, muscles_id, role)
                VALUES (:pattern_id, :muscle_id, :role)
                """),
                {"pattern_id": pattern_id, "muscle_id": muscle_id, "role": role}
                )
    db.commit()
    print("Insertion Successful")
except Exception as e:
    db.rollback()
    print(f"Insertion Failed: {e}")
    raise e
finally:
    db.close()