from fastapi import FastAPI
from routers.tags import router as tags_router 
from routers.quentions import router as question_router 
from db.Services.dependencies import  shutdown_db_client
from routers.users import router as users_router


app1 = FastAPI()

app1.include_router(tags_router, prefix="/tags")
app1.include_router(users_router, prefix="/users")
app1.include_router(question_router, prefix="/question", tags=["questions"])

@app1.on_event("shutdown")
def shutdown_event():
    shutdown_db_client()

@app1.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}







