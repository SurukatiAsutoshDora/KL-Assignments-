from fastapi import FastAPI
from scripts.core.services.inventory_servies import item_router


app = FastAPI()
item_data = {}

app.include_router(item_router)


