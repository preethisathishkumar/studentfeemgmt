from tkinter.ttk import *
from tkinter import *
from tkinter.font import BOLD
from tkcalendar import Calendar
import mysql.connector
from tkinter import messagebox
      
root = Tk()
root.geometry("1300x1300")
root.title("Insert Student Details")
global tree

NAME = StringVar()
ROLL = StringVar()
FEEID = StringVar()
CLASS = StringVar()
PHONE = StringVar()
EMAIL = StringVar()
TUTION = StringVar()
BUS = StringVar()
HOSTEL = StringVar()
TOTAL = StringVar()
DUE = StringVar()

def grab_date():
    l.config(text = due.get_date())

def Database():
    global con, cursor
    con = mysql.connector.connect(host='localhost', database= 'capstone', user='root', password="",port = 3306)
    cursor = con.cursor()

def Register():
    Database()
    if NAME.get() == "" or ROLL.get() == "" or EMAIL.get() == "":
        #l_result.config(text="Please complete the required field!", fg="red")
        messagebox.showerror("System","Please fill all the fields !!")
    else:
        cursor.execute("insert into students (Rollno,Feeid,Name,Class,Email,Phone) values (%s, %s, %s, %s, %s, %s)", (str(ROLL.get()), str(FEEID.get()),str(NAME.get()),str(CLASS.get()), str(EMAIL.get()),str(PHONE.get())))
        con.commit()
        cursor.execute("insert into fee (Feeid,Tutionfee,busfee,hostelfee,Total,Due_date) values (%s, %s, %s, %s, %s, %s)", (str(FEEID.get()), str(TUTION.get()),str(BUS.get()),str(HOSTEL.get()), str(TOTAL.get()),str(DUE.get())))
        con.commit()
        NAME.set("")
        EMAIL.set("")
        
        #l_result.config(text="Successfully Registered", fg="Green")
        messagebox.showinfo("System","Successfully Registered")
    cursor.close()
    con.close()

def DisplayData():
    #open database
    Database()
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor.execute("SELECT * FROM students")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    con.close()


L_Frame = Frame(root,width=600,relief=SOLID,padx=150)
L_Frame.pack(side=LEFT, fill=Y)

#canvas = Canvas(L_Frame)
#canvas.pack(side=LEFT,fill=BOTH,expand=True)

R_Frame = Frame(root,bg="blue",width=650)
R_Frame.pack(side=RIGHT,fill=Y)

#scrollbar = Scrollbar(L_Frame, orient=VERTICAL,command=canvas.yview)
#scrollbar.pack(side=RIGHT,fill=Y)

#canvas.configure(yscrollcommand = scrollbar.set(1,1))
#S_Frame = Frame(canvas)
#canvas.create_window((0,0),window = S_Frame,anchor = "nw")


#scrollbar.config(command=canvas.yview)
#L_Frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))


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

l_pno = Label(L_Frame, text= "Phone No.", font=("Comic Sans MS", 12, BOLD))
l_pno.place(x=0,y=310)
pno = Entry(L_Frame,font=("Comic Sans MS", 12),textvariable=PHONE)
pno.place(x=100,y=310)

l1 = Label(L_Frame, text= "Fee Details", font=("Comic Sans MS", 12, BOLD))
l1.place(x=0,y=350)

l_tut = Label(L_Frame, text= "Tutuion fee", font=("Comic Sans MS", 12, BOLD))
l_pno.place(x=0,y=400)
tut = Entry(L_Frame,font=("Comic Sans MS", 12),textvariable=TUTION)
tut.place(x=100,y=400)

l_bus = Label(L_Frame, text= "Bus fee", font=("Comic Sans MS", 12, BOLD))
l_bus.place(x=0,y=450)
bus = Entry(L_Frame,font=("Comic Sans MS", 12),textvariable=BUS)
bus.place(x=100,y=450)

l_hos = Label(L_Frame, text= "Hostel Fee", font=("Comic Sans MS", 12, BOLD))
l_hos.place(x=0,y=500)
hos = Entry(L_Frame,font=("Comic Sans MS", 12),textvariable=HOSTEL)
hos.place(x=100,y=500)

l_pno = Label(L_Frame, text= "Total", font=("Comic Sans MS", 12, BOLD))
l_pno.place(x=0,y=550)
pno = Entry(L_Frame,font=("Comic Sans MS", 12),textvariable=TOTAL)
pno.place(x=100,y=550)


l_due = Label(L_Frame, text= "Due date", font=("Comic Sans MS", 12, BOLD))
l_due.place(x=0,y=600)
due = Calendar(L_Frame, year= 2021, month = 3, day = 3, date_pattern = 'yyyy/mm/dd', textvariable= DUE)
due.place(x= 100, y= 600)
b = Button(L_Frame, text="Select the date", font=("Comic Sans MS", 12, BOLD),command=grab_date)
b.place(x= 100,y=700)
l = Label(R_Frame, font=("Comic Sans MS", 14))
l.place(x=200,y=740)

sub = Button(L_Frame, text="Register", font=("Comic Sans MS", 14, BOLD), bg="blue", command=Register)
sub.place(x=0,y=800)



scrollbarx = Scrollbar(R_Frame, orient=HORIZONTAL)
scrollbary = Scrollbar(R_Frame, orient=VERTICAL)
tree = Treeview(R_Frame,columns=("Rollno","Feeid", "Name", "Class", "Email","Phone","Feeid","Tutionfee","busfee","hostelfee","Total","Due_date"),
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
tree.heading('Phone', text="Phone", anchor=W)
tree.heading('Feeid', text="Feeid", anchor=W)
tree.heading('Tutionfee', text="Tution", anchor=W)
tree.heading('busfee', text="Bus", anchor=W)
tree.heading('hostelfee', text="Hostel", anchor=W)
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
tree.column('#9', stretch=NO, minwidth=0, width=80)
tree.column('#10', stretch=NO, minwidth=0, width=80)
tree.column('#11', stretch=NO, minwidth=0, width=80)
tree.column('#12', stretch=NO, minwidth=0, width=80)

tree.pack()
DisplayData()
root.mainloop()