import os
import json 

FILE_PATH = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_PATH): return[]
    with open(FILE_PATH, "r", encoding ="UTF-8") as f:
        return json.load(f)
def save_tasks(tasks): 
    with open(FILE_PATH, "w", encoding = "UTF-8")as t: 
        json.dump(tasks, t, indent=4, ensure_ascii=False)