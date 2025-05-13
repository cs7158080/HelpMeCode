from fastapi import FastAPI
from db.Services.dependencies import startup_db_client, shutdown_db_client
from routers.quentions import router as question_router

app1 = FastAPI()

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