from typing import Optional
from uuid import UUID,uuid4
from pydantic import BaseModel

class User(BaseModel):
    schemas:list
    externalId:str
    userName: str
    active:bool
    emails: list
    meta: dict
    name: dict
    roles:list
    #phoneNumbers:list=[{"value":value,"type":type}]

class UserUpdateRequest(BaseModel):
    businessPhones: list
    jobTitle: str
    mobilePhone: str
    officeLocation: str

class UserLoginSchema(BaseModel):
    id:str
    password:str
