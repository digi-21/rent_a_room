from fastapi import Body, APIRouter, HTTPException , Request , Response, Header, File, UploadFile , Depends
from auth.firebase import get_current_user
from models.user import User
from database.user import *
from fastapi.responses import JSONResponse

router = APIRouter()

#to add a new user 
@router.post("/add_a_user/")
async def add_user(request:Request, current_user: dict = Depends(get_current_user)):
    uuid = current_user.get("user_id")
    data = await request.json()
    first_name = data['first_name']
    last_name = data["last_name"]
    date_of_birth = data['date_of_birth']
    # email = data["email"]
    # phone_number = data["phone_number"]
    user: User = {
        "first_name" : first_name,
        "last_name" : last_name,
        "date_of_birth" : date_of_birth,
        "firebase_id" : uuid,
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
    try:
        await add_new_user(user)
        response_data = {
        "status_code": "200",
        "message": "user created successfully!",
        }
        response = JSONResponse(content=response_data)
        return response
    
    except:
        raise HTTPException(status_code=400, detail="Bad request")   
    



