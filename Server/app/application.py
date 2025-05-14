from fastapi import FastAPI
from routers.tags import router as tags_router  
from db.Services.dependencies import startup_db_client, shutdown_db_client

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
app1.include_router(tags_router, prefix="/tags")





