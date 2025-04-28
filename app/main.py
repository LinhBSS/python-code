# app/main.py
from fastapi import FastAPI
from app import database
from app.models import user

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
