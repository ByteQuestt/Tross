from fastapi import FastAPI
from pydantic import BaseModel


class ContextRequest(BaseModel):
    function_name : str
    file_path : str
    repo_name : str 


class ContextResponse(BaseModel) :
    snippet :str


app = FastAPI()


SERVICE_URL = "http://127.0.0.1:8000/"

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/getcontext")
async def contextretrieval(request : ContextRequest, response_model = ContextResponse):
    return request


@app.get("/getcontext/", response_model= ContextResponse)
async def read_items() -> Any:
    return {"message ":"from pydantic import BaseModel"}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]


