from fastapi import FastAPI
from db.Services.MongoConnection import MongoConnection  # Ensure the path matches your project structure
from db.Services.MongoOperations import MongoOperations  # Adjusted to match a typical module structure
from db.services. import UserService  # Ensure the path matches your project structure

# This file can be empty or contain package-level imports or initializations
app = FastAPI()
connectToMongo = MongoConnection()
connectToMongo.connect()
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}


@app.get("/{name}")
def read(name: str):
    user_model = GenericModel(connectToMongo, "users")
    user_service = UserService(user_model)
    user_data = user_service.find_user(name)
    if user_data:
        return {"message": f"Hello, {name}!"}
    else:
        return {"message": f"User {name} not found."}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello, {name}!"}


