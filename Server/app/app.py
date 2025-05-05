from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI server!"}


@app.get("/{name}")
def read(name: str):
    return {"message": f"{name}!"}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello, {name}!"}
