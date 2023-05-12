from fastapi import APIRouter
from scripts.core.handler.inventory_handler import Item_handler
from scripts.core.handler.email_handler import send_email, Email
from scripts.core.db.mongo import Item

item_router=APIRouter()

@item_router.post("/add/{item_id}")
def adding_item(item_id:int, item:Item):
   item_object=Item_handler()
   final_list = item_object.adding_item(item_id, item)
   return final_list

@item_router.delete("/remove/{item_id}")
def deleting_item(item_id: int):
   item_object=Item_handler()
   all_item=item_object.deleting_item(item_id)
   return all_item

@item_router.put("/update/{item_id}")
def updating_item(item_id:int, item:Item):
   item_object=Item_handler()
   all_item=item_object.updating_item(item_id, item)
   return all_item

@item_router.get("/")
def fetching_item():
   item_object=Item_handler()
   all_item=item_object.fetching_item()
   return all_item

@item_router.post("/send_email")
def sending_item(email:Email):
    send_email(email)
    return {"success"}