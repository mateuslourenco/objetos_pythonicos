from tkinter import Label
from time import strftime

relogio = Label()
relogio.pack()

relogio['font'] = 'Helvetica 80 bold'
relogio['text'] = strftime('%H:%M:%S')


def tictac():
    relogio['text'] = strftime('%H:%M:%S')
    relogio.after(100, tictac)


tictac()
relogio.mainloop()
