from fastapi import FastAPI
from routers.tags import router as tags_router 
from routers.quentions import router as question_router
from routers.users import router as users_router
from routers.posts import router as posts_router
from routers.answers import router as answers_router
from db.Services.dependencies import shutdown_db_client

app1 = FastAPI()

@app1.on_event("shutdown")
def shutdown_event():
    shutdown_db_client()

@app1.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}

app1.include_router(question_router, prefix="/questions")
app1.include_router(posts_router, prefix="/posts")
app1.include_router(tags_router, prefix="/tags")
app1.include_router(users_router, prefix="/users")
app1.include_router(answers_router, prefix="/answers")







