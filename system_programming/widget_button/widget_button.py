from tkinter import *

root = Tk()
lab = Label(width=15)
e1 = Entry(text='Код цвета', width=15)
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


but = Button(bg='#ff0000', command=insert, width=13,)
but2 = Button(bg='#FFA500', command=insert2, width=13)
but3 = Button(bg='#FFFF00', command=insert3, width=13)
but4 = Button(bg='#00FF00', command=insert4, width=13)
but5 = Button(bg='#00FFFF', command=insert5, width=13)
but6 = Button(bg='#0000FF', command=insert6, width=13)
but7 = Button(bg='#800080', command=insert7, width=13)
lab.pack()
e1.pack()
but.pack()
but2.pack()
but3.pack()
but4.pack()
but5.pack()
but6.pack()
but7.pack()
root.mainloop()