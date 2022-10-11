from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter.ttk import Combobox
import time

shifr_message1 = []
shifr_message = []
messege1 = []
messege = []

def _shifr (text_for_shifr):

    for i in text_for_shifr:
        messege.append(i)

    for shifr in messege:
        if ord(shifr) < 119:
            shifr_message.append(chr(ord(shifr) + 3))
        else:
            shifr_message.append(chr(ord(shifr) - 23))

    b = "".join(shifr_message)
    messege.clear()
    shifr_message.clear()

    lbl1.configure(text = b)

def _reshifr (shifr):
    for i in shifr:
        messege1.append(i)
        print(messege1)

    for i in messege1:
        if ord(i) < 100:
            shifr_message1.append(chr(ord(i) + 23))
            print(shifr_message1)
            print(messege1)
        else:
            shifr_message1.append(chr(ord(i) - 3))

    b = "".join(shifr_message1)


    lbl1.configure(text=b)
    messege1.clear()
    shifr_message1.clear()




def clicked():
    btn.configure(text=combo.get())
    if combo.get() == 'Зашифровать':
        btn.configure(text='Зашифровать')

        lbl.configure(text= 'Идет зашифровка...')
        res = txt.get()
        print(res)
        _shifr(res)

    else:
        btn.configure(text='Расшифровать')
        lbl.configure(text='Идет Дешифровка...')

        res1 = txt.get()
        print(res1)
        _reshifr(res1)




window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
selected = IntVar()

combo = Combobox(window)
combo['values'] = ("Зашифровать","Расшифровать")
combo.current(1)  # установите вариант по умолчанию
combo.grid(column=0, row=0)
btn = Button(window, text="Клик", command=clicked)

lbl = Label(window, text="")
lbl1 = Label(window, text="")

lbl.grid(column=1, row=2)
lbl1.grid(column=1, row=3)

txt = Entry(window, width=25)
txt.grid(column=1, row=0)
btn = Button(window, text="ок", command=clicked)
btn.grid(column=2, row=0)


window.mainloop()

shifr_message = []
messege = []
a = 'zyx'
def _shifr (a):

    for i in a:
        messege.append(i)

    for shifr in messege:
        if ord(shifr) <= 121:
            shifr_message.append(chr(ord(shifr) + 1))
        else:
            shifr_message.append(chr(ord(shifr) - 25))

b = "".join(shifr_message)
print(messege)
print(shifr_message)
print(b)