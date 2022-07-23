from tkinter import font
from tkinter.ttk import *
from tkinter import *
from tkinter.font import BOLD
from tkcalendar import DateEntry
import sqlite3
from tkinter import messagebox
      
root = Tk()
root.geometry("1300x1300")
root.title("Insert or Update Student Details")
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
    import admin_permissions

def Database():
    global con, cursor,cur1,cur2
    con = sqlite3.connect('capstonedb.db')
    cursor = con.cursor()
    cur1 = con.cursor()
    cur2 = con.cursor()


def Register():
    Database()
    if NAME.get() == "" or ROLL.get() == "" or EMAIL.get() == "":
        #l_result.config(text="Please complete the required field!", fg="red")
        messagebox.showerror("System","Please fill all the fields !!")
    else:
        cur1.execute("insert into student (rollno,feeid,name,class,email) values (?,?,?,?,?)", (str(ROLL.get()), str(FEEID.get()),str(NAME.get()),str(CLASS.get()), str(EMAIL.get())))
        con.commit()
        cur2.execute("insert into fees (feeid,ins1,ins2,total,duedate) values (?,?,?,?,?)", (str(FEEID.get()),str(INS1.get()),str(INS2.get()),str(TOTAL.get()),str(DUE.get())))
        con.commit()
        NAME.set("")
        EMAIL.set("")
        ROLL.set("")
        FEEID.set("")
        INS1.set("")
        INS2.set("")
        TOTAL.set("")
        CLASS.set("")
        
        #l_result.config(text="Successfully Registered", fg="Green")
        messagebox.showinfo("System","Successfully Registered")
    cursor.close()
    con.close()

def Update():
    Database()
    if NAME.get() == "" or ROLL.get() == "" or EMAIL.get() == "":
        #l_result.config(text="Please complete the required field!", fg="red")
        messagebox.showerror("System","Please fill all the fields !!")
    else:
        r1 = messagebox.askquestion('System',"Do you want to update the record", icon="warning")
        if r1 == 'yes':
            cur1.execute(" update student set rollno = ?,feeid= ?,name=?, class=?,email=? where rollno = ?", (str(ROLL.get()), str(FEEID.get()),str(NAME.get()),str(CLASS.get()), str(EMAIL.get()),(str(ROLL.get()))))
            con.commit()
            cur2.execute("update fees set feeid = ?,ins1=?,ins2=?,total=?,duedate=? where feeid = ?", (str(FEEID.get()),str(INS1.get()),str(INS2.get()),str(TOTAL.get()),str(DUE.get()),(str(FEEID.get()))))
            con.commit()
            NAME.set("")
            EMAIL.set("")
            ROLL.set("")
            FEEID.set("")
            INS1.set("")
            INS2.set("")
            TOTAL.set("")
            CLASS.set("")
        
        #l_result.config(text="Successfully Registered", fg="Green")
        messagebox.showinfo("System","Successfully Updated")
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

L_Frame = Frame(root,width=600,relief=SOLID,padx=150)
L_Frame.pack(side=LEFT, fill=Y)

R_Frame = Frame(root,bg="blue",width=650)
R_Frame.pack(side=RIGHT,fill=Y)

l_tit = Label(L_Frame, text= "Insert or Update Student Details", font=("Comic Sans MS", 20, BOLD))
l_tit.place(x=0,y=10)

l_name = Label(L_Frame, text= "Name", font=("Comic Sans MS", 12, BOLD))
l_name.place(x=0,y=60)
name = Entry(L_Frame,font=("Comic Sans MS", 12),textvariable=NAME)
name.place(x=100,y=60)

l_rno = Label(L_Frame, text= "Roll No", font=("Comic Sans MS", 12, BOLD))
l_rno.place(x=0,y=110)
roll = Entry(L_Frame,font=("Comic Sans MS", 12),textvariable=ROLL)
roll.place(x=100,y=110)

l_fee = Label(L_Frame, text= "Fee Id", font=("Comic Sans MS", 12, BOLD))
l_fee.place(x=0,y=160)
roll = Entry(L_Frame,font=("Comic Sans MS", 12),textvariable=FEEID)
roll.place(x=100,y=160)

l_class = Label(L_Frame, text="Class  ", font=("Comic Sans MS", 12, BOLD))
l_class.place(x=0,y=210)
gen= Combobox(L_Frame, values =("CSE-A", "CSE-B", "CSE-C"), font=("Comic Sans MS", 12, BOLD),textvariable=CLASS).place(x=100,y=210)

l_email = Label(L_Frame, text= "Email", font=("Comic Sans MS", 12, BOLD))
l_email.place(x=0,y=260)
email = Entry(L_Frame,font=("Comic Sans MS", 12),textvariable=EMAIL)
email.place(x=100,y=260)

l_ins1 = Label(L_Frame,text="Installment1",font=("Comic Sans MS", 12, BOLD))
l_ins1.place(x=0,y=310)
ins1 = Entry(L_Frame,font=("Comic Sans MS",12),textvariable=INS1)
ins1.place(x=100,y=310)

l_ins2 = Label(L_Frame,text="Installment2",font=("Comic Sans MS", 12, BOLD))
l_ins2.place(x=0,y=360)
ins2 = Entry(L_Frame,font=("Comic Sans MS",12),textvariable=INS2)
ins2.place(x=100,y=360)

l_due = Label(L_Frame, text= "Due date", font=("Comic Sans MS", 12, BOLD))
l_due.place(x=0,y=410)
due = DateEntry(L_Frame, year= 2021, month = 3, day = 3, date_pattern = 'yyyy/mm/dd', textvariable= DUE)
due.place(x= 100, y= 410)

l_tot = Label(L_Frame, text= "Total", font=("Comic Sans MS", 12, BOLD))
l_tot.place(x=0,y=460)
total1 = Entry(L_Frame,font=("Comic Sans MS",12),textvariable=TOTAL)
total1.place(x= 100, y= 460)
total1 = Button(L_Frame,text="Total",font=("Comic Sans MS", 12, BOLD),command=total)
total1.place(x=330,y=460)

sub = Button(L_Frame, text="Register", font=("Comic Sans MS", 14, BOLD), bg="light green", command=Register)
sub.place(x=0,y=510)

sub = Button(L_Frame, text="Update", font=("Comic Sans MS", 14, BOLD), bg="light green", command=Update)
sub.place(x=100,y=510)

backb = Button(L_Frame,text="Back",font=("Comic Sans MS", 14, BOLD), bg="light blue",command=back)
backb.place(x=0,y=560)

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
'''
tree.heading('Phone', text="Phone", anchor=W)
tree.heading('Feeid', text="Feeid", anchor=W)
tree.heading('Tutionfee', text="Tution", anchor=W)
tree.heading('busfee', text="Bus", anchor=W)
tree.heading('hostelfee', text="Hostel", anchor=W)'''

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
DisplayData()

root.mainloop()