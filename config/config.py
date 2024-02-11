from typing import Optional
from xml.dom.minidom import Document
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings
from models.user import User
from models.property import Property
from pymongo import MongoClient
from urllib.parse import quote_plus
from pymongo.server_api import ServerApi


class Settings(BaseSettings):
    # database configurations
    username= quote_plus('rentaroom')
    password = quote_plus('Rent@room')
    DATABASE_URL: Optional[str] = 'mongodb+srv://' + username + ':' + password + '@' + 'sbrooms.j1wukwg.mongodb.net/?retryWrites=true&w=majority'
    #mongodb+srv://rentaroom:<password>@sbrooms.j1wukwg.mongodb.net/?retryWrites=true&w=majority
    # JWT
    secret_key: str = "62a707a32f174a25acb892cd"
    algorithm: str = "HS256"

    class Config:
        env_file = ".env.dev"
        orm_mode = True


async def initiate_database():
    try:
        client = AsyncIOMotorClient(Settings().DATABASE_URL, server_api=ServerApi('1'))
        print("1----------------------------------------")
        database = client["rent_a_roomDB"]
        print("2----------------------------------------")
        await init_beanie(database,
                        document_models=[User,Property])
        print("3----------------------------------------")
        
        print("Pinged your deployment. You successfully connected to MongoDB!")

    except Exception as e:
        print("4----------------------------------------")
        print(e)



