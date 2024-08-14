from tkinter import *
from tkinter import ttk
import random


win = Tk()
win.geometry("750x250")

# def clear():
#    entry.delete(0,END)
# def display_num():
#    for i in range(1):
#       entry.insert(0, random.randint(5,20))
#
# entry= Entry(win, width= 40)
# entry.pack()
buttons = ttk.Frame(win)
# buttons.pack(pady = 5)
button1= ttk.Button(buttons, text="Начать тест")  #, command=display_num)
# button1['bg'] = 'green'
# button1['activebackground'] = 'lime'
# button1['activeforeground'] = 'white'

button1.pack(side = LEFT)
# button1.place(x=1, y=1)

button2=ttk.Button(buttons, text="Закрыть")  #, command= clear)
button2.pack()

win.mainloop()