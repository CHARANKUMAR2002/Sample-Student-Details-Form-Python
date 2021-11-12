from tkinter import *
from tkinter import ttk
master = Tk()
master.geometry('500x300')
master.resizable(0, 0)
master.title("Personal Details (Prototype)")
title = Label(master, text= "Student Details", padx=30, pady=5, font=("times", 10), bg='gray', fg='white')
title.pack(fill=X)
Label(master, text='First Name : ').place(x=10, y=30)
f_name = Text(master, height=1, width=20)
f_name.place(x=80, y=32)
Label(master, text='Last Name : ').place(x=10, y=60)
l_name = Text(master, height=1, width=20)
l_name.place(x=80, y=62)
o = IntVar()
male = Radiobutton(master, text='Male', value=1, variable=o)
male.place(x=10, y=90)
female = Radiobutton(master, text='Female', value=2, variable=o)
female.place(x=10, y=110)
Label(master, text="Course : ").place(x=10, y=150)
course = ("Select Your Course", "AERO", "CSE", "IT", "CSBS", "AUTO", "BIOTECH", "TEXTILE", "FD")
c = ttk.Combobox(master, value=course, width=20)
c.place(x=50, y=170)
c.current(0)
master.update()
DataBase = open('DataBase.txt', 'a')

def entry():
        entry_1 = f_name.get(1.0, END)
        f1 = str(entry_1)
        entry_2 = l_name.get(1.0, END)
        f2 =str(entry_2)
        if o.get() == 1:
                if c.get() == "Select Your Course":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Male' + '\n'+ 'Course : ' + "NOT SPECIFIED" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get()=="AERO":
                        DataBase.write('_'*255+ '\n'+ 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : '+'Male' + '\n'+ 'Course : '+ "AERO"+ '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get()=="CSE":
                        DataBase.write('_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Male' + '\n'+ 'Course : ' + "CSE" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get()=="IT":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Male' + '\n'+ 'Course : ' + "IT" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get()=="AUTO":
                        DataBase.write('_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Male' + '\n'+ 'Course : ' + "AUTO" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get() == "CSBS":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Male'+ '\n' + 'Course : ' + "CSBS" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get() == "BIOTECH":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Male'+ '\n' + 'Course : ' + "BIOTECH" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get() == "TEXTILE":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Male'+ '\n' + 'Course : ' + "TEXTILE" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get() == "FD":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Male'+ '\n' + 'Course : ' + "FD" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
        if o.get() == 2:
                if c.get() == "Select Your Course":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Female'+ '\n' + 'Course : ' + "NOT SPECIFIED" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get() == "AERO":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Female' + '\n'+ 'Course : ' + "AERO" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get() == "CSE":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Female'+ '\n' + 'Course : ' + "CSE" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get() == "IT":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Female'+ '\n' + 'Course : ' + "IT" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get() == "AUTO":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Female'+ '\n' + 'Course : ' + "AUTO" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get() == "CSBS":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Female' + '\n'+ 'Course : ' + "CSBS" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get() == "BIOTECH":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Female'+ '\n' + 'Course : ' + "BIOTECH" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get() == "TEXTILE":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Female'+ '\n' + 'Course : ' + "TEXTILE" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)
                elif c.get() == "FD":
                        DataBase.write(
                                '_' * 255 + '\n' + 'FIRST NAME : ' + f1 + 'LAST NAME : ' + f2 + 'Gender : ' + 'Female'+ '\n' + 'Course : ' + "FD" + '\n')
                        Label(master, text='Saved').place(x=150, y=275)

save = Button(master, text="SAVE", command=entry, width=8, bg='green', activebackground='blue')
save.place(x=210, y=275)


def exit():
        master.destroy()

close = Button(master, text="CLOSE", width=8, bg='red', activebackground='orange', command=exit)
close.place(x=280, y=275)
master.mainloop()
