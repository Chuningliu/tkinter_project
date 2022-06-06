import tkinter
import tkinter.messagebox
root=tkinter.Tk()
root.title("TO-Do List by @Navgurukul Student")
def add_task():
    task=entry_task.get()
    if task!= "":
        listbox_tasks.insert(tkinter.END,task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning!",message="you must enter a task.")
def delete_task():
    try:
        task_index=listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="warning!",message="you must enter a task.")
frame_task=tkinter.Frame(root)
frame_task.pack()
listbox_tasks=tkinter.Listbox(frame_task,height=10,width=50)
listbox_tasks.pack(side=tkinter.LEFT)  
scrollbar_tasks=tkinter.Scrollbar(frame_task)
scrollbar_tasks.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)
entry_task=tkinter.Entry(root,width=50)
entry_task.pack()
button_add_task=tkinter.Button(root,text="Add task",width=48,command=add_task)
button_add_task.pack()
button_delet_task=tkinter.Button(root,text="Delete task",width=48,command=delete_task)
button_delet_task.pack()
root.mainloop()