import os,sys
import yaml
from cellSegmentation.utils.main_utils import read_yaml_file
from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
from cellSegmentation.entity.config_entity import ModelTrainerConfig
from cellSegmentation.entity.artifacts_entity import ModelTrainerArtifact

# we will have bash scripting commands here

class ModelTrainer:
    def __init__(
            self,
            model_trainer_config: ModelTrainerConfig
    ):
        self.model_trainer_config = model_trainer_config


    def initiate_model_training(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")
            # execute bash commands with os.system("command")
            os.system("unzip data.zip")
            os.system("rm data.zip")

            os.system(f"yolo task=segment mode=train model={self.model_trainer_config.weight_name} data=data.yaml epochs={self.model_trainer_config.no_epochs} imgsz=640 save=true")
            
            # copy directory
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(f"c runs/segment/train/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")

            # only keep weights remove other files
            os.system("rm -rf yolov8l-seg.pt")
            os.system("rm -rf train")
            os.system("rm -rf valid")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")
            os.system("rm -rf runs")
            os.system("rm README.dataset.txt")
            os.system("rm README.roboflow.txt")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="artifacts/model_trainer/best.pt"
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact
            
        except Exception as e:
            raise AppException(e, sys)
