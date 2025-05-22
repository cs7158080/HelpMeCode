from fastapi import APIRouter,Depends,Query
from db.Modules.users import User,UserService
from db.Services.dependencies import get_mongo_operations, get_db
from functools import lru_cache
from typing import List



router = APIRouter(tags=["users"])

@lru_cache()
def get_users_service(
    mongo_operations=Depends(lambda db=Depends(get_db): get_mongo_operations("users", db))
):
   
    return UserService(mongo_operations)

@router.post("/add")
def add_user(user: User, user_service=Depends(get_users_service)):
    user_id = user_service.create_user(user) 
    return {"message": "User created successfully", "user_id": user_id}  
    
@router.get("/getall")
def get_all_users(user_service=Depends(get_users_service)):
   return  user_service.get_all_users()
     

@router.get("/getuserbyname/{username}")
def get_user_by_name(username: str,user_service=Depends(get_users_service)):
    user = user_service.get_user_by_name(username)
    return user


@router.get("/getusersbytags/")
def get_users_by_tags(tags: List[str] = Query(...), user_service=Depends(get_users_service)):
    users_by_tags = user_service.get_users_by_tags(tags)
    return users_by_tags


@router.get("/getusersbytagstrue/")
def get_users_by_tags_true(tags: List[str] = Query(...), user_service=Depends(get_users_service)):
    users_by_tags = user_service.get_users_by_tags_flag(tags, True)
    return users_by_tags

@router.get("/getusersbytagsfalse/")
def get_users_by_tags_false(tags: List[str] = Query(...), user_service=Depends(get_users_service)):
    users_by_tags = user_service.get_users_by_tags_flag(tags, False)
    return users_by_tags