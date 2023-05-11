from pymongo import MongoClient 

client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")

mydb = client.interns_b2_23
Item={
    "item_name": "Shampoo",
    "item_price": 40,
    "item_volume": 60,
    "item_manufacture_date": "2022-02-12 15:50:00",
    "item_expiry_date":  "2023-05-12 15:20:00",
    "item_shelf_number": "A111"
}   
inventory = mydb.Asutosh_Dora
inventory.insert_one(Item)



 




