from fastapi import FastAPI
from routes.users import router as users_router
app = FastAPI()
app.include_router(users_router, prefix="/users", tags=["users"]) 
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello, {name}!"}
