from pydantic import BaseModel

class UserIntake(BaseModel):
    name: str
    age: int
    gender: str
    height: float
    weight: float
    body_fat_percent: float