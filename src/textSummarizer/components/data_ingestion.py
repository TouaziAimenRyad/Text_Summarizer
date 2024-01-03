import os
import gdown
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            gdown.download(self.config.source_URL, output=self.config.local_data_file, quiet=False)
            logger.info(f"File downloaded to: {self.config.local_data_file}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    
    #def extract_zip_file(self):
    #    """
    #    zip_file_path: str
    #    Extracts the zip file into the data directory
    #    Function returns None
    #    """
    #    unzip_path = self.config.unzip_dir
    #    os.makedirs(unzip_path, exist_ok=True)
    #    with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
    #        zip_ref.extractall(unzip_path)
    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        try:
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
        except zipfile.BadZipFile:
            logger.error(f"File '{self.config.local_data_file}' is not a valid zip file.")
            # Handle the error or raise an exception as needed
            # For example, you could delete the invalid zip file if it's not needed
            os.remove(self.config.local_data_file)
        except Exception as e:
            logger.error(f"An error occurred during zip file extraction: {e}")
            # Handle other exceptions if needed