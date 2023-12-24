ARTIFACTS_DIR: str = "artifacts"

'''
Data Ingestion related  constants start with DATA_INGESTION VAR NAME
'''

DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/1ydJ2orU0v-odMwbBMooYS-kBB7ST6i-S/view?usp=drive_link"


# artifacts/data_ingestion/data.zip 
# artifacts/data_ingestion/feature_store/all_features

"""
Data Validation related contant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ['train', 'valid', 'test', 'data.yaml']


"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"