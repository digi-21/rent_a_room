from typing import Optional
from xml.dom.minidom import Document
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings
from models.user import User
from pymongo import MongoClient


class Settings(BaseSettings):
    # database configurations in which "DATABASE_URL" will contain the actual url to mongodb
    DATABASE_URL: Optional[str] = "mongodb:connection_url"

    # JWT
    # secret_key: str = "xxxxxxxxxx"
    # algorithm: str = "any algo for eg. HS256"

    class Config:
        env_file = ".env.dev"
        orm_mode = True


async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(database=client.get_default_database(),
                      document_models=[User])

