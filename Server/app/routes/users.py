from fastapi import APIRouter,Depends
from db.Modules.users import User,UserService
from db.Services.dependencies import get_mongo_operations, get_db
from functools import lru_cache


router = APIRouter(tags=["users"])

@lru_cache()
def get_users_service(
    mongo_operations=Depends(lambda db=Depends(get_db): get_mongo_operations("users", db))
):
   
    return UserService(mongo_operations)

@router.post("/add")
def add_user(user: User, user_service=Depends(get_users_service)):
    user_data = user.dict()  
    user_id = user_service.create_user(user_data) 
    return {"message": "User created successfully", "user_id": user_id}  
    
@router.get("/getall")
def get_all_users(user_service=Depends(get_users_service)):
    return user_service.get_all_users()
 
@router.get("/getuserbyname/{username}")
def get_user_by_name(username: str,user_service=Depends(get_users_service)):
    user = user_service.get_user_by_name(username)
    return user

@router.get("/getusersbytag/{tag}")
def get_users_by_tag(tag: str,user_service=Depends(get_users_service)):
    users_by_tag = user_service.get_users_by_tag(tag)
    return users_by_tag

@router.get("/getusersbytagvaluetrue/{tag}")
def get_users_by_tag_value(tag: str,user_service=Depends(get_users_service)):
    users_by_tag_value = user_service.get_users_by_tag_value_true(tag)
    return users_by_tag_value

@router.get("/getusersbytagvaluefalse/{tag}")
def get_users_by_tag_value_false(tag: str,user_service=Depends(get_users_service)):
    users_by_tag_value_false = user_service.get_users_by_tag_value_false(tag)
    return users_by_tag_value_false
