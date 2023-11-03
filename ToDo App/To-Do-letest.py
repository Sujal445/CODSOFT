from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
root = Tk()
root.title("TO-DO-LIST")
root.geometry("400x670")
root.resizable(False,False)

task_list= []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END , task) 
    else:
        messagebox.showwarning("Warning","Please enter a task",file=None, line=None)     

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist.txt','w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)        

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END ,task)
    except:
        file = open('tasklist.txt','w')
        file.close()            


# icon
icon = PhotoImage(file="todo.png")
root.iconphoto(False,icon)

# topbar
Top = Image.open("topbar.jpg",)
Top = Top.resize((400,70))
topbar = ImageTk.PhotoImage(Top)
l1=Label(root,image=topbar,fg="black",font="arial 20 bold")
l1.pack()

logo = Image.open("todoLogo.jpg")
logo = logo.resize((30,40))
todologo = ImageTk.PhotoImage(logo)
l2 = Label(l1,image=todologo)
l2.place(x=25,y=13)


todo = Label(root,text="TO-DO",font="italic 30 bold",bg="red")
todo.place(x=140,y=10)

heading = Label(root,text="ALL TASKS",font="arial 20 bold",fg="white",bg="purple",padx=40)
heading.place(x=80,y=80)

# main
frame= Frame(root,width=400,height=63,bg="white")
frame.place(x=0,y=130)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0,bg="yellow")
task_entry.place(x=10,y=15)

button= Button(frame,text="ADD",font="arial 20 bold",width=6,bg="blue",fg="white",bd=5,command=addTask)
button.place(x=280,y=0)
task_entry.focus()

# box
frame1 = Frame(root,bd=3,width=700,height=180,bg="gray")
frame1.pack(pady=(120,0))
listbox = Listbox(frame1,font=('arial',15),width=40,height=16,bg="black",fg="white",cursor="hand2")
listbox.pack(side=LEFT,fill=BOTH,padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side= RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


openTaskFile() # for save the task 


# delete
d = Image.open("delete.jpg")
d = d.resize((50,50))
delete = ImageTk.PhotoImage(d)
button1 = Button(root,image=delete,bd=5,font="arial 20 bold",fg="white",bg="red",command=deleteTask)
button1.pack(side=BOTTOM,pady=13)

root.mainloop()