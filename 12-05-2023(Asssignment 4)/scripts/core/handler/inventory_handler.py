from scripts.core.db.mongo import add_item,delete_item,update_item,total_price,fetch,Item

class Item_handler:
    def adding_item(self, item_id:int, item: Item):
        try:
            return add_item(item_id,item)
        except Exception as e:
            return ("ERROR", str(e))
            
    def deleting_item(self,item_id: int):
        try:
            return delete_item(item_id)
        except Exception as e:
            return ("ERROR", str(e)) 
     
    def updating_item(self,item_id: int, item: Item):
        try:
            return update_item(item_id,item)
        except Exception as e:
            return ("ERROR", str(e))
        
    def total_pricing(self):
        try:
            return total_price()
        except Exception as e:
            return ("ERROR", str(e))


    def fetching_item(self):
        try:
            return fetch()
        except Exception as e:
            return ("ERROR", str(e)) 
        
    # def sending_email(self,email):
    #     try:
    #         return send_email()
    #     except Exception as e:
    #          return ("ERROR", str(e)) 
              