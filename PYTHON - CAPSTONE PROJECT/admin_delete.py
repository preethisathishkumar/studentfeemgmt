from tkinter import font
from tkinter.ttk import *
from tkinter import *
from tkinter.font import BOLD
from tkcalendar import DateEntry
import sqlite3
from tkinter import messagebox
      
root = Tk()
root.geometry("1300x500")
root.title("Delete Student Details")
global tree

NAME = StringVar()
ROLL = StringVar()
FEEID = StringVar()
CLASS = StringVar()
EMAIL = StringVar()
INS1 = StringVar()
INS2 = StringVar()
TOTAL = StringVar()
DUE = StringVar()

def total():
    res=int(INS1.get())+int(INS2.get())
    TOTAL.set(res)

def back():
    root.destroy()
    import main

def Database():
    global con, cursor,cur1,cur2
    con = sqlite3.connect('capstonedb.db')
    cursor = con.cursor()
    cur1 = con.cursor()
    cur2 = con.cursor()


def Register():
    #e1 = ROLL.get()
    Database()
    if  ROLL.get() == "":
        #l_result.config(text="Please complete the required field!", fg="red")
        messagebox.showerror("System","Please fill all the fields !!")
    else:
        r1 = messagebox.askquestion('System',"Do you want to delete the record", icon="warning")
        if r1 == 'yes':
            cur1.execute("delete from student where rollno = ?",(str(ROLL.get()),))
            con.commit()
            cur2.execute("delete from fees where feeid = ?",(str(FEEID.get()),))
            con.commit()
            ROLL.set("")
            FEEID.set("")
            messagebox.showinfo("System","Deleted!!")
    cursor.close()
    con.close()

def DisplayData():
    #open database
    Database()
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor.execute("SELECT * FROM student natural join fees")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    con.close()
'''
def get_cursor():
    cursor_tab = tree.focus()
    content = tree.item(cursor_tab)
    r = content['values']
    ROLL.set(str(roll))'''

L_Frame = Frame(root,width=600,relief=SOLID,padx=150)
L_Frame.pack(side=LEFT, fill=Y)

R_Frame = Frame(root,bg="blue",width=650)
R_Frame.pack(side=RIGHT,fill=Y)

l_tit = Label(L_Frame, text= "Delete Student Details", font=("Comic Sans MS", 20, BOLD))
l_tit.place(x=0,y=10)

l_rno = Label(L_Frame, text= "Roll No", font=("Comic Sans MS", 12, BOLD))
l_rno.place(x=0,y=110)
roll = Entry(L_Frame,font=("Comic Sans MS", 12),textvariable=ROLL)
roll.place(x=100,y=110)

l_fee = Label(L_Frame, text= "Fee Id", font=("Comic Sans MS", 12, BOLD))
l_fee.place(x=0,y=160)
roll = Entry(L_Frame,font=("Comic Sans MS", 12),textvariable=FEEID)
roll.place(x=100,y=160)

sub = Button(L_Frame, text="Delete", font=("Comic Sans MS", 14, BOLD), bg="light green", command=Register)
sub.place(x=0,y=210)

backb = Button(L_Frame,text="Back",font=("Comic Sans MS", 14, BOLD), bg="light blue",command=back)
backb.place(x=0,y=260)

scrollbarx = Scrollbar(R_Frame, orient=HORIZONTAL)
scrollbary = Scrollbar(R_Frame, orient=VERTICAL)
tree = Treeview(R_Frame,columns=("Rollno","Feeid", "Name", "Class", "Email","Installment_1","Installment_2","Total","Due_date"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
tree.heading('Rollno', text="Roll", anchor=W)
tree.heading('Feeid', text="Feeid", anchor=W)
tree.heading('Name', text="Name", anchor=W)
tree.heading('Class', text="Class", anchor=W)
tree.heading('Email', text="Email", anchor=W)

#tree.heading('Feeid', text="Feeid", anchor=W)
#tree.heading('ins1', text="ins1", anchor=W)
#tree.heading('Installment2', text="Installment2", anchor=W)
tree.heading('Total', text="Total", anchor=W)
tree.heading('Due_date', text="Date", anchor=W)
    #setting width of the columns
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=80, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=80)
tree.column('#7', stretch=NO, minwidth=0, width=80)
tree.column('#8', stretch=NO, minwidth=0, width=80)

tree.pack()
#tree.bind("<ButtonRelease-1>",get_cursor())
DisplayData()

root.mainloop()