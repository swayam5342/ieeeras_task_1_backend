from fastapi import APIRouter,Depends,HTTPException
from app.schemas import book

root = APIRouter()
db={1:{"name":"book1","author":"author1"}}
@root.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}

@root.get("/items")
def read_items():
    if db:
        return db
    else:
        raise HTTPException(status_code=404, detail="No items found")