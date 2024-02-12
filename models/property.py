from fastapi import Request, Response
from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr, Field as PydanticField
from typing import Optional, Any
from beanie import PydanticObjectId
from datetime import date, datetime
from uuid import UUID
from typing import Union
from fastapi import Body
from bson.objectid import ObjectId as BsonObjectId

class PydanticObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            v = v  # raise TypeError('ObjectId required')
        return str(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class Property(Document) :
    name : str 
    property_owner_name : str| None = None
    property_owner_id : PydanticObjectId | None = None
    description : str| None = None
    rent : int| None = None
    available : str | None = None
    location : str| None = None
    occupation : str| None = None
    room_size : int| None = None
    Gender : str| None = None
    Amenities : list[str] | None  = None


class Collection:
        name = "property"
class Config:
        schema_extra = {
            "example": {
                "name" : None,
                "property_owner_name" : None,
                "property_owner_id" : None,
                "description" : None,
                "rent" : None, 
                "available" : None,
                "location" : None,
                "occupation" : None,
                "room_size" : None,
                "Gender" : None,
                "Amenities" : None
            }
        }