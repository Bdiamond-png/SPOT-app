# Debug Log

## Format
Each entry should include:
- Date
- Problem encountered
- How it was diagnosed
- How it was resolved

## Entries
5/12/2026
Feature Decision: built a dictionary for valid styles. This dictionary
is to be used to reject or accept a users goals
and training method/style. If a user has a goal of
gaining strength yet chooses a style of training contradictory 
of strength gaining like body building then that users request
is rejected. They shall receive an error message.
The other approach is hardcode each option inside the validation function. 
I chose a dictionary for easy mutability later and simplicity for other 
engineers to read about. (Known issue: error message returns raw enum
values, not human-readable strings. Will fix later. )


if last time consistent > 1.5 months -> reduce circuit.
if beginner -> 1 or 2 circuits.
if intermediate or advanced 3 circuits minimum.
if sets per compound > 2 or sets per isolation > 3 -> factor into circuit count.
I chose 1.5 months because at 1 month of not being consistent in the gym you lose about 5-10% gains, 
at 2 months its double. The closer you are to 2 months out of condition the harder it feels to as you return so, at that
point I reduce the intensity for a real life client. 

Trainer logic is the next step. I decided I need to helper functions to go inside my create_new_program function.
Selection logic and Assembly logic, one to select the exercises that fit subject needs and assembly logic that 
understand the order in which to create circuits. 

As for the exercises themselves I've decided that I will pull exercises from an API map them accordingly and insert them
into my supabase tables to pull from. (ETL)


5/28/2026

I evaluated rounds of API's including API ninjas & ExerciseDB as exercise data sources. Both
I rejected due to inconsistent categorization, missing muscle groups, and poor mapping to movement pattern
schema. 

My decision is to build my on exercise table in Supabase with full control over my schema. 
