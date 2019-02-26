login={"CSELECT01":["0001","Kamal Mehta"],"CSELECT02":["0002","Akanksha Choubey"],"CSELECT03":["0003","Abhishek Dewangan"],
       "CSELECT04":["0004","Rajesh Tiwari"],"CSELECT05":["0005","Krishna Kumar Pandey"],"CSELECT06":["0006","Manjula Swarnkar"],
       "CSELECT07":["0007","Yamini Chauhan"], "CSELECT08":["0008","Siddharth Choubey"], "CSELECT09":["0009","Samta Gajbhiye"],
       "CSELECT10": ["0010", "Yogesh Kumar Sahu"], "CSELECT11":["0011","Megha Mishra"], "CSELECT12":["0012","Vishnu Mishra"],
       "CSELECT13": ["0013", "Sampada Massey"], "CSELECT14":["0014","Prageet Vajpayee"]}

#LIBRARIES
import tkinter as tk
from tkinter import messagebox

def raise_frame(frame):
    frame.tkraise()

#WINDOW CONFIGURATIONS
window = tk.Tk()
window.title('SSTC Automatic Time-Table Generator')
window.geometry("1000x600+200+50")
window.configure(bg = '#002248')

#LOGIN PAGE SSTC LOGO
logo = tk.PhotoImage(file = "sstc.png")
default_image_label = tk.Label(window, image = logo)
default_image_label.pack(pady = 50)

#LOGIN PAGE HEADING
w = tk.Label(window, text="Shri Shankaracharya Technical Campus", font = ('Comic Sans MS', 25), bg = '#002248', fg = '#FFFFFF')
w.pack(anchor = "center")
v = tk.Label(window, text="Automatic Time-Table Generator", font = ('Comic Sans MS', 20), bg = '#002248', fg = '#FFFFFF')
v.pack(anchor = "center")

e1 = ""
e2 = ""
#LOGIN PAGE ENTRY
def getdata():
    global e1
    global e2
    e1 = user_.get()
    e2 = pass_.get()
    validation()
    


user_name = tk.Label(text = "Username: ", bg = '#002248', fg = '#FFFFFF')
user_name.pack(anchor = "center")
user_ = tk.Entry(window)
user_.pack(anchor = "center")
password = tk.Label(text = "Password: ", bg = '#002248', fg = '#FFFFFF')
password.pack(anchor = "center")
pass_ = tk.Entry(window, show = '*', width = 20)
pass_.pack(anchor = "center")
login_button = tk.Button(text = "Login")
login_button = tk.Button(window, text = "Login", command = getdata)
login_button.pack(pady = 10)

def validation():
    flag=0
    for key,value in login.items():
        if (e1 == key):
            if (e2 == value[0]):
                flag=1
                break
            else:
                flag=0
        else:
             flag=0
    if flag==0:
        messagebox.showerror("Unauthorized Accesss", "Incorrect User id or Password")
    else:
        def raise_frame(frame):
            frame.tkraise()

        root = tk.Tk()
        f1 = tk.Frame(window)
        f2 = tk.Frame(window)

        for frame in (f1, f2):
            frame.pack()
        
        root.mainloop()   
window.mainloop()
