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


## Home Route
@app.get("/")
def home_route():
    return {
        "message": "Welcome to the FastAPI MongoDB CRUD API. Visit /docs for API documentation."
    }

## Pydantic model for data validation
class apidata(BaseModel):
    name: str
    phone: int
    city: str
    course: str


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


## API Endpoints for Insert 
@app.post("/api/insert")
async def api_data_insert(data:apidata):
    result = await api_data.insert_one(data.dict())
    if result.inserted_id:
        return {"message": "Data inserted successfully", "id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Data insertion failed")


## API Endpoints for full update
@app.put("/api/fullupdate")
async def api_data_full_update(id: str, data:apidata):
    result = await api_data.update_one({"_id": ObjectId(id)}, {"$set": data.dict()})
    if result.modified_count == 1:
        return {"message": "Data fully updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Data not found")


## API Endpoints for partial update
@app.patch("/api/partialupdate")
async def api_data_partial_update(id: str, data: dict):
    result = await api_data.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.modified_count == 1:
        return {"message": "Data partially updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Data not found")


## API Endpoints for Delete
@app.delete("/api/delete")
async def api_data_delete(id: str):
    result = await api_data.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Data deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Data not found")