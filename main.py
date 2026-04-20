import fastapi
import uvicorn
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from core.database.db_setup import engine, sessionLocal
from fastapi import FastAPI, Depends
from spotter.subjectgate.services import goals_feasibility
from spotter.goals.models import GoalsIntake, GoalsProfile
from spotter.users.models import UserIntake, UserProfile
from spotter.users.services import profile_creation
from spotter.goals.services import create_goals
from core.database.db_tables import Base
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print("Database synchronized")
    yield
    engine.dispose()
    print("shutting down")

app = fastapi.FastAPI(lifespan=lifespan)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/new_user")
def user_intake(profile_info: UserIntake, db: Session = Depends(get_db)):
     new_user = profile_creation(profile_info, db)
     return new_user

@app.post("/new_goal")
def user_goal(goals_info: GoalsIntake, db: Session = Depends(get_db)):
    new_goal = create_goals(goals_info, db)
    return new_goal

@app.post("/new_subject")
def user_subject(final_user: UserProfile, final_goals: GoalsProfile, db: Session = Depends(get_db)):
    new_subject = goals_feasibility(final_user, final_goals, db)
    return new_subject

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
