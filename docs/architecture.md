[App flow] (diagrams/app_flowchart.pdf)

[System Design] (system_design.pdf)

I created these 2 diagrams before any code or any files to illustrate my vison on
how the app should work on a basic level.


I ended up creating 10 tables(including users and user_goals): exercises, muscles, exercise_muscles, movement_patterns, exercise_relationships, exersice_workout_style_scores,
user_goal_muscles, workout_styles. 


The muscles tables are 56 muscles and their muscle groups ex: upper_pec group chest.
movement_patterns tabel illustrates the different movement patterns and a description of the movement function.


Exercise muscles illustrates the relationship between exercises and the movement_patterns and muscles involved, this allows for
the logic to pull more accurate exercises per user goals. exercise relationships is a table meant to show the relationships 
of exercise progressions and regressions. 

Workout styles is a table representing all the different kinds of workout styles
like body building and olympic lifting. Exercise workout style scores is likely one of the most important tables of all. 
It scores exercises based on the style for example bench press scores a 10 on powerlifting but an 8 on body building and a 
0 for calisthenics and a 2 for olympic lifting. 

This allows logic like "if score > 7 add to program". The exercise table 
is also one of extreme importance, it lists all numbers of exercises and includes a multitude of information about the exercise 
giving the user a guideline on execution.