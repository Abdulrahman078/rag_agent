# Using the ConfigParser to read all the settings from the config.cfg file and parse it here in the config file
# creating a centralized configuration file for the project
import configparser

parser = configparser.ConfigParser()

parser.read("config.cfg")

MODEL = parser['DEFAULT']['model'] #  you can printout the value to makesure its working : print(MODEL)