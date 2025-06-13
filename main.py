from sensor.exception import sensorException
import sys 
import os
from sensor.logger import logging

def test_exception():
    try:
        logging.info("yaha per ek error ayega division by zero ")
        a=1/0
    except Exception as e:
        raise e

if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e :
        print(e)

