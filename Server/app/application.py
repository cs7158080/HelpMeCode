from fastapi import FastAPI
from db.Services.MongoConnection import MongoConnection  # Ensure the path matches your project structure
from db.Services.MongoOperations import MongoOperations  # Adjusted to match a typical module structure
from db.Modules.users import Users  # Ensure the path matches your project structure

# This file can be empty or contain package-level imports or initializations
app1 = FastAPI()
connectToMongo = MongoConnection()
connectToMongo.connect()
@app1.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}


@app1.post("/{name}")
def read(name: str):
    
    user_model = MongoOperations(connectToMongo.database, 'users')
    user_service = Users(user_model)
    user_data = user_service.create_user({name: name})
    if user_data:
        return {"message": f"Hello, {name}!"}
    else:
        return {"message": f"User {name} not found."}

@app1.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello, {name}!"}


