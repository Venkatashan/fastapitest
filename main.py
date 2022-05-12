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
from auth_bearer import JWTBearer

app = FastAPI()

db: List[User]=[]

def check_user(user: UserLoginSchema):
    for user in user:
        if user.id == user.id and user.password == user.password:
            return True
    return False

@app.post("/scim/Token")
async def signup_user(user: UserLoginSchema):
    #db.append(user) # replace with db call, making sure to hash the password first
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


@app.get("/scim/v2/Users",dependencies=[Depends(JWTBearer())])
async def fetch_users():
    #return db
    testuser={
     "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User",
      "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
      "urn:ietf:params:scim:schemas:extension:CustomExtensionName:2.0:User"],
     "userName":"bjensen@testuser.com",
     "id": "48af03ac28ad4fb88478",
     "externalId":"bjensen",
     "name":{
       "familyName":"Jensen",
       "givenName":"Barbara"
     },
     "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
     "Manager": "123456"
   },
     "urn:ietf:params:scim:schemas:extension:CustomExtensionName:2.0:User": {
     "tag": "701984",
   },
   "meta": {
     "resourceType": "User",
     "created": "2010-01-23T04:56:22Z",
     "lastModified": "2011-05-13T04:42:34Z",
     "version": "W\/\"3694e05e9dff591\"",
     "location":
 "https://example.com/v2/Users/2819c223-7f76-453a-919d-413861904646"
   }
}
    return testuser

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