from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
import sys, os

from cellSegmentation.pipeline.training_pipeline import TrainPipeline

# logging.info("log should show levelname")

# try:
#     a = 1/0
# except Exception as e:
#     logging.info("Divide by zero error")
#     raise AppException(e, sys)

obj = TrainPipeline()
obj.run_pipeline()
print("Training done")