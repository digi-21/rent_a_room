# from ast import Str, alias
# from dataclasses import Field
# from datetime import datetime, timedelta
# from email.policy import default
# from typing import Collection, List, Union,Dict
# from urllib.error import HTTPError
# from beanie import PydanticObjectId 
from models.user import User
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['rent_a_room']
user_collection = User

async def add_new_user(user_dict: dict):
    user = User(**user_dict)
    user = await user.create()
    return user
