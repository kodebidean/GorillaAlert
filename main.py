import os
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta
from pystray import Icon, MenuItem, Menu
from PIL import Image
from tasks import load_tasks, save_tasks, add_task, check_due_tasks, remove_task_by_id

# Cargar tareas existentes
tasks = load_tasks()

# Función para actualizar la lista de tareas
def update_task_list(task_listbox):
    task_listbox.delete(0, tk.END)
    for task in tasks:
        importance_color = {
            "Muy Importante": "#FF6B6B",
            "Importante": "#FFA94D",
            "Regular": "#FFD43B",
            "Simple": "#69DB7C"
        }.get(task.get("importance", "Regular"), "white")
        task_display = f"{task['name']} - {task['datetime']} ({task.get('importance', 'Regular')})"
        task_listbox.insert(tk.END, task_display)
        task_listbox.itemconfig(tk.END, bg=importance_color)

# Mostrar ventana emergente para tareas vencidas
def show_popup(task, task_listbox):
    """
    Muestra una ventana emergente para tareas vencidas.
    """
    popup = tk.Toplevel()
    popup.title("Recordatorio de Tarea")
    popup.geometry("500x400")
    popup.configure(bg="#2C2F33")
    popup.attributes("-fullscreen", True)
    tk.Label(popup, text=f"Tarea: {task['name']}", font=("Helvetica", 20, "bold"), bg="#2C2F33", fg="white").pack(pady=20)
    tk.Label(popup, text=f"Descripción: {task['description']}", font=("Helvetica", 16), bg="#2C2F33", fg="white").pack(pady=10)

    def complete_task():
        tasks[:] = remove_task_by_id(task["id"], tasks)
        save_tasks(tasks)
        update_task_list(task_listbox)
        popup.destroy()

    def postpone_task():
        def apply_postpone():
            try:
                minutes = int(minutes_entry.get())
                new_time = datetime.now() + timedelta(minutes=minutes)
                task["datetime"] = new_time.strftime("%Y-%m-%d %H:%M:%S")
                task["processed"] = False  # Permitir que el popup vuelva a aparecer más tarde
                save_tasks(tasks)
                update_task_list(task_listbox)
                postpone_popup.destroy()
                popup.destroy()
            except ValueError:
                messagebox.showerror("Error", "Ingrese minutos válidos.")

        postpone_popup = tk.Toplevel()
        postpone_popup.title("Posponer Tarea")
        postpone_popup.geometry("300x150")
        postpone_popup.configure(bg="#2C2F33")

        tk.Label(postpone_popup, text="Minutos para posponer:", bg="#2C2F33", fg="white").pack(pady=10)
        minutes_entry = tk.Entry(postpone_popup)
        minutes_entry.pack(pady=5)
        tk.Button(postpone_popup, text="Aceptar", command=apply_postpone, bg="#7289DA", fg="white").pack(pady=10)

    tk.Button(popup, text="Completar", command=complete_task, bg="#43B581", fg="white", font=("Helvetica", 14)).pack(pady=10)
    tk.Button(popup, text="Posponer", command=postpone_task, bg="#F04747", fg="white", font=("Helvetica", 14)).pack(pady=10)


# Función para verificar tareas vencidas
def check_and_show_due_tasks(task_listbox, root):
    """
    Verifica si hay tareas vencidas y muestra un popup solo una vez.
    """
    now = datetime.now()
    margin = timedelta(seconds=10)  # Margen de error de 10 segundos
    for task in tasks:
        try:
            # Convertir a datetime si es necesario
            task_time = task["datetime"]
            if isinstance(task_time, str):
                task_time = datetime.strptime(task_time, "%Y-%m-%d %H:%M:%S")
                task["datetime"] = task_time  # Actualizamos en memoria

            # Mostrar popup si la tarea está dentro del margen y no se ha procesado
            if task_time <= now + margin and not task.get("processed", False):
                show_popup(task, task_listbox)
                task["processed"] = True  # Marcamos la tarea como procesada
                save_tasks(tasks)  # Guardamos el cambio
        except Exception as e:
            print(f"Error al verificar tarea '{task['name']}': {e}")
            
    # Ejecuta esta función cada 60 segundos incluso si la ventana está minimizada
    task_listbox.after(60000, lambda: check_and_show_due_tasks(task_listbox, root))

