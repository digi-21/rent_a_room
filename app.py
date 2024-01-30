from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware 
from routes.user import router as UserRouter
from contextlib import asynccontextmanager
from config.config import initiate_database



@asynccontextmanager
async def start_app(app: FastAPI):
    await initiate_database()
    yield
    print("3")

app = FastAPI(lifespan=start_app)

# @app.on_event("startup")
# async def start_database():
#    await initiate_database()
#    print("3")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your Remix.js app's domain
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)




@app.get("/", tags=["Root"])
async def read_root():
    return print("welcome to rent_a_room!")

app.include_router(UserRouter, tags=["user"], prefix="/user")

