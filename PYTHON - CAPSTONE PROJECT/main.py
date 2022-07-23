from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox

def Admin():
    root.destroy()
    import admin_login

def Student():
    root.destroy()
    import student_search

def Exit():
    r1 = messagebox.askquestion('System',"Do you want to exit ?", icon="warning")
    if r1 == 'yes':
        root.destroy()

root = Tk()
root.geometry("700x400")
root.title("Student Fee Management System")

T_Frame = Frame(root, height=300, width= 640, bd = 3, relief=SOLID)
T_Frame.pack(side= TOP)

R_Frame = Frame(root)
R_Frame.pack(side= TOP,pady=5)

l_title = Label(T_Frame, text="Student Fee Management System", font=("Comic Sans MS", 18, BOLD),bd=1)
l_title.pack()

l_subtitle = Label(T_Frame, text="Choose Login", font=("Comic Sans MS", 18, BOLD),bd=2)
l_subtitle.pack()

sub = Button(R_Frame, text="Admin", font=("Comic Sans MS", 14, BOLD), bg="light green", command=Admin)
sub.grid(row = 11,column=0,pady=7)

stu = Button(R_Frame, text="Student", font=("Comic Sans MS", 14, BOLD), bg="powder blue", command=Student)
stu.grid(row = 13,column=0,pady=7)

exit = Button(R_Frame, text="Exit", font=("Comic Sans MS", 14, BOLD), bg="Red", fg="white",command=Exit)
exit.grid(row = 15,column=0,pady=7)

root.mainloop()