from textSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline 
from textSummarizer.logging import logger

STAGE_NAME= "data ingestion stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} starting")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "data validation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} starting")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e