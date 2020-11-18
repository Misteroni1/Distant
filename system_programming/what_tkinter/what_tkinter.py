from tkinter import *
from tkinter import messagebox

global a, b

def func():
    try:
        global a, b
        a = ent.get()
        a = int(a)
        b = ent1.get()
        b = int(b)
    except ValueError:
        messagebox.showerror("ОШИБКА", "Введите корректные значения")

def summ(event):
    func()
    s = a+b
    s = str(s)
    lab['text'] = ' '.join(s)

def minus(event):
    func()
    s = a-b
    s = str(s)
    lab['text'] = ' '.join(s)

def mult(event):
    func()
    s = a*b
    s = str(s)
    lab['text'] = ' '.join(s)

def div(event):
    func()
    s = a/b
    s = str(s)
    lab['text'] = ' '.join(s)

root = Tk()

ent = Entry(width=15)
ent1 = Entry(width=15)
but = Button(text="+", width=15)
but2 = Button(text="-", width=15)
but3 = Button(text="*", width=15)
but4 = Button(text="/", width=15)
lab = Label(width=20, bg='black', fg='white')


but.bind('<Button-1>', summ)
but2.bind('<Button-1>', minus)
but3.bind('<Button-1>', mult)
but4.bind('<Button-1>', div)

ent.pack()
ent1.pack()
but.pack()
but2.pack()
but3.pack()
but4.pack()
lab.pack()
root.mainloop()

