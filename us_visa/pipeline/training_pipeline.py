import sys 

from us_visa.exception import CustomException
from us_visa.logger import logging

from us_visa.components.data_ingestion import DataIngestion
from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.entity.config_entity import DataIngestionConfig

class TrainingPipeline:

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()


    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:

            logging.info("entered start-data_ingestion in trainiing_pipeline.py")
            logging.info("Getting data from MongoDB")

            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info("Got train and test dataset")
            logging.info("Exited start_data_ingestion of training pipeline")

            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e,sys)

    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise CustomException(e,sys)
