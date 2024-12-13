import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta
import threading
from tasks import load_tasks, save_tasks, add_task, check_due_tasks

# Load existing tasks
tasks = load_tasks()

# Function to update the task list in the GUI
def update_task_list(task_listbox):
    task_listbox.delete(0, tk.END)
    for task in tasks:
        importance_color = {
            "Muy Importante": "red",
            "Importante": "orange",
            "Regular": "yellow",
            "Simple": "green"
        }.get(task.get("importance", "Regular"), "white")
        task_display = f"{task['name']} - {task['datetime']} ({task.get('importance', 'Regular')})"
        task_listbox.insert(tk.END, task_display)
        task_listbox.itemconfig(tk.END, bg=importance_color)

# Function to add a new task
def add_task_gui(task_listbox, name_entry, desc_entry, date_entry, time_entry, importance_combo):
    name = name_entry.get()
    description = desc_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    importance = importance_combo.get()
    try:
        task_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        new_task = add_task(name, description, task_datetime)
        new_task["importance"] = importance  # Add importance to the task
        tasks.append(new_task)
        save_tasks(tasks)
        update_task_list(task_listbox)
        messagebox.showinfo("Éxito", "Tarea agregada correctamente.")
    except ValueError:
        messagebox.showerror("Error", "Formato de fecha/hora incorrecto. Use YYYY-MM-DD y HH:MM.")

# Function to delete a selected task
def delete_task(task_listbox):
    selected_index = task_listbox.curselection()
    if selected_index:
        task_to_delete = tasks[selected_index[0]]
        tasks.remove(task_to_delete)
        save_tasks(tasks)
        update_task_list(task_listbox)
        messagebox.showinfo("Éxito", "Tarea eliminada correctamente.")
    else:
        messagebox.showerror("Error", "Seleccione una tarea para eliminar.")

# Function to check due tasks in the background
def monitor_tasks(task_listbox):
    while True:
        due_tasks = check_due_tasks(tasks)
        for task in due_tasks:
            # Crear un pop-up bloqueante personalizado
            popup = tk.Toplevel()
            popup.title("Tarea Pendiente")
            popup.attributes("-fullscreen", True)  # Hacer que la ventana sea de pantalla completa
            popup.resizable(False, False)

            # Color de fondo según la importancia
            importance_color = {
                "Muy Importante": "red",
                "Importante": "orange",
                "Regular": "yellow",
                "Simple": "green"
            }.get(task.get("importance", "Regular"), "white")
            popup.configure(bg=importance_color)

            # Mostrar información de la tarea
            tk.Label(
                popup,
                text=f"Tarea: {task['name']}",
                font=("Arial", 24, "bold"),
                bg=importance_color,
                fg="white"
            ).pack(pady=20)
            tk.Label(
                popup,
                text=f"Descripción: {task['description']}",
                font=("Arial", 18),
                bg=importance_color,
                fg="white"
            ).pack(pady=20)

            # Botones para completar o posponer la tarea
            def complete_task():
                tasks.remove(task)
                save_tasks(tasks)
                update_task_list(task_listbox)  # Actualizar la lista de tareas
                popup.destroy()

            def postpone_task():
                # Crear una entrada para los minutos a posponer
                def apply_postpone():
                    try:
                        # Leer minutos de la entrada
                        minutes = int(minutes_entry.get())
                        new_time = datetime.now() + timedelta(minutes=minutes)
                        task["datetime"] = new_time.strftime("%Y-%m-%d %H:%M:%S")
                        save_tasks(tasks)
                        update_task_list(task_listbox)  # Actualizar la lista de tareas
                        postpone_popup.destroy()
                        popup.destroy()
                    except ValueError:
                        messagebox.showerror("Error", "Ingrese un número válido de minutos.")

                # Crear un pop-up para ingresar los minutos
                postpone_popup = tk.Toplevel()
                postpone_popup.title("Posponer tarea")
                postpone_popup.geometry("300x150")
                postpone_popup.resizable(False, False)

                tk.Label(postpone_popup, text="Ingrese los minutos para posponer:", font=("Arial", 12)).pack(pady=10)
                minutes_entry = tk.Entry(postpone_popup, width=10, font=("Arial", 12))
                minutes_entry.pack(pady=5)

                tk.Button(postpone_popup, text="Aceptar", command=apply_postpone, font=("Arial", 12)).pack(pady=10)

                postpone_popup.grab_set()  # Bloquear interacción con otras ventanas
                postpone_popup.focus_set()

            tk.Button(popup, text="Completar la tarea", command=complete_task, font=("Arial", 16)).pack(pady=10)
            tk.Button(popup, text="Posponer", command=postpone_task, font=("Arial", 16)).pack(pady=10)

            # Bloquear cualquier acción en el sistema operativo
            popup.protocol("WM_DELETE_WINDOW", lambda: None)  # Desactiva el botón de cerrar
            popup.focus_set()  # Forzar el foco en la ventana
            popup.grab_set()  # Bloquear interacción con el resto del sistema operativo
            popup.wait_window()

        threading.Event().wait(60)  # Comprobar cada 60 segundos

# Create the main GUI
def create_gui():
    root = tk.Tk()
    root.title("Gestor de Tareas")

    # Task list frame
    task_frame = tk.Frame(root)
    task_frame.pack(pady=10)

    task_listbox = tk.Listbox(task_frame, width=50, height=10)
    task_listbox.pack(side=tk.LEFT, padx=10)

    scrollbar = tk.Scrollbar(task_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    task_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=task_listbox.yview)

    # Add task frame
    add_task_frame = tk.Frame(root)
    add_task_frame.pack(pady=10)

    tk.Label(add_task_frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(add_task_frame, width=20)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(add_task_frame, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
    desc_entry = tk.Entry(add_task_frame, width=20)
    desc_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(add_task_frame, text="Fecha (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
    date_entry = tk.Entry(add_task_frame, width=20)
    date_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(add_task_frame, text="Hora (HH:MM):").grid(row=3, column=0, padx=5, pady=5)
    time_entry = tk.Entry(add_task_frame, width=20)
    time_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(add_task_frame, text="Importancia:").grid(row=4, column=0, padx=5, pady=5)
    importance_combo = ttk.Combobox(add_task_frame, values=["Muy Importante", "Importante", "Regular", "Simple"], state="readonly")
    importance_combo.grid(row=4, column=1, padx=5, pady=5)
    importance_combo.set("Regular")

    tk.Button(
        add_task_frame, text="Agregar Tarea",
        command=lambda: add_task_gui(task_listbox, name_entry, desc_entry, date_entry, time_entry, importance_combo)
    ).grid(row=5, column=0, columnspan=2, pady=10)

    # Delete task button
    tk.Button(
        root, text="Eliminar Tarea",
        command=lambda: delete_task(task_listbox),
        font=("Arial", 12)
    ).pack(pady=10)
    
    

    # Load tasks into the listbox
    update_task_list(task_listbox)

    # Start the task monitor in a separate thread
    threading.Thread(target=lambda: monitor_tasks(task_listbox), daemon=True).start()

    root.mainloop()

if __name__ == "__main__":
    create_gui()