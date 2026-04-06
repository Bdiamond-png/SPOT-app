import fastapi
import uvicorn
from spotter.subjectgate.services import goals_feasibility
from spotter.goals.models import GoalsIntake, GoalsProfile
from spotter.users.models import UserIntake, UserProfile
from spotter.users.services import profile_creation
from spotter.goals.services import create_goals
app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/new_user")
def user_intake(profile_info: UserIntake):
     new_user = profile_creation(profile_info)
     return new_user

@app.post("/new_goal")
def user_goal(goals_info: GoalsIntake):
    new_goal = create_goals(goals_info)
    return new_goal

@app.post("/new_subject")
def user_subject(final_user: UserProfile, final_goals: GoalsProfile):
    new_subject = goals_feasibility(final_user, final_goals)
    return new_subject

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
