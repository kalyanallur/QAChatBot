import logging
import os
import datetime

date = datetime.datetime.now().strftime("%d_%m_%y_%H_%M_%S_")
dir_path = os.path.join(os.getcwd(),"src","Log")
if not os.path.exists(dir_path):
    os.makedirs(dir_path, exist_ok=True)
log_filepath = os.path.join(dir_path,f"{date}.log")

logging.basicConfig(
    filename = log_filepath,format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO
)
logging.info("Log file created successfully")