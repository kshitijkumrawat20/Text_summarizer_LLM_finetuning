from Text_summarizer.config.configuration import ConfigurationManager
from Text_summarizer.components.data_ingestion import DataIngestion
from Text_summarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def intiate_data_ingestion(self):
        config= ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_dataset()
        data_ingestion.extract_dataset()

