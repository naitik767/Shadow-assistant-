import json
import os

TASK_FILE = 'tasks_gui.json'

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    return []

def get_completed_count():
    tasks = load_tasks()
    return sum(1 for task in tasks if task.get("completed"))

def get_pending_count():
    tasks = load_tasks()
    return sum(1 for task in tasks if not task.get("completed"))
