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


class Collection:
        name = "property"

class Property :
    name : str 
    property_owner_name : str
    property_owner_id : PydanticObjectId | None = None
    description : str
    rent : int
    available : datetime
    location : str
    occupation : str
    room_size : int
    Gender : str
    Amenities : list[str] | None  = None


