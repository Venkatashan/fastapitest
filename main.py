from typing import Optional,List
from fastapi import FastAPI,HTTPException
#from sqlalchemy.testing.suite.test_reflection import users

from model import User,UserUpdateRequest,UserLoginSchema
from uuid import UUID,uuid4
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from auth_handler import signJWT

app = FastAPI()

db: List[User]=[
    User(id = UUID("434f46a1-bfb6-4e98-8a8d-ca7049909f7c"),
    businessPhones=["+1 412 555 0109"],
    displayName="Megan Bowen",
    givenName="Megan",
    jobTitle="Auditor",
    mail="MeganB@M365x214355.onmicrosoft.com",
    mobilePhone="123 456 789",
    officeLocation="12/1110",
    preferredLanguage="en-US",
    surname="Bowen",
    userPrincipalName="MeganB@M365x214355.onmicrosoft.com"),

    User(id=UUID("c9807ff6-cc54-4034-9c74-df1cb2e69b06"),
         businessPhones=["+1 412 555 01026"],
         displayName="Venkat Krish",
         givenName="Venkat",
         jobTitle="Auditor",
         mail="VenkatK@M365x214355.onmicrosoft.com",
         mobilePhone="123 456 000",
         officeLocation="15/1111",
         preferredLanguage="en-US",
         surname="Krish",
         userPrincipalName="venkatK@M365x214355.onmicrosoft.com")
]

def check_user(user: UserLoginSchema):
    for user in user:
        if user.id == user.id and user.password == user.password:
            return True
    return False

@app.post("/scim/Token")
async def signup_user(user: UserLoginSchema):
    db.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.id)

@app.post("/scim/v2/Users/login")
def user_login(user: UserLoginSchema):
    if check_user(user):
        return signJWT(user.id)
    return {
        "error": "Wrong login details!"
    }
@app.get("/")
async def read_root():
    return {"Hello": "Venkat"}


@app.get("/scim/v2/Users")
async def fetch_users():
    return db

@app.post("/scim/v2/Users")
async def create_user(user:User):
    db.append(user)
    return {"id":user.id}

@app.delete("/scim/v2/Users/{id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )

@app.put("scim/v2/Users/{id}")
async def update_user(user_update:UserUpdateRequest,user_id:UUID):
    for user in db:
        if user.id==user_id:
            if user_update.businessPhones is not None:
                user.businessPhones = user_update.businessPhones
            if user_update.mobilePhone is not None:
                user.mobilePhone = user_update.mobilePhone
            if user_update.officeLocation is not None:
                user.officeLocation = user_update.officeLocation
            if user_update.jobTitle is not None:
                user.jobTitle = user_update.jobTitle
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )