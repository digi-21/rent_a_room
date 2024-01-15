from fastapi import Request, Response
from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr, Field as PydanticField
from typing import Optional, Any
from beanie import PydanticObjectId 
from datetime import date, datetime
from uuid import UUID
from typing import Union , 
from fastapi import Body
from bson.objectid import ObjectId as BsonObjectId

class User :
    first_name : str | None = None
    last_name : str | None = None
    date_of_birth : datetime | None = None
    firebase_id : PydanticObjectId | None = None
    email : EmailStr | None = None
    phone_number : str | None = None
    profile_pic : str | None = None
    space : list[PydanticObjectId] | None = None
    Tenant : list[PydanticObjectId] | None = None
    Buddyup : list[PydanticObjectId] | None = None
    verification : bool 
    notifications : list[PydanticObjectId] | None = None
    liked : list[PydanticObjectId] | None = None
    

class Collection:
        name = "user"
class Config:
        schema_extra = {
            "example": {
                "first_name" : None,
                "last_name" : None,
                "date_of_birth" : None,
                "firebase_id" : None, 
                "email" : None,
                "phone_number" : None,
                "profile_pic" : None,
                "space" : None,
                "Tenant" : None,
                "Buddyup" : None,
                "verification" : False, 
                "notifications" : None,
                "liked" : None
            }
        }