import tkinter as tk
from datetime import datetime

def add_task():
    task = entry_task.get()
    deadline = entry_deadline.get()
    if task:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_with_timestamp = f"{timestamp} - {task} (Deadline: {deadline})"
        listbox_tasks.insert(tk.END, task_with_timestamp)
        entry_task.delete(0, tk.END)
        entry_deadline.delete(0, tk.END)

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        pass

def complete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(task_index, {'bg': 'light gray', 'fg': 'gray'})
    except IndexError:
        pass

def edit_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        old_task = listbox_tasks.get(task_index)
        entry_task.delete(0, tk.END)
        entry_task.insert(tk.END, old_task.split(" - ", 1)[1].split(" (Deadline: ")[0])
        entry_deadline.delete(0, tk.END)
        entry_deadline.insert(tk.END, old_task.split(" (Deadline: ")[1][:-1])
        delete_task()
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10, bd=0, bg='white', fg='black')
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

label_task = tk.Label(root, text="Task:")
label_task.pack()

entry_task = tk.Entry(root, width=50)
entry_task.pack()

label_deadline = tk.Label(root, text="Deadline (optional):")
label_deadline.pack()

entry_deadline = tk.Entry(root, width=50)
entry_deadline.pack()

button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_complete_task = tk.Button(root, text="Complete Task", width=48, command=complete_task)
button_complete_task.pack()

button_edit_task = tk.Button(root, text="Edit Task", width=48, command=edit_task)
button_edit_task.pack()

root.mainloop()
