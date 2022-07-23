from tkinter import font
from tkinter.ttk import *
from tkinter import *
from tkinter.font import BOLD
from tkcalendar import DateEntry
import sqlite3
from tkinter import messagebox

root = Tk()
root.geometry("1200x1000")
root.title("Search Student Details")

ROLL = StringVar()
FEEID = StringVar()
DET = StringVar()
FEE = StringVar()
FIN = StringVar()


def Database():
    global con, cursor,cur1,cur2,cur3
    con = sqlite3.connect('capstonedb.db')
    cursor = con.cursor()
    cur1 = con.cursor()
    cur2 = con.cursor()
    cur3 = con.cursor()

def Search():
    #e1 = ROLL.get()
    Database()
    if  ROLL.get() == "":
        #l_result.config(text="Please complete the required field!", fg="red")
        messagebox.showerror("System","Please fill all the fields !!")
    else:
            cur1.execute("select * from student where rollno like ?",(str(ROLL.get()),))
            student = cur1.fetchone()
            DET.set(student)
            
            con.commit()
            cur2.execute("select ins1, ins2,total,duedate from fees where feeid like ?",(str(FEEID.get()),))
            student = cur2.fetchone()
            FEE.set(student)
            con.commit()

            cur3.execute("select * from student natural join fees where rollno like ?",(str(ROLL.get()),))
            student = cur3.fetchone()
            FIN.set(student)
            con.commit()
            ROLL.set("")
            FEEID.set("")
    cursor.close()
    con.close()

def back():
    root.destroy()
    import main

L_Frame = Frame(root,width=1000,relief=SOLID,padx=150)
L_Frame.pack(side=LEFT, fill=Y)

l_tit = Label(L_Frame, text= "Search Student Details", font=("Comic Sans MS", 20, BOLD))
l_tit.place(x=0,y=10)

l_rno = Label(L_Frame, text= "Roll No", font=("Comic Sans MS", 12, BOLD))
l_rno.place(x=0,y=110)
roll = Entry(L_Frame,font=("Comic Sans MS", 12),textvariable=ROLL)
roll.place(x=100,y=110)

l_fee = Label(L_Frame, text= "Fee Id", font=("Comic Sans MS", 12, BOLD))
l_fee.place(x=0,y=160)
roll = Entry(L_Frame,font=("Comic Sans MS", 12),textvariable=FEEID)
roll.place(x=100,y=160)

l1 = Label(L_Frame,text = "Student Details",font=("Comic Sans MS", 12, BOLD))
l1.place(x=0,y=210)
l1 = Label(L_Frame,text = "Roll  Feeid  Name  Class  Email",font=("Comic Sans MS", 12, BOLD))
l1.place(x=0,y=240)
T = Label(L_Frame,font=("Comic Sans MS", 12, BOLD),textvariable=DET)
T.place(x=0,y=270)

l2 = Label(L_Frame,text = "Student's Fee Details",font=("Comic Sans MS", 12, BOLD))
l2.place(x=0,y=310)
l2 = Label(L_Frame,text = "Ins1  Ins2  Total  Duedate",font=("Comic Sans MS", 12, BOLD))
l2.place(x=0,y=340)
T2 = Label(L_Frame,font=("Comic Sans MS", 12, BOLD),textvariable=FEE)
T2.place(x=0,y=370)

l3 = Label(L_Frame,text = "Student's Fee Details",font=("Comic Sans MS", 12, BOLD))
l3.place(x=0,y=410)
l3 = Label(L_Frame,text = "Roll  Feeid  Name  Class  Email             Ins1   Ins2   Total   Duedate",font=("Comic Sans MS", 12, BOLD))
l3.place(x=0,y=450)
T3 = Label(L_Frame,font=("Comic Sans MS", 12, BOLD),textvariable=FIN)
T3.place(x=0,y=490)

sub = Button(L_Frame, text="Search", font=("Comic Sans MS", 14, BOLD), bg="light green",command=Search)
sub.place(x=0,y=520)

backb = Button(L_Frame, text="Back", font=("Comic Sans MS", 14, BOLD), bg="dodgerblue",fg = "white",command=back)
backb.place(x=0,y=570)


root.mainloop()