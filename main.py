import fastapi
from spotter.users.models import UserIntake

app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/new_user")
def user_intake(profile_info: UserIntake):
    return{
"response": "OK! Need more information",
"body": profile_info}