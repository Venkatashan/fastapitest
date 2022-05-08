#Twitter: Bek Brace
#Instagram: Bek Brace
#uvicorn main:app --reload
#python -m uvicorn main:app --reload

import uvicorn
from fastapi import FastAPI, Body, Depends

from model import PostSchema, UserSchema, UserLoginSchema
from auth_bearer import JWTBearer
from auth_handler import signJWT

app = FastAPI()

posts = [
    {
        "id": 1,
        "title": "Penguins ",
        "text": "Penguins are a group of aquatic flightless birds."
    },
    {
        "id": 2,
        "title": "Tigers ",
        "text": "Tigers are the largest living cat species and a memeber of the genus panthera."
    },
    {
        "id": 3,
        "title": "Koalas ",
        "text": "Koala is arboreal herbivorous maruspial native to Australia."
    },
]

users = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Get Posts
@app.get("/user")
def get_posts():
    return { "data": posts }