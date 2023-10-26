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

class User :
    first_name : str | None = None
    last_name : str | None = None
    date_of_birth : datetime | None = None
    firebase_id : PydanticObjectId | None = None
    email : EmailStr | None = None
    phone_number : str | None = None
    profile_pic : str | None = None
    
    