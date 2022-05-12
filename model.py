from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):

    id: int = Field(default=None)
    externalId:str = Field(default=None)
    meta:str= Field(default=None)
    businessPhones : str = Field(...)
    userName : str = Field(...)
    displayName:str = Field(...)
    givenName:str = Field(...)
    jobTitle:str = Field(...)
    mail:str = Field(...)
    mobilePhone:str = Field(...)
    officeLocation:str = Field(...)
    preferredLanguage:str = Field(...)
    surname:str = Field(...)
    userPrincipalName:str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "id": 4,
                "externalId": "userext",
                "meta": "TestMetta",
                "businessPhones": "044284789",
                "userName": "TestSCIM",
                "displayName": "TestScimAPI",
                "givenName": "TestSCIMuser",
                "jobTitle": "scimendpoint",
                "mail": "scimendpoint@.onmicrosoft.com",
                "mobilePhone": "1234567890",
                "officeLocation": "ind",
                "preferredLanguage": "eng",
                "surname":"endpoint",
                "userPrincipalName": "scimendpoint@M365x214355.onmicrosoft.com"
            }
        }


class UserLoginSchema(BaseModel):

    userName : str = Field(...)
    mail: str = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "userName": "scimendpoint azureAD",
                "mail": "scimendpointazuread@x.com",
            }
        }
