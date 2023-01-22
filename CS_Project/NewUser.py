from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector as msql

mycon=msql.connect(host='localhost', username='root', passwd='root', database='login')
cur=mycon.cursor()

def newUser():
    global password, username, tadmin, mycon, cur, root
    def next1(event):
        ent.focus_set()
    def next2(event):
        ent3.focus_set() 

    def next3(event):
        enter.focus_set() 


    new = Tk()
    new.geometry("600x400")
    password = StringVar()
    username = StringVar()
    tadmin = StringVar()
    
    ttk.Label(new, text="Username").pack()
    name = Entry(new, width=25, textvariable=username)
    name.pack(pady=10)
    name.bind('<Return>', next1)

    ttk.Label(new, text="Password").pack()
    ent = Entry(new, width=25, textvariable=password)
    ent.pack(pady=10)
    ent.bind('<Return>', next2)
    
    ttk.Label(new, text="Admin Permission (y/n)").pack()
    ent3 = Entry(new, width=25, textvariable=tadmin)
    ent3.pack(pady=10)
    ent3.bind('<Return>', next3)

    def y():
        p=ent.get()
        u = name.get()
        b = ent3.get()
        print(u,p,b)
        sqls="insert into uname values ('"+u+"','"+p+"','"+b+"');"
        print(sqls)
        cur.execute(sqls)
        mycon.commit()
        messagebox.showinfo('Success',"User added successfully")
        new.destroy()
    def y2(event):
        p=ent.get()
        u = name.get()
        b = ent3.get()
        print(u,p,b)
        sqls="insert into uname values ('"+u+"','"+p+"','"+b+"');"
        print(sqls)
        cur.execute(sqls)
        mycon.commit()
        messagebox.showinfo('Success',"User added successfully")
        new.destroy()
        
    enter = Button(new, text="Add User", command=y)
    enter.bind('<Return>', y2)
   
    enter.pack()
    mycon.commit()
    ttk.Label(new, text="(Keep hitting Enter to navigate / submit or\n            or press button to submit!)").pack()

    new.mainloop()
    mycon.close()
