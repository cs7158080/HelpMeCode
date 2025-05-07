from fastapi import APIRouter
router = APIRouter(tags=["users"]) 

@router.get("/")
def read_root():
    return {"message": "Welcome to the users server!"}

@router.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello, {name}!"}