# Función para crear el icono en la bandeja del sistema
def create_tray_icon(root):
    def show_window(icon, item):
        icon.stop()
        root.after(0, root.deiconify)  # Restaura la ventana principal

    def exit_app(icon, item):
        icon.stop()
        root.quit()  # Cierra la aplicación

    icon_path = os.path.join(os.path.dirname(__file__), "iconoGestortareas.ico")
    image = Image.open(icon_path) if os.path.exists(icon_path) else None

    menu = Menu(
        MenuItem("Abrir Gestor", lambda: show_window(tray_icon, None)),
        MenuItem("Salir", lambda: exit_app(tray_icon, None))
    )

    tray_icon = Icon("GorillaAlert", image, "Gestor de Tareas", menu)
    tray_icon.run()

# Crear la interfaz principal
def create_gui():
    root = tk.Tk()
    root.title("Gestor de Tareas")
    root.geometry("600x500")
    root.configure(bg="#23272A")

    # Cerrar la ventana y mostrar en la bandeja del sistema
    root.protocol("WM_DELETE_WINDOW", lambda: root.withdraw() or create_tray_icon(root))

    # Lista de tareas
    task_frame = tk.Frame(root, bg="#23272A")
    task_frame.pack(pady=10)

    task_listbox = tk.Listbox(task_frame, width=70, height=12, bg="#2C2F33", fg="white", font=("Helvetica", 10))
    task_listbox.pack(side=tk.LEFT, padx=10)

    scrollbar = tk.Scrollbar(task_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    task_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=task_listbox.yview)

 # Formulario para agregar tareas
    add_task_frame = tk.Frame(root, bg="#23272A")
    add_task_frame.pack(pady=10)

    tk.Label(add_task_frame, text="Nombre:", bg="#23272A", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    name_entry = tk.Entry(add_task_frame, width=35)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(add_task_frame, text="Descripción:", bg="#23272A", fg="white").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    desc_entry = tk.Entry(add_task_frame, width=35)
    desc_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(add_task_frame, text="Fecha (YYYY-MM-DD):", bg="#23272A", fg="white").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    date_entry = tk.Entry(add_task_frame, width=35)
    date_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(add_task_frame, text="Hora (HH:MM):", bg="#23272A", fg="white").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    time_entry = tk.Entry(add_task_frame, width=35)
    time_entry.grid(row=3, column=1, padx=5, pady=5)

    # Combobox para seleccionar la prioridad
    tk.Label(add_task_frame, text="Importancia:", bg="#23272A", fg="white").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    importance_combo = ttk.Combobox(add_task_frame, values=["Muy Importante", "Importante", "Regular", "Simple"], state="readonly", font=("Helvetica", 10))
    importance_combo.grid(row=4, column=1, padx=5, pady=5)
    importance_combo.set("Regular")

    # Botón para agregar tarea
    tk.Button(
        add_task_frame, text="Agregar Tarea",
        command=lambda: add_task_gui(task_listbox, name_entry, desc_entry, date_entry, time_entry, importance_combo),
        bg="#43B581", fg="white"
    ).grid(row=5, column=0, columnspan=2, pady=10)


    # Botón para eliminar tarea
    tk.Button(root, text="Eliminar Tarea", command=lambda: delete_task(task_listbox), bg="#F04747", fg="white").pack(pady=10)

    # Actualización de la lista y verificación periódica
    update_task_list(task_listbox)
    task_listbox.after(1000, lambda: check_and_show_due_tasks(task_listbox, root))  # Pasa root correctamente
    root.mainloop()


# Función para agregar tarea desde la GUI
def add_task_gui(task_listbox, name_entry, desc_entry, date_entry, time_entry, importance_combo):
    """
    Agrega una nueva tarea con prioridad seleccionada desde la interfaz.
    """
    try:
        task_datetime = datetime.strptime(f"{date_entry.get()} {time_entry.get()}", "%Y-%m-%d %H:%M")
        importance = importance_combo.get()  # Obtener la prioridad seleccionada
        new_task = add_task(name_entry.get(), desc_entry.get(), task_datetime)
        new_task["importance"] = importance  # Añadir prioridad a la tarea
        tasks.append(new_task)
        save_tasks(tasks)
        update_task_list(task_listbox)
        messagebox.showinfo("Éxito", "Tarea agregada correctamente.")
    except ValueError:
        messagebox.showerror("Error", "Formato de fecha/hora incorrecto. Use YYYY-MM-DD y HH:MM.")


# Función para eliminar tarea
def delete_task(task_listbox):
    selected_index = task_listbox.curselection()
    if selected_index:
        tasks.pop(selected_index[0])
        save_tasks(tasks)
        update_task_list(task_listbox)
        messagebox.showinfo("Éxito", "Tarea eliminada correctamente.")

# Ejecutar la GUI
if __name__ == "__main__":
    create_gui()
