from scripts.db.mongo import item_object
from scripts.logging.logs import logger
from scripts.schemas.inventory_schemas import Item


class item_handler:
    def fetch(self):
        try:
            all_items = item_object.fetch()
            if all_items == []:
                logger.warning({"Warning": "No items present in the database"})
                return {"Warning": "No items present in the database"}
            return all_items
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def add_item(self, item_id: int, item: Item):
        try:
            if list(item_object.find_by_id({"id": item_id})) != []:
                logger.warning({"Warning:": "item already exist"})
                return {"Warning:": "item already exist"}
            return item_object.add_item(item)
        except Exception as e:
            logger.error({"error": str(e.args)})
            return {"error": str(e.args)}

    def update_item(self, item_id: int, item: Item):
        try:
            if item_object.find_by_id({"id": item_id}) == []:
                logger.warning({"Warning": "item does not exist"})
                return {"Warning": "item does not exist"}
            return item_object.update_item(item_id, item)
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def delete_item(self, item_id: int):
        try:
            if item_object.find_by_id({"id": item_id}) == []:
                logger.warning({"Warning": "item does not exist"})
                return {"Warning": "item does not exist"}
            return item_object.delete_item(item_id)
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}

    def find_total(self):
        try:
            total = item_object.get_total()
            if total == 0:
                logger.warning(
                    {"Warning:": "There are no items in the database"})
                return {"Warning:": "There are no items in the database"}
            return (list(total))[0]['total']
        except Exception as e:
            logger.error({"error": str(e)})
            return {"error": str(e)}
