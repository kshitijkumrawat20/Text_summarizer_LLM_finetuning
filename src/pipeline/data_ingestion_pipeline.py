from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.logging import logger


config= ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()
data_ingestion = DataIngestion(config=data_ingestion_config)
data_ingestion.download_dataset()
data_ingestion.extract_dataset()