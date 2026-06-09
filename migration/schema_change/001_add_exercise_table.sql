CREATE TABLE exercise (
    ID UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50) NOT NULL,
    movement_pattern public.movementpattern,
    equipment public.workoutequipmentused,
    difficulty public.experiencelevel,
    is_isolation BOOLEAN,
);

ALTER TABLE exercise ADD COLUMN weight_score INT CHECK (weight_score BETWEEN 1 AND 100);
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
    exercise_id UUID REFERENCES exercise(id) ON DELETE CASCADE,
    related_exercise_id UUID REFERENCES exercise(id) ON DELETE CASCADE,
    exercise_relationship_type public.relationship_type
);

CREATE TABLE workout_styles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE exercise_workout_style_scores (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    exercise_id UUID NOT NULL REFERENCES exercise(id) ON DELETE CASCADE,
    workout_style_id UUID NOT NULL REFERENCES workout_styles(id) ON DELETE CASCADE,
    score INT NOT NULL CHECK(score BETWEEN 0 AND 10),
    UNIQUE(exercise_id, workout_style_id)
);