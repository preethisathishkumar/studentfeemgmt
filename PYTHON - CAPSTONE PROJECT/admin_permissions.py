from tkinter.ttk import *
from tkinter import *
from tkinter.font import BOLD

root = Tk()
root.geometry("600x400")
root.title("Admin Permissions")

def add():
    root.destroy()
    import admin_insert

def update():
    root.destroy()
    import admin_update

def delete():
    root.destroy()
    import admin_delete

def back():
    root.destroy()
    import main
    

L_Frame = Frame(root,width=600,relief=SOLID,padx=150)
L_Frame.pack(side=LEFT, fill=Y)

l_tit = Label(L_Frame, text= "Choose a Operation", font=("Comic Sans MS", 20, BOLD))
l_tit.place(x=0,y=10)

add = Button(L_Frame, text="Add or Update Student", font=("Comic Sans MS", 14, BOLD), bg="light green",command=add)
add.place(x=0,y=120)

#update = Button(L_Frame, text="Update Student", font=("Comic Sans MS", 14, BOLD), bg="light pink",command=update)
#update.place(x=150,y=120)

delete = Button(L_Frame, text="Delete Student", font=("Comic Sans MS", 14, BOLD), bg="light pink",command=delete)
delete.place(x=60,y=180)

backb = Button(L_Frame, text="Back", font=("Comic Sans MS", 14, BOLD), bg="dodgerblue",fg = "white",command=back)
backb.place(x=100,y=290)

root.mainloop()