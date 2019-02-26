
from tkinter import *
def raise_frame(frame):
    frame.tkraise()

window = Tk()

login = Frame(window)
f2 = Frame(window)
f3 = Frame(window)
f4 = Frame(window)

for frame in (login, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

Button(login, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
Label(login, text='FRAME 1').pack()

Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to frame 1', command=lambda:raise_frame(login)).pack()

raise_frame(login)
window.mainloop()