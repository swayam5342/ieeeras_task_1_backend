from fastapi import APIRouter, Depends,HTTPException
from app.schemas import book

root = APIRouter()

@root.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}