from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import asyncio


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

# @app.post("/getcontext")
# async def contextretrieval(request : ContextRequest, response_model = ContextResponse):
#     return request


@app.get("/getcontext/")
async def read_items() :
    return {"from pydantic import BaseModel"}

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []


# @app.post("/items/", response_model=Item)
# async def create_item(item: Item) :
#     return item


# @app.get("/items/", response_model=list[Item])
# async def read_items() :
#     return [
#         {"name": "Portal Gun", "price": 42.0},
#         {"name": "Plumbus", "price": 32.0},
#     ]


request = ContextRequest(function_name="calculate", file_path= "client/script.py", repo_name="repo")

@app.post("/retrieve", response_model =ContextResponse)
async def retrieve(request:ContextRequest):
    async with httpx.AsyncClient() as client:
        response = await client.get(SERVICE_URL,
                                     params=request.model_dump())
        context = response.json()
      
    return ContextResponse(**context)