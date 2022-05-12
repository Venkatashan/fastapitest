#Twitter: Bek Brace
#Instagram: Bek Brace
#uvicorn main:app --reload
#python -m uvicorn main:app --reload

import uvicorn
from fastapi import FastAPI, Body, Depends

from model import UserSchema, UserLoginSchema
from auth_bearer import JWTBearer
from auth_handler import signJWT


posts = [
    {
        "id":1,
        "externalId":"userext1",
        "meta":"TestMetta",
        "businessPhones": "044284789",
        "displayName": "TestScimAPI",
        "userName": "TestSCIM1",
        "givenName": "TestSCIMuser",
        "jobTitle": "scimendpoint",
        "mail": "scimendpoint@.onmicrosoft.com",
        "mobilePhone": "1234567890",
        "officeLocation": "ind",
        "preferredLanguage": "eng",
        "userPrincipalName": "scimendpoint@M365x214355.onmicrosoft.com"
    },
    {
        "id": 2,
        "externalId": "userext2",
        "meta": "TestMetta",
        "businessPhones": "044284789",
        "displayName": "TestScimAPI",
        "userName": "TestSCIM2",
        "givenName": "TestSCIMuser",
        "jobTitle": "scimendpoint",
        "mail": "scimendpoint@.onmicrosoft.com",
        "mobilePhone": "1234567890",
        "officeLocation": "ind",
        "preferredLanguage": "eng",
        "userPrincipalName": "scimendpoint@M365x214355.onmicrosoft.com"
    },
    {
        "id": 3,
        "externalId": "userext3",
        "meta": "TestMetta",
        "businessPhones": "044284789",
        "displayName": "TestScimAPI",
        "userName": "TestSCIM3",
        "givenName": "TestSCIMuser",
        "jobTitle": "scimendpoint",
        "mail": "scimendpoint@.onmicrosoft.com",
        "mobilePhone": "1234567890",
        "officeLocation": "ind",
        "preferredLanguage": "eng",
        "userPrincipalName": "scimendpoint@M365x214355.onmicrosoft.com"
    },
]

users = []

app = FastAPI()



def check_user(data: UserLoginSchema):
    for user in users:
        if user.mail == data.mail and user.userName == data.userName:
            return True
    return False


# route handlers

# testing
@app.get("/", tags=["test"])
def greet():
    return {"hello": "world!."}

@app.post("/scim/token", tags=["user"])
def create_user(user: UserLoginSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.mail)


@app.post("/scim/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.mail)
    return {
        "error": "Wrong login details!"
    }

@app.post("/scim/v2/Users", dependencies=[Depends(JWTBearer())], tags=["posts"])
def add_post(post: UserSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }

@app.get("/scim/v2/Users/{id}", dependencies=[Depends(JWTBearer())], tags=["posts"])
def get_single_post(id: int):
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


