from sqlalchemy import text
from core.database.db_setup import sessionLocal

db = sessionLocal()

exercises = [
    {
        "name": "barbell_bench_press",
        "equipment": "barbell",
        "difficulty": "INTERMEDIATE",
        "movement_pattern": "horizontal_push",
        "is_isolation": False,
        "requires_bench": True,
        "requires_spotter": True,
        "hypertrophy_score": 7,
        "strength_score": 10,
        "fatigue_cost": 7,
        "stability_demand": 2,
        "athletic_transfer_score": 5,
    },
]
try:
    pattern_lookup = {}
    result = db.execute(text("SELECT id, name FROM movement_pattern"))
    for row in result:
        pattern_lookup[row.name] = row.id

    for exercise in exercises:
        movement_pattern = exercise["movement_pattern"]
        movement_pattern_id = pattern_lookup[movement_pattern]
        db.execute(text("""
            INSERT INTO exercise (
                name, equipment, difficulty, movement_pattern_id, is_isolation, requires_bench, requires_spotter,
                hypertrophy_score, strength_score, fatigue_cost, stability_demand, athletic_transfer_score
            )
            VALUES (
                :name, :equipment, :difficulty, :movement_pattern_id, :is_isolation, :requires_bench, :requires_spotter,
                :hypertrophy_score, :strength_score, :fatigue_cost, :stability_demand, :athletic_transfer_score
             )
         """),
        {"name": exercise["name"], "equipment": exercise["equipment"], "difficulty": exercise["difficulty"], "movement_pattern_id": movement_pattern_id,
                    "is_isolation": exercise["is_isolation"], "requires_bench":exercise["requires_bench"], "requires_spotter":exercise["requires_spotter"],
                    "hypertrophy_score": exercise["hypertrophy_score"], "strength_score": exercise["strength_score"], "fatigue_cost": exercise["fatigue_cost"],
                    "stability_demand": exercise["stability_demand"], "athletic_transfer_score": exercise["athletic_transfer_score"]
        })
    db.commit()
    print("Insertion Completed")
except Exception as e:
    db.rollback()
    print(f"Insertion Failed: {e}")
    raise e
finally:
    db.close()