from fastapi import FastAPI
from db.Services.MongoConnection import MongoConnection  
from db.Services.MongoOperations import MongoOperations 
from db.Services.dependencies import startup_db_client, shutdown_db_client
from db.Modules.users import User
from routes.tags import router as tags_router  
from routes.users import router as users_router  

app1 = FastAPI()
connectToMongo = MongoConnection()
connectToMongo.connect()

app1.include_router(tags_router, prefix="/tags")
app1.include_router(users_router, prefix="/users")

@app1.on_event("startup")
def startup_event():
    startup_db_client()

@app1.on_event("shutdown")
def shutdown_event():
    shutdown_db_client()

@app1.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}

app1.include_router(question_router, prefix="/question", tags=["questions"])
