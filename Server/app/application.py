from fastapi import FastAPI
from db.Services.MongoConnection import MongoConnection  # Ensure the path matches your project structure
from db.Services.MongoOperations import MongoOperations  # Adjusted to match a typical module structure
from db.Modules.users import Users  # Ensure the path matches your project structure
from routes.tags import router as tags_router  # Ensure the path matches your project structure
# This file can be empty or contain package-level imports or initializations
app1 = FastAPI()
connectToMongo = MongoConnection()
connectToMongo.connect()

app1.include_router(tags_router, prefix="/tags")
@app1.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}






