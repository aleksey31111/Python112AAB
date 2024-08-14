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

# entry= Entry(win)
# entry.pack(fill='x')
button1= ttk.Button(win, text= "Print")  #, command=display_num)
# button1['bg'] = 'green'
# button1['activebackground'] = 'lime'
# button1['activeforeground'] = 'white'

# button1.pack(side= LEFT,expand=1,anchor='ne')
button1.place(x=50, y=50)
button2= ttk.Button(win, text= "Clear")  #, command= clear)

# button1['bg'] = 'red'
# button1['activebackground'] = 'pink'
# button1['activeforeground'] = 'white'
button2.pack(side=LEFT,expand=1,anchor='nw')

win.mainloop()