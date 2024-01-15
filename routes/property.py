from fastapi import Body, APIRouter, HTTPException , Request , Response, Header, File, UploadFile , Depends
from auth.firebase import get_current_user
from models.property import Property
from database.user import *
from database.property import *
from fastapi.responses import JSONResponse

router = APIRouter()

#to add a new user 
@router.post("/add_a_user/")
async def add_property(request:Request, 
                       current_user: dict = Depends(get_current_user)):
    uuid = current_user.get("user_id")
    data = await request.json()
    name = data['first_name'] 
    property_owner_name = data['property_owner_name']
    property_owner_id = data['property_owner_id']
    description = data['description']
    rent = data['rent']
    available = data['available']
    location = data['location']
    occupation = data['occupation']
    room_size = data['room_size']
    Gender = data['Gender']
    Amenities = data['Amenities']
    property: Property = {

        "property_owner_name" : property_owner_name,
        "property_owner_id" : property_owner_id,
        "description" : description,
        "rent" : rent,
        "available" : available,
        "location" : location,
        "occupation" : occupation,
        "room_size" : room_size,
        "Gender" : Gender,
        "Amenities" : Amenities

        }
    new_property = await (property)
    print(new_property)
    response_data = {
        "status_code": "200",
        "message": "user created successfully!",
    }
    response = JSONResponse(content=response_data)
    return response
