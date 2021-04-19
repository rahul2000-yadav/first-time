from tkinter import *
import tkinter as tk
from tkinter import messagebox
task_list=[]
counter=1
def inputError():
    if enterTaskField.get()=="":
        messagebox.showerror("Input Error")
        return 0
    return 1
def clear_taskNumberField():
    taskNumberField.delete(0,0,END)
def clear_taskField():
    enterTaskField.delete(0,END)
def insertTask():
    global counter
    value=inputError()
    if value==0:
        return
    content=enterTaskField.get()+"\n"
    task_list.append(content)
    TextArea.insert('end -1 chars',"["+str(counter)+"]"+content)
    counter+=1
    clear_taskField()
def delete():
    global counter
    if len(task_list)==0:
        messagebox.showerror("No tasks")
        return
    number=clear_taskNumberField(1.0,End)
    if number=="\n":
        messagebox.showerror("input error")
        return
    else:
        task_no=int(number)
        clear_taskNumberField()
        task_list.pop(task_no-1)
        counter-=1
        TextArea.delete(1.0,END)
    for i in range(len(task_list)):
        TextArea.insert('end -1 chars',"["+str(i+1)+"]"+task_list[i])
if __name__=="__main__":
    gui=tk.Tk()
    gui.configure(background="grey")
    gui.title("ToDo App")
    gui.geometry("250x300")
    enterTask=Label(gui,text="Enter task",bg="red")
    enterTaskField=Entry(gui)
    Submit=Button(gui,text="submit",fg="pink",bg="Red",command=insertTask)
    TextArea=Text(gui,height=5,width=25,font="lucida 13")
    TaskNumber=Label(gui,text="Delete Task number",bg="blue")
    TaskNumberField=Text(gui,height=1,width=2,font="lucida 13")
    delete=Button(gui,text="Delete",fg="black")
    Exit=Button(gui,text="Exit",fg="black",bg="red",command=exit)
    enterTask.grid(row=0,column=2)
    enterTaskField.grid(row=1,column=2,ipadx=50)
    Submit.grid(row=2,column=2)
    TextArea.grid(row=3,column=2,padx=10,sticky=W)
    TaskNumber.grid(row=4,column=2,ipadx=5)
    TaskNumberField.grid(row=5,column=2)
    delete.grid(row=6,column=2,ipadx=5)
    Exit.grid(row=7,column=2)
    gui.mainloop()




