import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project="ML_project"

list_of_files=[
    f"srce/{project}/__init__.py",
    f"srce/{project}/components/__init__.py",
    f"srce/{project}/components/data_ingestion.py",
    f"srce/{project}/components/data_trans.py",
    f"srce/{project}/components/model_training.py",
    f"srce/{project}/components/model_mon.py",
    f"srce/{project}/pipelines/__init__.py",
    f"srce/{project}/pipelines/train_pipeline.py",
    f"srce/{project}/pipelines/pred_pipeline.py",
    f"srce/{project}/exception.py",
    f"srce/{project}/logger.py",
    f"srce/{project}/utilis.py",
    "app.py",
    "Dockerfile",
    "setup.py",
    "rndom.txt",
   
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if not filepath.exists():
        with open(filepath, 'w') as f:
            pass  
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")



