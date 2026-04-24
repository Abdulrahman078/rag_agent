# Using the ConfigParser to read all the settings from the config.cfg file and parse it here in the config file
# creating a centralized configuration file for the project
import configparser
from dotenv import load_dotenv
import os

parser = configparser.ConfigParser()

parser.read("config.cfg")
load_dotenv()

#  you can printout the value to makesure its working e.g print(MODEL) 
MODEL = parser['DEFAULT']['MODEL'] 
EMBEDDING_MODEL = parser['DEFAULT']['EMBEDDING_MODEL']
CHUNK_SIZE = parser['DEFAULT']['CHUNK_SIZE']
CHUNK_OVERLAP = parser['DEFAULT']['CHUNK_OVERLAP']
TOP_K = parser['DEFAULT']['TOP_K']
DISTANCE_THRESHOLD = parser['DEFAULT']['DISTANCE_THRESHOLD']
EMBEDDING_REQUESTS_PER_MIN = parser['DEFAULT']['EMBEDDING_REQUESTS_PER_MIN']


PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")
