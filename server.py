from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import asyncio
import requests
import json
import uvicorn


class ContextRequest(BaseModel):
    function_name : str
    file_path : str
    repo_name : str 


# class ContextResponse(BaseModel) :
#     snippet :str


app = FastAPI()


SERVICE_URL = "http://127.0.0.1:3000/test"
SERVICE_URL2 = "http://127.0.0.1:3000/context"

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.post("/getcontext")
# async def contextretrieval(request : ContextRequest, response_model = ContextResponse):
#     return request

@app.get("/testing/")
async def testhello():
    res = requests.get(SERVICE_URL)
    print(res)
    return {"message": res.content}



@app.get("/getcontext/")
async def read_items() :
    return {"from pydantic import BaseModel"}



request = ContextRequest(function_name="calculate", file_path= "client/script.py", repo_name="repo")# Convert the request object to a dictionary
request = request.__dict__

# Convert the dictionary to a JSON string
request = json.dumps(request)
@app.post("/retrieve")
async def retrieve(request):
        response = requests.post(SERVICE_URL2)
        context = response.content
         
        print(response.status_code)
        return {"message": response.content, "response.status_code":response.status_code}
        # Handle JSON response from the service
    #     if response.headers.get('Content-Type', '').lower() == 'application/json':
    #         data = response.json()
    #         context = data
    #     else:
    #         # Handle non-JSON responses (if applicable)
    #         # raise an exception or log a warning
    #         raise HTTPException(status_code=500, detail="Unexpected response type from service")

    #     return c
    # except requests.exceptions.RequestException as e:
    #     # Handle network errors gracefully
    #     raise HTTPException(status_code=500, detail=f"Error retrieving data: {str(e)}")

    # except Exception as e:
    #     # Handle other unexpected exceptions
    #     raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    #      # Handle other unexpected exceptions
    #     raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    

if __name__ =="__main__":
    uvicorn.run(app)