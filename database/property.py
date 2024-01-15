# from ast import Str, alias
# from dataclasses import Field
# from datetime import datetime, timedelta
# from email.policy import default
# from typing import Collection, List, Union,Dict
# from urllib.error import HTTPError
# from beanie import PydanticObjectId 
from models.property import Property
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['rent_a_room']
user_collection = Property

async def add_new_property(property_dict: dict):
    property = Property(**property_dict)
    property = await property.create()
    return property