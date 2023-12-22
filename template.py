import os
from pathlib import Path
import logging # python inbuilt logging

# create logging string
# initialise infomration related log and format string -> logs ascii time and message to print
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

### Automating project template creation ###

project_name = "cellSegmentation"

list_of_files = [
    ".github/workflows/.gitkeep", # needed for automatic deployment in Azure
    "data/.gitkeep", # .gitkeep is a trick we use to create empty directories in Git repository
    f"{project_name}/__init__.py", # local constructor
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py", # training related constants
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/exception/__init__.py", # exceptions module
    f"{project_name}/logger/__init__.py",   # logging modules
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",    # utils module
    f"{project_name}/utils/main_utils.py",
    "research/trials.ipynb",    # notebook file
    "templates/index.html",     # UI html template
    "app.py",   # end point
    "Dockerfile",
    "requirements.txt", # packages needed fro project
    "setup.py",     # for local package installation
]


for file_path in list_of_files:
    file_path = Path(file_path) # this automaticaly detects whether we have a linux path or windoes path -> avoid errors

    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file {file_name}")

    
    if(not os.path.exists(file_name)) or (os.path.getsize(file_name) == 0):
        with open(file_path, "w") as file_obj:
            pass
            logging.info(f"Creating empty file: {file_name}")

    else:
        logging.info(f"{file_name} is already created")