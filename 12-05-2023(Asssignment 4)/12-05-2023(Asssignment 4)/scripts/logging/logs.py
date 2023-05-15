import logging


def getLogger():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='logs/app.log',
    )
