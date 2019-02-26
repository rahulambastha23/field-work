from tkinter import *

master = Tk()

variable_class = StringVar(master)
variable_class.set("Class") # default value

w = OptionMenu(master, variable_class, "A", "B", "C")
w.pack()

variable_day = StringVar(master)
variable_day.set("Day")

v = OptionMenu(master, variable_day, "MON", "TUE", "WED", "THU", "FRI")
v.pack()

mainloop()