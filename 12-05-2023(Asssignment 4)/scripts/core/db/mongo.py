from pymongo import MongoClient 
from pydantic import BaseModel
from datetime import datetime
import logging

client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")

mydb = client.interns_b2_23
collection=mydb.Asutosh_Dora

item_data = {}

class Item(BaseModel):
    """This class takes the parameters for the item in the inventory"""
    item_id:int
    item_name: str
    item_price: int
    item_volume: int
    item_manufacture_date: datetime
    item_expiry_date: datetime
    item_shelf_number: str
    


   
def add_item(item_id: int, item: Item):
        if list(collection.find({"item_id":item_id})) != []:
            return ("This ID is already present")
        else:
           collection.insert_one(item.dict())
        return "Succesfully Added"

def delete_item(item_id: int):
        if list(collection.find({"item_id":item_id})) == []:
            return {"error", "Item not found"}
        collection.delete_one({"item_id":item_id})
        return {"Message":"Item deleted succesfully"}
            
    
def update_item(item_id: int, item: Item):
        if list(collection.find({"item_id":item_id})) != []:
            collection.update_one({"item_id": item_id}, {"$set": item.dict()})
            return "It is updated successfully"
        else:
            return {"error": "Item not found"}


def total_price():
        item_list = [item_data[key]["item_price"] * item_data[key]["item_volume"] for key in item_data.keys()]
        total_price = sum(item_list)
        return {"total_price": total_price}


def fetch():
        items=list(collection.find({}))
        final_items = []
        for each in items:
             del each["_id"]
             final_items.append(each)
        return final_items

