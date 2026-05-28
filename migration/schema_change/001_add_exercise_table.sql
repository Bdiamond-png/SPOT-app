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
