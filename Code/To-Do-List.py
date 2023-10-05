import tkinter as tk
from tkinter import messagebox
import json

def toggle_completion():
    selected_item = listbox.curselection()
    if selected_item:
        index = selected_item[0]
        task = to_do_items[index]
        if task.startswith("✓ "):
            task = task[2:]
        else:
            task = "✓ " + task
        to_do_items[index] = task
        update_listbox()
        save_list()

def add_item(event=None):
    item = entry.get()
    if item:
        to_do_items.append(item)
        update_listbox()
        entry.delete(0, tk.END)
        save_list()

def remove_item():
    selected_item = listbox.curselection()
    if selected_item:
        index = selected_item[0]
        to_do_items.pop(index)
        update_listbox()
        save_list()

def clear_all():
    global to_do_items
    to_do_items = []
    update_listbox()
    save_list()

def update_listbox():
    listbox.delete(0, tk.END)
    for item in to_do_items:
        listbox.insert(tk.END, "• " + item)
        if item.startswith("✓ "):
            listbox.itemconfig(tk.END, {'fg': 'gray12'})

def save_list():
    with open("todo_list.json", "w") as file:
        json.dump(to_do_items, file)

def load_list():
    global to_do_items
    try:
        with open("todo_list.json", "r") as file:
            to_do_items = json.load(file)
            update_listbox()
    except FileNotFoundError:
        to_do_items = []

app = tk.Tk()
app.title("To-Do List")
app.geometry("600x400")
app.configure(bg="gray12")

to_do_items = []

entry_frame = tk.Frame(app, bg="gray12")
entry = tk.Entry(entry_frame, width=50, bg="gray", fg="lawngreen")
add_button = tk.Button(entry_frame, text="Add", width=10, command=add_item, bg="gray12", fg="gray", relief=tk.RAISED)
entry_frame.pack()
entry.pack(pady=10)
add_button.pack(pady=(0, 5))  # Reduce the gap below "Add" button by 50%

listbox_frame = tk.Frame(app, bg="gray12", padx=20, pady=10)
listbox_frame.pack(fill=tk.BOTH, expand=True, padx=20)  # Add padding to the left and right sides

listbox = tk.Listbox(listbox_frame, selectmode=tk.SINGLE, height=10, width=40, bg="gray", fg="lawngreen", selectbackground="gray19")
listbox.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(app, bg="gray12", pady=20)  # Increase top and bottom padding for buttons by 100%
remove_button = tk.Button(button_frame, text="Remove", width=10, command=remove_item, bg="gray12", fg="gray", relief=tk.RAISED)
completed_button = tk.Button(button_frame, text="Completed", width=10, command=toggle_completion, bg="gray12", fg="gray", relief=tk.RAISED)
clear_all_button = tk.Button(button_frame, text="Clear All", width=10, command=clear_all, bg="gray12", fg="gray", relief=tk.RAISED)
remove_button.pack(side=tk.LEFT, padx=5)
completed_button.pack(side=tk.LEFT, padx=5)
clear_all_button.pack(side=tk.LEFT, padx=5)
button_frame.pack()

entry.bind("<Return>", add_item)

load_list()

app.mainloop()
