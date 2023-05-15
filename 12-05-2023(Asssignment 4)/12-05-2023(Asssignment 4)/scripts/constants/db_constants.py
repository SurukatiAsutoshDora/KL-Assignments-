import logging
from scripts.logging.logs import getLogger

getLogger()

class DatabaseConstants:
 try:    
    """ this class is used to create database constants """
    database_name = "interns_b2_23"
    collection_name = "Asutosh_Dora"
    uri = "mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"
 except Exception as e:
    logging.error({})    


db_constant_object = DatabaseConstants()
