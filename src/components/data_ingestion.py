from src.logging import logger
from src.config.configuration import DataIngestionConfig
import os 
import zipfile
from urllib import request
from src.config.configuration import ConfigurationManager
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config 
        
    def download_dataset(self):
        if not os.path.exists(self.config.local_data_file): # check if the dataset is downloaded or not 
            filename, headers  = request.urlretrieve(
                url = self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info("Dataset is downloaded!")
        else:
            logger.info("Dataset already exists!")
            
    def extract_dataset(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip: 
            zip.extractall(unzip_path)
            

