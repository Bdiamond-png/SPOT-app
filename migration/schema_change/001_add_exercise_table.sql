CREATE TYPE public.movementpattern AS ENUM ('horizontal_pull','vertical_pull',
'horizontal_push', 'vertical_push','squat', 'hinge', 'unilateral', 'isometric',
'transverse', 'plyometric');

CREATE TABLE exercise (
    ID UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50) NOT NULL,
    movement_pattern public.movement_pattern,
    equipment public.workoutequipmentused,
    difficulty public.experiencelevel,
    primary_muscle public.muscle_enum_type,
    assisting_muscles public.muscle_enum_type[],
    is_isolation BOOLEAN
);

ALTER TABLE exercise ADD COLUMN weight_score INT CHECK (weight_score BETWEEN 1 AND 100)
ALTER TABLE exercise ADD COLUMN hypertrophy_score INT CHECK (hypertrophy_score BETWEEN 1 AND 10);
ALTER TABLE exercise ADD COLUMN strength_score INT CHECK (strength_score BETWEEN 1 AND 10);
ALTER TABLE exercise ADD COLUMN fatigue_cost INT CHECK (fatigue_cost BETWEEN 1 AND 10);
ALTER TABLE exercise ADD COLUMN stability_demand INT CHECK (stability_demand BETWEEN 0 AND 3);
ALTER TABLE exercise ADD COLUMN skill_requirement public.experiencelevel;
ALTER TABLE exercise ADD COLUMN athletic_transfer_score INT CHECK (athletic_transfer_score BETWEEN 1 AND 10);
ALTER TABLE exercise ADD COLUMN requires_bench BOOLEAN NOT NULL DEFAULT FALSE;
ALTER TABLE exercise ADD COLUMN requires_spotter BOOLEAN NOT NULL DEFAULT FALSE;

CREATE TYPE public.relationship_type AS ENUM ('progression', 'regression', 'equal_level');

CREATE TABLE exercise_relationships (
    ID UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    exercise_id UUID REFERENCES exercise(id),
    related_exercise_id UUID REFERENCES exercise(id),
    exercise_relationship_type public.relationship_type
);