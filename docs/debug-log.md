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
