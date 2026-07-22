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
CREATE TYPE public.muscles_type AS ENUM ('lagging', 'target');

CREATE TABLE user_goal_muscles (
    ID UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    goals_id UUID,
    muscles_id UUID,
    muscles_type public.muscles_type,
    FOREIGN KEY (muscles_id) REFERENCES muscles(id) ON DELETE CASCADE,
    FOREIGN KEY (goals_id) REFERENCES user_goals(id) ON DELETE CASCADE
);

ALTER TABLE exercise DROP COLUMN movement_pattern;
ALTER TABLE exercise DROP COLUMN primary_muscles;
ALTER TABLE exercise DROP COLUMN assisting_muscles;
ALTER TABLE user_goals DROP COLUMN target_muscles;
ALTER TABLE user_goals DROP COLUMN lagging_muscles;
ALTER TABLE exercise ADD COLUMN movement_pattern_id UUID REFERENCES movement_pattern(id) ON DELETE CASCADE;
ALTER TABLE exercise ADD COLUMN exercise_muscles_id UUID REFERENCES exercise_muscles(id) ON DELETE CASCADE;

ALTER TABLE movement_pattern ADD COLUMN description TEXT;


SELECT DISTINCT em.movement_pattern_id
FROM exercise_muscles em
JOIN muscles m ON em.muslces_id = m.id
WHERE m.muscles_group = 'chest' AND em.role = 'primary'
