import os
import json
from datetime import datetime

# Ruta al archivo donde se guardan las tareas
task_file = os.path.join(os.path.dirname(__file__), "tasks.json")

# Crear un archivo vacío si no existe
if not os.path.exists(task_file):
    with open(task_file, "w") as file:
        json.dump([], file, indent=4)
    print("Archivo tasks.json creado correctamente.")

def save_tasks(tasks):
    """
    Guarda las tareas en el archivo JSON.
    """
    try:
        with open(task_file, "w") as file:
            json.dump([
                {
                    "name": task["name"],
                    "description": task["description"],
                    "datetime": task["datetime"].strftime("%Y-%m-%d %H:%M:%S") if isinstance(task["datetime"], datetime) else task["datetime"],
                    "id": task["id"],
                    "importance": task.get("importance", "Regular")
                }
                for task in tasks
            ], file, indent=4)
        print("Tareas guardadas correctamente en tasks.json.")
    except Exception as e:
        print(f"Error al guardar las tareas: {e}")

def load_tasks():
    """
    Carga las tareas desde el archivo JSON y convierte el campo 'datetime' a objetos datetime.
    """
    try:
        with open(task_file, "r") as file:
            tasks = json.load(file)
            for task in tasks:
                if isinstance(task["datetime"], str):
                    task["datetime"] = datetime.strptime(task["datetime"], "%Y-%m-%d %H:%M:%S")
            print(f"{len(tasks)} tareas cargadas desde el archivo tasks.json.")
            return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        print("El archivo tasks.json no existe o está corrupto. Creando un archivo nuevo.")
        with open(task_file, "w") as file:
            file.write("[]")
        return []
    except Exception as e:
        print(f"Error al cargar las tareas: {e}")
        return []

def check_due_tasks(tasks):
    """
    Verifica si hay tareas vencidas.
    """
    try:
        now = datetime.now()
        due_tasks = [task for task in tasks if isinstance(task["datetime"], datetime) and task["datetime"] <= now]
        print(f"{len(due_tasks)} tareas vencidas encontradas.")
        return due_tasks
    except Exception as e:
        print(f"Error al verificar las tareas vencidas: {e}")
        return []

def add_task(name, description, task_datetime):
    """
    Añade una nueva tarea.
    """
    try:
        task = {
            "name": name,
            "description": description,
            "datetime": task_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "id": datetime.now().timestamp(),
            "importance": "Regular"
        }
        print(f"Tarea '{name}' agregada correctamente.")
        return task
    except Exception as e:
        print(f"Error al añadir una nueva tarea: {e}")
        return None

def remove_task_by_id(task_id, tasks):
    """
    Elimina una tarea por su ID.
    """
    try:
        tasks = [task for task in tasks if task["id"] != task_id]
        print(f"Tarea con ID {task_id} eliminada correctamente.")
        return tasks
    except Exception as e:
        print(f"Error al eliminar una tarea: {e}")
        return tasks

