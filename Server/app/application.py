from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.tags import router as tags_router 
from routers.quentions import router as question_router
from routers.users import router as users_router
<<<<<<< HEAD
=======
from routers.posts import router as posts_router
from routers.answers import router as answers_router
>>>>>>> 2c5704495807b500217b9483b386f6de334baec7
from db.Services.dependencies import shutdown_db_client

app1 = FastAPI()

<<<<<<< HEAD

origins = [
    "http://localhost:4200"
]

app1.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)


=======
>>>>>>> 2c5704495807b500217b9483b386f6de334baec7
@app1.on_event("shutdown")
def shutdown_event():
    shutdown_db_client()

@app1.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}

app1.include_router(question_router, prefix="/questions")
<<<<<<< HEAD
app1.include_router(tags_router, prefix="/tags")
app1.include_router(users_router, prefix="/users")
=======
app1.include_router(posts_router, prefix="/posts")
app1.include_router(tags_router, prefix="/tags")
app1.include_router(users_router, prefix="/users")
app1.include_router(answers_router, prefix="/answers")





>>>>>>> 2c5704495807b500217b9483b386f6de334baec7


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("application:app1", host="0.0.0.0", port=8000, reload=True)