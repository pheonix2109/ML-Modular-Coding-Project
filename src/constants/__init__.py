import os, sys
from datetime import datetime


# artifact -> pipeline folder -> timestamp -> output

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_time_stamp()

ROOT_DIR_KEY = os.getcwd()
DATA_DIR = "Data"
DATA_DIR_KEY = "finalTrain.csv"

ARTIFACT_DIR_KEY = "Artifact"

#data ingestion related variable
DATA_INGESTION_KEY = "data_ingestion"
DATA_INGESTION_RAW_DATA_DIR = "raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_KEY = "ingested_dir"
RAW_DATA_DIR_KEY = "raw.csv"
TRAIN_DATA_DIR_KEY ="train.csv"
TEST_DATA_DIR_KEY = "test.csv"



# DaTA Transformation Related Variable

DATA_TRANSFORMATION_ARTIFACT = "data_transformation"
DATA_PREPROCESSED_DIR = "processor"
DATA_TRANSFORMATION_PROCESSING_OBJ = "processor.pkl"
DATA_TRANSFORM_DIR = "transformation"
TRANSFORM_TRAIN_DIR_KEY = "train.csv"
TRANSFORM_TEST_DIR_KEY = "test.csv"

# artifact / data_transformation / processor -> processor.pkl and transformation -> train.csv and test.csv


