from tkinter import *
from tkinter.ttk import *
from tkhtmlview import HTMLLabel

root = Tk()

root.title("Хотите начать тест?")
root.geometry("600x300")

label = Label(text="Хотите начать тест?", font=50, background="yellow")
label.pack(pady=60)
# editor.place(x=100, y=100)

my_label = HTMLLabel(root, html="""
<ul>
    <li><a href='http://127.0.0.1:8000/1'>Подготовка бензиновой мотопомпы к работе</a></li>
    <li><a href='http://127.0.0.1:8000/2'>Промывка</a></li>
</ul>
""")
my_label.pack()
my_label.place(x=40, y=90)

# button = Button(root, text="Начать тест", font=40)
# button['bg'] = 'green'
# button['activebackground'] = 'lime'
# button['activeforeground'] = 'white'
# # button.pack(side=BOTTOM and RIGHT, padx=20, pady=20)
# # button.pack(side=BOTTOM, padx=20)
# # button.pack(ipadx=10, ipady=10)
# button.pack()  #side=BOTTOM, anchor="sw", padx=20, pady=20)
# button.place(x=20, y=250)

def click1():
    exit()


button1 = Button(root, text="Закрыть", font=40, command=click1)
button1['bg'] = 'red'
button1['activebackground'] = 'pink'
button1['activeforeground'] = 'white'
# button1.pack(side=BOTTOM, padx=60)
# button1.pack(anchor="se")
button1.pack()  #side=BOTTOM, anchor="se", padx=20, pady=10)
button1.place(x=500, y=250)
root.mainloop()
