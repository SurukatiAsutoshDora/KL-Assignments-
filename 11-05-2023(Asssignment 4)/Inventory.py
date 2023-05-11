from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from pymongo import MongoClient 

from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from starlette.requests import Request
from starlette.responses import JSONResponse
from pydantic import EmailStr, BaseModel
from typing import List


app = FastAPI()
item_data = {}

client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")

mydb = client.interns_b2_23
collection=mydb.Asutosh_Dora


class Item(BaseModel):
    """This class takes the parameters for the item in the inventory"""
    item_id:int
    item_name: str
    item_price: int
    item_volume: int
    item_manufacture_date: datetime
    item_expiry_date: datetime
    item_shelf_number: str


#print(list(collection.find()))
@app.get("/")
async def root():
        items=list(collection.find({}))
        final_items = []
        for each in items:
             del each["_id"]
             final_items.append(each)
        return final_items
        


@app.get("/totalprice")
async def root():
    try:
        item_list = [item_data[key]["item_price"] * item_data[key]["item_volume"] for key in item_data.keys()]
        total_price = sum(item_list)
        return {"total_price": total_price}
    except Exception as e:
        return ("Error", str(e))


@app.post("/add/{item_id}")
def add_item(item_id: int, item: Item):
    try:
        if list(collection.find({"item_id":item_id})) != []:
            return ("This ID is already present")
        else:
           collection.insert_one(item.dict())
        return "Succesfully Added"

    except Exception as e:
        return ("error", str(e))


@app.delete("/remove/{item_id}")
def delete_item(item_id: int):
    try:
        if list(collection.find({"item_id":item_id})) == []:
            return {"error", "Item not found"}
        collection.delete_one({"item_id":item_id})
        return {"Message":"Item deleted"}
            
    except Exception as e:
        return {"error", str(e)}


@app.put("/update/{item_id}")
def update_item(item_id: int, item: Item):
    try:
        if list(collection.find({"item_id":item_id})) != []:
            collection.update_one({"item_id": item_id}, {"$set": item.dict()})
            return "updated successfully"
        else:
            return {"error": "Item not found"}
    except Exception as e:
        return {"error": str(e)}

