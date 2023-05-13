from tkinter import *
from tkinter.ttk import Combobox

window=Tk()
window.title('asv')
window.geometry('700x500')
combo=Combobox(window)


result=Label(window,text='',font=('Kegel',50))
def f():
    if '+' in ent1.get():
        result.configure(text=int(ent1.get()[0])+int(ent1.get()[2]))
    if '-' in ent1.get():
        result.configure(text=int(ent1.get()[0])-int(ent1.get()[2]))
    if '*' in ent1.get():
        result.configure(text=int(ent1.get()[0])*int(ent1.get()[2]))
    if '/' in ent1.get():
        result.configure(text=int(ent1.get()[0])/int(ent1.get()[2]))
def h1():
    ent1.insert(END,1)
def h2():
    ent1.insert(END,2)
def h3():
    ent1.insert(END,3)
def h4():
    ent1.insert(END,4)
def h5():
    ent1.insert(END,5)
def h6():
    ent1.insert(END,6)
def h7():
    ent1.insert(END,7)
def h8():
    ent1.insert(END,8)
def h9():
    ent1.insert(END,9)
def h10():
    ent1.insert(END,'+')
def h11():
    ent1.insert(END,'-')
def h12():
    ent1.insert(END,'*')
def h13():
    ent1.insert(END,'/')
def h14():
    ent1.delete(ent1.index('end')-1)
def h15():
    ent1.delete(0,END)
combo['values']=('plus','minus','mult','division')


ent1=Entry(window,width='10')
ent1.focus()


btn=Button(window,bg='white',text='Ecuals',width='5',height='2',command=f)
btn1=Button(window,text='1',bg='Green',width='5',height='2',command=h1)
btn2=Button(window,text='2',bg='Green',width='5',height='2',command=h2)
btn3=Button(window,text='3',bg='Green',width='5',height='2',command=h3)
btn4=Button(window,text='4',bg='Green',width='5',height='2',command=h4)
btn5=Button(window,text='5',bg='Green',width='5',height='2',command=h5)
btn6=Button(window,text='6',bg='Green',width='5',height='2',command=h6)
btn7=Button(window,text='7',bg='Green',width='5',height='2',command=h7)
btn8=Button(window,text='8',bg='Green',width='5',height='2',command=h8)
btn9=Button(window,text='9',bg='Green',width='5',height='2',command=h9)
btnq=Button(window,text='+',bg='Green',width='5',height='2',command=h10)
btnw=Button(window,text='-',bg='Green',width='5',height='2',command=h11)
btne=Button(window,text='*',bg='Green',width='5',height='2',command=h12)
btnr=Button(window,text='/',bg='Green',width='5',height='2',command=h13)
btn_del=Button(window,text='delete',bg='Aqua',width='5',height='2',command=h14)
btn_cl=Button(window,text='clear',bg='Red',width='5',height='2',command=h15)

btn1.grid(column=0,row=5)
btn2.grid(column=1,row=5)
btn3.grid(column=2,row=5)
btn4.grid(column=3,row=5)
btn5.grid(column=4,row=5)
btn6.grid(column=3,row=6)
btn7.grid(column=0,row=6)
btn8.grid(column=1,row=6)
btn9.grid(column=2,row=6)
btnq.grid(column=0,row=7)
btnw.grid(column=1,row=7)
btne.grid(column=2,row=7)
btnr.grid(column=3,row=7)
btn.grid(column=4,row=6)
btn_del.grid(column=0,row=8)
btn_cl.grid(column=1,row=8)
result.grid(column=5,row=6)
ent1.grid(column=5,row=7)
window.mainloop()
