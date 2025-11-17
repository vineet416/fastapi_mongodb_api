from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
db = client["fastapi"]
api_data = db["fastapi_coll"]

app = FastAPI()

class apidata(BaseModel):
    name: str
    phone: int
    city: str
    course: str

@app.post("/api/insert")
async def api_data_insert_helper(data:apidata):
    result = await api_data.insert_one(data.dict())
    return str(result.inserted_id)


def api_helper(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

@app.post("/api/getdata")
async def get_api_data():
    items = []
    cursor = api_data.find({})
    async for document in cursor:
        items.append(api_helper(document))
    return items