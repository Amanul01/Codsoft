from tkinter import *
import random
import string

root=Tk()
root.title('MY APP')
root.geometry('400x400')
root.configure(bg='black')
root.resizable(0,0)


def click():
   password=" "
   a=int(pas_len.get())
   for i in range(0,4):
      password=password+random.choice(string.ascii_uppercase+string.ascii_lowercase)
   for i in range(a-4):
      password=password+random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)
   gen_pas.set(password)



head=Label(root,text='PASSWORD GENERATOR',font=('arial',20,'bold'),fg='white',bg='black')
head.pack(pady=(20,30))
head2=Label(root,text='THANK YOU ',font=('arial',20,'bold'),fg='white',bg='black')
head2.pack(side='bottom')


lab1=Label(root,text='ENTER THE LENGTH OF PASSWORD',font=('vardana',10,'bold'),height=1,bg='black',fg='white')
lab1.pack(pady=(0,15))
pas_len=IntVar()
inp=Spinbox(root,from_=6,to_=25,textvariable=pas_len,font=('arial',10))
inp.pack()


btn=Button(root,text='GENERATE',bg='white',width=10,fg='black',font=('arial',10,'bold'),command=click)
btn.pack(pady=(30,30))


gen_pas=StringVar()
gen=Entry(root,textvariable=gen_pas,fg='black',width=30,font=('arial',10))
gen.pack()

root.mainloop()


