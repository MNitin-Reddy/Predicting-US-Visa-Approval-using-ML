import sys 

from us_visa.configuration.mongo_db_connection import MongoDBClient
from us_visa.constants import DATABASE_NAME
from us_visa.exception import CustomException
from us_visa.logger import logging

import numpy as np 
import pandas as pd 

from typing import Optional 


class USvisaData:


    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise CustomException(e,sys)

    
    def export_collection_as_dataframe(self, collection_name:str, database_name:Optional[str]=None)->pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in list(df.columns):
                df = df.drop(columns="_id")
            df.replace({"na":np.nan}, inplace = True)
            return df

        except Exception as e:
            raise CustomException(e,sys)




