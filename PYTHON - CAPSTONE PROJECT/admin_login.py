from tkinter.ttk import *
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox

def Login():
    if NAME.get() == 'Admin' and PASS.get() == 'admin@123':
        root.destroy()
        import admin_permissions
    
    else:
        messagebox.showerror("SFM","Incorrect Login Credentials!!!")

def back():
    root.destroy()
    import main

root = Tk()
root.geometry("700x400")
root.title("Admin Login")

NAME = StringVar()
PASS = StringVar()

T_Frame = Frame(root, height=100, width= 640, bd = 1, relief=SOLID)
T_Frame.pack(side= TOP)

R_Frame = Frame(root)
R_Frame.pack(side= TOP,pady=5)

l_title = Label(T_Frame, text="Admin Login", font=("Comic Sans MS", 18, BOLD),bd=2)
l_title.pack()
l_name = Label(R_Frame, text= "UserName  ", font=("Comic Sans MS", 18, BOLD))
l_name.grid(row=5,pady=50)
name = Entry(R_Frame,font=("Comic Sans MS", 14),textvariable=NAME)
name.grid(row=5, column=1,pady=50)

l_name = Label(R_Frame, text= "Password  ", font=("Comic Sans MS", 18, BOLD))
l_name.grid(row=7)
name = Entry(R_Frame,font=("Comic Sans MS", 14),show="*",textvariable=PASS)
name.grid(row=7, column=1)
sub = Button(R_Frame, text="Login", font=("Comic Sans MS", 14, BOLD), bg="light green", command=Login)
sub.grid(row = 8,padx=(20,0),pady=(55,55),columnspan=2)
backb = Button(R_Frame, text="Back", font=("Comic Sans MS", 14, BOLD), bg="dodgerblue",fg = "white",command=back)
backb.grid(row =8)
root.mainloop()