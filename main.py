## Importing necessary libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
from dotenv import load_dotenv

## Loading environment variables
load_dotenv()

## Database connection
MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
db = client["fastapi"]
api_data = db["fastapi_coll"]

## FastAPI app instance
app = FastAPI()

## Pydantic model for data validation
class apidata(BaseModel):
    name: str
    phone: int
    city: str
    course: str


## API Endpoints for Insert
@app.post("/api/insert")
async def api_data_insert(data:apidata):
    result = await api_data.insert_one(data.dict())
    if result.inserted_id:
        return {"message": "Data inserted successfully", "id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Data insertion failed")


## API Endpoints for Update
@app.post("/api/update")
async def api_data_update(name: str, data:apidata):
    result = await api_data.update_one({"name": name}, {"$set": data.dict()})
    if result.modified_count == 1:
        return {"message": "Data updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Data not found")


## API Endpoints for Delete
@app.post("/api/delete")
async def api_data_delete(name: str):
    result = await api_data.delete_one({"name": name})
    if result.deleted_count == 1:
        return {"message": "Data deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Data not found")


## API Helper function to format data
def api_helper(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc


## API Endpoints for Get Data
@app.get("/api/getdata")
async def get_api_data():
    items = []
    cursor = api_data.find({})
    async for document in cursor:
        items.append(api_helper(document))
    return items