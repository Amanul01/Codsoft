from tkinter import *

def show(num):
    a=result['text']
    result['text']=a+str(num)

def clear():
    result['text']=''

def delt():
    c=result['text']
    e=list(c)
    del e[-1]
    d="".join(e)
    result['text']=d


def final():
    b=result['text']
    result['text']=eval(b)

root=Tk()
root.geometry('280x322')
root.title('Calculator')
root.iconbitmap('F:\COURSES\PRACTICE\PYTHON PRACTICE\home.ico')
root.resizable(0,0)
root.configure(background='black')

result=Label(root,text=' ',bg='black',fg='white',font=('arial',30,'bold'))
result.grid(row=0,column=0,pady=(40,30),columnspan=5,sticky='w')

btnc=Button(root,text='C',bg='blue',fg='white',height=1,width=5,font=('verdana',14),command=lambda:clear())
btnc.grid(row=1,column=0)
btn7=Button(root,text='7',bg='grey',fg='white',height=1,width=5,font=('verdana',14),command=lambda:show(7))
btn7.grid(row=2,column=0)
btn4=Button(root,text='4',bg='grey',fg='white',height=1,width=5,font=('verdana',14),command=lambda:show(4))
btn4.grid(row=3,column=0)
btn1=Button(root,text='1',bg='grey',fg='white',height=1,width=5,font=('verdana',14),command=lambda:show(1))
btn1.grid(row=4,column=0)
btn0=Button(root,text='0',bg='grey',fg='white',height=1,width=5,font=('verdana',14),command=lambda:show(0))
btn0.grid(row=5,column=0)

btnd=Button(root,text='DEL',bg='blue',fg='white',height=1,width=5,font=('verdana',14),command=lambda:delt())
btnd.grid(row=1,column=1)
btn8=Button(root,text='8',bg='grey',fg='white',height=1,width=5,font=('verdana',14),command=lambda:show(8))
btn8.grid(row=2,column=1)
btn5=Button(root,text='5',bg='grey',fg='white',height=1,width=5,font=('verdana',14),command=lambda:show(5))
btn5.grid(row=3,column=1)
btn2=Button(root,text='2',bg='grey',fg='white',height=1,width=5,font=('verdana',14),command=lambda:show(2))
btn2.grid(row=4,column=1)
btndot=Button(root,text='.',bg='grey',fg='white',height=1,width=5,font=('verdana',14),command=lambda:show('.'))
btndot.grid(row=5,column=1)

btnmod=Button(root,text='%',bg='grey',fg='white',height=1,width=5,font=('verdana',14),command=lambda:show('%'))
btnmod.grid(row=1,column=3)
btn9=Button(root,text='9',bg='grey',fg='white',height=1,width=5,font=('verdana',14),command=lambda:show(9))
btn9.grid(row=2,column=3)
btn6=Button(root,text='6',bg='grey',fg='white',height=1,width=5,font=('verdana',14),command=lambda:show(6))
btn6.grid(row=3,column=3)
btn3=Button(root,text='3',bg='grey',fg='white',height=1,width=5,font=('verdana',14),command=lambda:show(3))
btn3.grid(row=4,column=3)
btneq=Button(root,text='=',bg='blue',fg='white',height=1,width=5,font=('verdana',14),command=lambda:final())
btneq.grid(row=5,column=3)

btnadd=Button(root,text='+',bg='yellow',fg='black',height=1,width=5,font=('verdana',14),command=lambda:show('+'))
btnadd.grid(row=1,column=4)
btnsub=Button(root,text='-',bg='yellow',fg='black',height=1,width=5,font=('verdana',14),command=lambda:show('-'))
btnsub.grid(row=2,column=4)
btnmul=Button(root,text='x',bg='yellow',fg='black',height=1,width=5,font=('verdana',14),command=lambda:show('*'))
btnmul.grid(row=3,column=4)
btndiv=Button(root,text='/',bg='yellow',fg='black',height=1,width=5,font=('verdana',14),command=lambda:show('/'))
btndiv.grid(row=4,column=4)
btnfl=Button(root,text='//',bg='yellow',fg='black',height=1,width=5,font=('verdana',14),command=lambda:show('//'))
btnfl.grid(row=5,column=4)

root.mainloop()