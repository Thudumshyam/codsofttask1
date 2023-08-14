from tkinter import *

# define tasks

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_tasks()
 
def delete_task():
    selected = tasks_listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_tasks()


def edit_task():
    selected = tasks_listbox.curselection()
    if selected:
        edit_window = Tk()
        edit_window.title("EDIT TASK")

        edit_label = Label(edit_window, text="Edit the task:",font=("",25))
        edit_label.pack()

        edit_entry = Entry(edit_window, width=30,font=("",25))
        edit_entry.pack()

        edit_button = Button(edit_window, text="Update",command=lambda: update_task(selected[0], edit_entry.get(), edit_window),width=8,height=3)
        edit_button.pack()

        edit_entry.insert(END, tasks[selected[0]])

    def update_task(index, new_task, window):
        tasks[index] = new_task
        window.destroy()
        update_tasks()


def update_tasks():
    tasks_listbox.delete(0, END)
    for task in tasks:
        tasks_listbox.insert(END, task)


tasks = []

root = Tk()
root.title("To-Do List")
label_head =Label(root,text="To Do List",font=("",50),background=("green"))
label_head.pack(fill= BOTH)

label = Label(root, text="Enter a task:",font=("",30))
label.pack()

entry = Entry(root, width=20,font=("",20))
entry.place(x=900,y=90)

add_button = Button(root, text="Add Task", command=add_task,width=9,height=3)
add_button.pack()

edit_button = Button(root, text="Edit Task", command=edit_task,width=9,height=3)
edit_button.pack()

delete_button = Button(root, text="Delete Task", command=delete_task,width=9,height=3)
delete_button.pack()

tasks_listbox = Listbox(root,font=("",30),height=7)
tasks_listbox.pack()

update_tasks()

root.mainloop()
