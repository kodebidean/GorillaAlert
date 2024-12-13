# tasks.py
import json
from datetime import datetime

# File to store tasks
task_file = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(task_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file does not exist, return an empty list
        return []
    except json.JSONDecodeError:
        # If the file is empty or corrupt, reset it to an empty list
        with open(task_file, "w") as file:
            file.write("[]")  # Write a valid empty JSON array
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(task_file, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(name, description, task_datetime):
    task = {
        "name": name,
        "description": description,
        "datetime": task_datetime.strftime("%Y-%m-%d %H:%M:%S")
    }
    return task

# Check tasks for due dates
def check_due_tasks(tasks):
    now = datetime.now()
    due_tasks = [task for task in tasks if datetime.strptime(task["datetime"], "%Y-%m-%d %H:%M:%S") <= now]
    return due_tasks
