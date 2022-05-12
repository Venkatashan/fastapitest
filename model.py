from typing import Optional
from uuid import UUID,uuid4
from pydantic import BaseModel

class User(BaseModel):
    id:str
    userName:str
    externalId:str


class UserUpdateRequest(BaseModel):
    businessPhones: list
    jobTitle: str
    mobilePhone: str
    officeLocation: str

class UserLoginSchema(BaseModel):
    id:str
    password:str
