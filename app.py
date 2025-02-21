import tkinter as tk
from tkinter import messagebox, font
from database import *

init_db()

# GUI setup
root = tk.Tk()
root.title("Daily Tasks")
root.geometry("1920x1080")

# Create custom font
custom_font = font.Font(size=16)

# Create a custom Listbox class to store additional data
class DataListbox(tk.Listbox):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._data = {}
    
    def set_data(self, index, key, value):
        if index not in self._data:
            self._data[index] = {}
        self._data[index][key] = value
    
    def get_data(self, index, key):
        return self._data.get(index, {}).get(key)
    
    def clear_data(self):
        self._data = {}

def add_task_gui(event=None):
    task = task_entry.get()
    if task:
        add_task(task)
        task_entry.delete(0, tk.END)
        refresh_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task_gui():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_id = task_listbox.get_data(selected_task[0], "task_id")
        delete_task(task_id)
        refresh_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def toggle_completed_gui():
    selected_task = task_listbox.curselection()
    if selected_task:
        selected_index = selected_task[0]  # Store the selected index
        task_id = task_listbox.get_data(selected_index, "task_id")
        toggle_completed(task_id)
        refresh_tasks(selected_index)  # Pass the selected index to refresh_tasks
    else:
        messagebox.showwarning("Warning", "No task selected!")

def refresh_tasks(maintain_selection=None):
    task_listbox.delete(0, tk.END)
    task_listbox.clear_data()
    tasks = get_tasks()
    for index, task in enumerate(tasks, start=1):
        task_id, task_text, completed, _ = task
        status = "✔" if completed else "X"
        display_text = f"{index}. {task_text} {status}"
        task_listbox.insert(tk.END, display_text)
        task_listbox.set_data(index-1, "task_id", task_id)
    
    # If we need to maintain selection and the index is valid
    if maintain_selection is not None and maintain_selection < task_listbox.size():
        task_listbox.selection_set(maintain_selection)
        task_listbox.see(maintain_selection)  # Ensure the selected item is visible

# UI LAYOUT
frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=100, font=custom_font)
task_entry.pack(side=tk.LEFT, padx=5)

task_entry.bind('<Return>', add_task_gui)

add_button = tk.Button(frame, text="Add Task", command=add_task_gui, font=custom_font)
add_button.pack(side=tk.LEFT)

task_listbox = DataListbox(root, width=150, height=35, font=custom_font)
task_listbox.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task_gui, font=custom_font)
delete_button.pack(side=tk.LEFT, padx=5)

complete_button = tk.Button(button_frame, text="Toggle Completed", command=toggle_completed_gui, font=custom_font)
complete_button.pack(side=tk.LEFT, padx=5)

refresh_tasks()

# Run
root.mainloop()