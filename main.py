import fastapi
import uvicorn

from spotter.users.models import UserIntake
from spotter.users.services import profile_creation
app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/new_user")
def user_intake(profile_info: UserIntake):
     new_user = profile_creation(profile_info)
     return new_user

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
