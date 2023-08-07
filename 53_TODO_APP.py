from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry('400x400')
root.resizable(0,0)
root.configure(bg='cyan')
root.title('TODO APP')



def add():
    task=user.get()
    if task!='':
        lst.insert('end',task)
        user.delete(0,'end')
    else:
        messagebox.showerror('ERROR','NOTHING TO ADD')

def delt():
    try:
        task=lst.curselection()
        lst.delete(task)
    except:
        messagebox.showerror('ERROR','NO TASK IS SLECTED')

def edit():
    try:
        task_select=lst.curselection()
        task_value=lst.get(task_select)
        user.insert('end',task_value)
        lst.delete(task_select)
    except:
        messagebox.showerror('ERROR','NO TASK IS SELECTED')



heading=Label(root,text='TO-DO APPLICATION',fg='black',bg='cyan',font=('verdana',18,'bold'))
heading.pack(pady=(20,30))

sub=Label(root,text='EVENT',fg='black',bg='cyan',font=('arial',14,'bold'))
sub.place(x=85,y=120)

user=Entry(root,width=23,bg='white',fg='black',font=('arial',12,'bold'))
user.place(x=10,y=160)

badd=Button(root,text='ADD',bg='grey',fg='black',width=10,command=add)
badd.place(x=70,y=210)

bdel=Button(root,text='DELETE',bg='grey',fg='black',width=10,command=delt)
bdel.place(x=70,y=260)

bmod=Button(root,text='MODIFY',bg='grey',fg='black',width=10,command=edit)
bmod.place(x=70,y=310)


f=Frame(root)
f.pack(side=RIGHT)

lst=Listbox(f,height=13,width=26,bg='white')
lst.pack(side='left')

scroll=Scrollbar(f)
scroll.pack(side='right',fill=Y)

lst.config(yscrollcommand=scroll.set)
scroll.config(command=lst.yview)


root.mainloop()