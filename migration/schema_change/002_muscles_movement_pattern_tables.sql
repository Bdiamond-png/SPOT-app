CREATE TYPE public.role AS ENUM ('primary', 'assisting', 'stabilizer');

CREATE TABLE muscles (
    ID UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50) NOT NULL,
    muscle_group VARCHAR(50)
);

CREATE TABLE movement_pattern (
    ID UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50) NOT NULL
);

CREATE TABLE exercise_muscles (
    ID UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    muscles_id UUID,
    movement_pattern_id UUID,
    role public.role,
    FOREIGN KEY (muscles_id) REFERENCES muscles(id) ON DELETE CASCADE,
    FOREIGN KEY (movement_pattern_id) REFERENCES movement_pattern(id) ON DELETE CASCADE
);