import tkinter as tk
from tkinter import messagebox
from database import *

init_db()

#GUI setup
root = tk.Tk()
root.title("Daily Tasks")

def add_task_gui():
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
    task_id = task_listbox.get(selected_task)[0]
    delete_task(task_id)
    refresh_tasks()
  else:
    messagebox.showwarning("Warning", "No task selected!")

def mark_completed_gui():
  selected_task = task_listbox.curselection()
  if selected_task:
    task_id = task_listbox.get(selected_task)[0]
    mark_completed(task_id)
    refresh_tasks()
  else:
    messagebox.showwarning("Warning", "No task selected!")
  
def refresh_tasks():
  task_listbox.delete(0, tk.END)
  tasks = get_tasks()
  for task in tasks:
    status = "✔" if task[2] else "X"
    task_listbox.insert(tk.END, (task[0], task[1], status))

#UI LAYOUT
frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add Task", command=add_task_gui)
add_button.pack(side= tk.LEFT)

task_listbox = tk.Listbox(root, width=50, height = 10)
task_listbox.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

delete_button = tk.Button(frame, text="Delete Task", command=delete_task_gui)
delete_button.pack(side=tk.LEFT, padx=5)

complete_button = tk.Button(frame, text="Mark Completed", command=mark_completed_gui)
complete_button.pack(side=tk.LEFT, padx=5)

refresh_tasks()

#run
root.mainloop