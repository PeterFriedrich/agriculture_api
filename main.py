# main.py
"""
Fastai API application
- automatic documentaion
- serialization

If you run uvicorn, then open the link:
http://127.0.0.1:8000/ to see the web server.
add /docs to see the docs page, by swagger UI,
or redoc

Paths: for https://example.com/items/foo,
 the path would be /items/foo. Last part of url.

Paths are also called "endpoints" or "routes".

Operation = HTTP request method,
POST, GET, PUT, etc. Each lets you communicate
with an endpoint/path.

"""
from typing import Optional

from fastapi import FastAPI # api class
from pydantic import BaseModel

# pydantic for data models/shapes
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    prince: float
    tax: Optional[float] = None

"""
{
    "name": "Foo",
    "description": "An optional description", (dft None)
    "price": 45.2,
    "tax": 3.5 (dft None)
}
or
{
    "name": "Foo",
    "price": 45.2
}
"""
class User_input(BaseModel):
    operation: str
    x : float
    y : float

app = FastAPI() # instance of api class

# path operation decorator, modifies root, notes it as get
@app.get("/")
async def root(): # makes async func
    return {"message": "Hello World!"}

@app.post("/items/")
async def create_item(item: Item):
    # Func type hint, creates instance of "Item"
    # -> FastAPI will read body, convert types
    # validate, return error if inv, give data
    # param item, generate json schema defn
    return item

# value of path param item_id is passed (/items/foo)
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# parses and returns the int, conversion
# error on non-int: validation + parsing
@app.get("/nums/{item_id}")
async def read_int(item_id: int):
    return {"item_id": item_id}

# make sure to put specific paths before general

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# request body: data sent by the client to your api
# response body: data your api sends back
# send data: use POST, PUT, DELETE, PATCH (not GET)

# pydantic