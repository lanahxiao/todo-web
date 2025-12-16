import json
import os
import random
import string

DATA_FILE = "todo_data.json"

def generate_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                tasks = json.load(f)
                for task in tasks:
                    if 'id' not in task:
                        task['id'] = generate_id()
                return tasks
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task(text):
    tasks = load_tasks()
    tasks.append({
        "id": generate_id(),
        "text": text,
        "completed": False
    })
    save_tasks(tasks)

def toggle_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    tasks.sort(key=lambda x: x["completed"])
    save_tasks(tasks)

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
