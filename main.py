from textSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline 
from textSummarizer.pipeline.stage04_model_trainer import ModelTrainerPipeline
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

STAGE_NAME= "data transformation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} starting")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "model train stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} starting")
    model_trainer=ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e