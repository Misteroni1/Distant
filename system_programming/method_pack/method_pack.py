from tkinter import *

root = Tk()
f_top = Frame(root)
lab = Label(width=15)
e1 = Entry(text='Код цвета', width=20)
e1.insert(0, 'Код цвета')
lab['text'] = 'Цвет'

def insert():
    e1.delete(0, END)
    e1.insert(0, "#ff0000")
    lab['text'] = 'Красный'
def insert2():
    e1.delete(0, END)
    e1.insert(0, "#FFA500")
    lab['text'] = 'Оранжевый'
def insert3():
    e1.delete(0, END)
    e1.insert(0, "#FFFF00")
    lab['text'] = 'Жёлтый'
def insert4():
    e1.delete(0, END)
    e1.insert(0, "#00FF00")
    lab['text'] = 'Зелёный'
def insert5():
    e1.delete(0, END)
    e1.insert(0, "#00FFFF")
    lab['text'] = 'Голубой'
def insert6():
    e1.delete(0, END)
    e1.insert(0, "#0000FF")
    lab['text'] = 'Синий'
def insert7():
    e1.delete(0, END)
    e1.insert(0, "#800080")
    lab['text'] = 'Фиолетовый'


but = Button(bg='#ff0000', command=insert, width=4)
but2 = Button(bg='#FFA500', command=insert2, width=4)
but3 = Button(bg='#FFFF00', command=insert3, width=4)
but4 = Button(bg='#00FF00', command=insert4, width=4)
but5 = Button(bg='#00FFFF', command=insert5, width=4)
but6 = Button(bg='#0000FF', command=insert6, width=4)
but7 = Button(bg='#800080', command=insert7, width=4)
lab.pack(padx=2, pady=2)
e1.pack(padx=2, pady=2)
f_top.pack(padx=2, pady=2)
but.pack(side=LEFT, padx=2, pady=2)
but2.pack(side=LEFT, padx=2, pady=2)
but3.pack(side=LEFT, padx=2, pady=2)
but4.pack(side=LEFT, padx=2, pady=2)
but5.pack(side=LEFT, padx=2, pady=2)
but6.pack(side=LEFT, padx=2, pady=2)
but7.pack(side=LEFT, padx=2, pady=2)
root.mainloop()
