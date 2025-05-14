from fastapi import APIRouter,HTTPException
from app.schemas.book import Book

root = APIRouter()

db={
    1:{
        "id":1,
        "title":"book1",
        "author":"author1",
        "year":2020,
        "genre":"fiction"
    }
}


@root.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}

@root.get("/items",response_model=list[Book])
def read_items():
    if db:
        return list(db.values())
    else:
        raise HTTPException(status_code=404, detail="No items found")

@root.post("/items", response_model=Book)
def create_item(item: Book):
    if item.id in db:
        raise HTTPException(status_code=400, detail="Item already exists")
    db[item.id] = item.model_dump()
    return item