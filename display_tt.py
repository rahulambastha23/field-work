from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1000x800")

timeTable_4A = [
    ['MON', 'DS', 'DS', 'CSA', 'OOPS', 'B', 'OS', 'CM', 'DMS'],
    ['TUE', 'CSA', 'OOPS', 'H/W LAB', 'H/W LAB', 'R', 'OS', 'DMS', 'CM'],
    ['WED', 'OOPS', 'OS', 'OOPS LAB', 'OOPS LAB', 'E', 'DS', 'DMS', 'CSA'],
    ['THU', 'OS', 'OOPS', 'DMS', 'DS', 'A', 'CM', 'DS LAB', 'DS LAB'],
    ['FRI', 'DMS', 'CSA', 'CM', 'DS', 'K', 'OOPS', 'GUI LAB', 'GUI LAB'],
]


frame = Frame(root)
frame.pack()

tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7,8,9), height = 5, show = "headings")
tree.pack(side = 'left')

tree.heading(1, text="Day")
tree.heading(2, text="Lecture 1")
tree.heading(3, text="Lecture 2")
tree.heading(4, text="Lecture 3")
tree.heading(5, text="Lecture 4")
tree.heading(6, text="")
tree.heading(7, text="Lecture 5")
tree.heading(8, text="Lecture 6")
tree.heading(9, text="Lecture 7")

tree.column(1, width = 100, anchor = "center")
tree.column(2, width = 100, anchor = "center")
tree.column(3, width = 100, anchor = "center")
tree.column(4, width = 100, anchor = "center")
tree.column(5, width = 100, anchor = "center")
tree.column(6, width = 100, anchor = "center")
tree.column(7, width = 100, anchor = "center")
tree.column(8, width = 100, anchor = "center")
tree.column(9, width = 100, anchor = "center")

for val in timeTable_4A:
    tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6], val[7], val[8]) )

root.mainloop()