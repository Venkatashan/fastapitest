from typing import Optional
from uuid import UUID,uuid4
from pydantic import BaseModel

class User(BaseModel):
    id:Optional[UUID]=uuid4()
    businessPhones: list
    displayName: str
    givenName: str
    jobTitle: str
    mail: str
    mobilePhone: str
    officeLocation: str
    preferredLanguage: str
    surname: str
    userPrincipalName: str

class UserUpdateRequest(BaseModel):
    businessPhones: list
    jobTitle: str
    mobilePhone: str
    officeLocation: str

class UserLoginSchema(BaseModel):
    id:str
    password:str
