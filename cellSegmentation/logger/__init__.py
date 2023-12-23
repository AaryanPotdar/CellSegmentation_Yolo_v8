import os
import logging # pre build logging module
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(current_dir, 'log', LOG_FILE) # will create log folder and inside that create a log file

os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)