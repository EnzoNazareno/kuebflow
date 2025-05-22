import shutil
import os

os.makedirs("/home/jovyan", exist_ok=True)
shutil.copy("/home/jovyan/data/intents.json", "/home/jovyan/intents.json")
shutil.copy("/home/jovyan/data/Mental_Health_FAQ.csv", "/home/jovyan/Mental_Health_FAQ.csv")
