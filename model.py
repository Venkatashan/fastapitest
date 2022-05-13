from typing import Optional
from uuid import UUID,uuid4
from pydantic import BaseModel

class User(BaseModel):
    schemas:list
    active: bool
    displayName:str
    preferredLanguage:str
    userName: str
    namegivenName:str
    namefamilyName:str
    nameformatted:str
    ReportableIdentifier:str
    externalId:str

    #phoneNumbers:list=[{"value":value,"type":type}]

class UserUpdateRequest(BaseModel):
    businessPhones: list
    jobTitle: str
    mobilePhone: str
    officeLocation: str

class UserLoginSchema(BaseModel):
    id:str
    password:str
