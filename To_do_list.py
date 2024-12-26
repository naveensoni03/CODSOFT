from tkinter import*
import tkinter as tk
from tkinter import messagebox


def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
      
        task_entry.delete(0, tk.END) 
    else:
        messagebox.showwarning("Input Error", "Please Enter a Task.")


def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")


def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, task + " - Completed")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Create main window
charge = tk.Tk()
charge.title("To-Do List")
charge.resizable(False,False)
charge.configure(bg="#de9874")


# Create a frame for better layout
frame = tk.Frame(charge)
frame.pack(pady=10)

# Entry widget to type in tasks
task_entry = tk.Entry(frame, width=40)
task_entry.grid(row=0, column=0, padx=20)

# Button to add task
add_button = tk.Button(frame, text="Add Task", width=20, command=add_task)
add_button.grid(row=0, column=1)

# Listbox to display tasks
task_listbox = tk.Listbox(charge, width=50, height=10, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

# Buttons to delete or complete tasks
delete_button = tk.Button(charge, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(charge, text="Mark as Completed", width=20, command=complete_task)
complete_button.pack(pady=5)


charge.mainloop()
