from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector as msql


try:
    from NewUser import *
    from AddBook import *
    from DeleteBook import *
    from IssueBook import *
    from issueList import *
    from ReturnBook import returnBook, returnn
    from ViewBooks import *
except:
    print('-----------------------------------Rerun program even if you see a window-----------------------------------')
def user():
    def kill():
        root.destroy()
    def help():
        hp = Tk()
        hp.title("Help")
        hp.minsize(width=400,height=400)
        hp.geometry("800x600")
        Canvas1 = Canvas(hp)
        
        Canvas1.config(bg="#12a4d9",width = 800, height = 600)
        Canvas1.pack(expand=True,fill=BOTH)
        headingFrame1 = Frame(hp,bg="#FFBB00",bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
        headingLabel = Label(headingFrame1, text="Help Page", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        hl=Label(hp, text="Add Book Details -- Add a new book to library\n\nDelete Book -- Remove a book from the library\n\nView Book List -- Shows a list of all the books in the library\n\nView Issue List -- Shows a list of books issued to students/members\n\nIssue Book -- Issue a book from the library to a student/member\n\nReturn Book -- Return an issued book back to the library.",font=('Verdana',14))
        hl.config(bg="#12a4d9")
        hl.place(relx=0,rely=0.3, relwidth=1, relheight=0.6)
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("1200x600")
    Canvas1 = Canvas(root)
        
    Canvas1.config(bg="#12a4d9",width = 1200, height = 600)
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome to\nTTS Library", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
   
    btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
    btn3.place(relx=0.28,rely=0.25, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="View Issue List",bg='black', fg='white', command=issuelist)
    btn4.place(relx=0.28,rely=0.35, relwidth=0.45,relheight=0.1)

    btn5 = Button(root,text="Issue Book",bg='black', fg='white', command = issueBook)
    btn5.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)
        
    btn6 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
    btn6.place(relx=0.28,rely=0.55, relwidth=0.45,relheight=0.1)
    
    btn7 = Button(root,text="Quit",bg='black', fg='white', command = kill)
    btn7.place(relx=0.28,rely=0.65, relwidth=0.45,relheight=0.1)
   
    btn8 = Button(root,text="?",bg='black', fg='white', command = help)
    btn8.place(relx=0.8,rely=0.5, relwidth=0.05,relheight=0.05)
    root.mainloop()
    
def main():
    def kill():
        root.destroy()
    def help():
        hp = Tk()
        hp.title("Help")
        hp.minsize(width=400,height=400)
        hp.geometry("800x600")
        Canvas1 = Canvas(hp)
        
        Canvas1.config(bg="#12a4d9",width = 800, height = 600)
        Canvas1.pack(expand=True,fill=BOTH)
        headingFrame1 = Frame(hp,bg="#FFBB00",bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
        headingLabel = Label(headingFrame1, text="Help Page", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        hl=Label(hp, text="Add Book Details -- Add a new book to library\n\nDelete Book -- Remove a book from the library\n\nView Book List -- Shows a list of all the books in the library\n\nView Issue List -- Shows a list of books issued to students/members\n\nIssue Book -- Issue a book from the library to a student/member\n\nReturn Book -- Return an issued book back to the library.",font=('Verdana',14))
        hl.config(bg="#12a4d9")
        hl.place(relx=0,rely=0.3, relwidth=1, relheight=0.6)
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("1200x600")
    Canvas1 = Canvas(root)
        
    Canvas1.config(bg="#12a4d9",width = 1200, height = 600)
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome to\nTTS Library", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
    btn1.place(relx=0.28,rely=0.25, relwidth=0.45,relheight=0.1)
        
    btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
    btn2.place(relx=0.28,rely=0.35, relwidth=0.45,relheight=0.1)
        
    btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
    btn3.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="View Issue List",bg='black', fg='white', command=issuelist)
    btn4.place(relx=0.28,rely=0.55, relwidth=0.45,relheight=0.1)

    btn5 = Button(root,text="Issue Book",bg='black', fg='white', command = issueBook)
    btn5.place(relx=0.28,rely=0.65, relwidth=0.45,relheight=0.1)
        
    btn6 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
    btn6.place(relx=0.28,rely=0.75, relwidth=0.45,relheight=0.1)
    
    btn7 = Button(root,text="Quit",bg='black', fg='white', command = kill)
    btn7.place(relx=0.28,rely=0.85, relwidth=0.45,relheight=0.1)
   
    btn8 = Button(root,text="?",bg='black', fg='white', command = help)
    btn8.place(relx=0.8,rely=0.5, relwidth=0.05,relheight=0.05)

    btn9 = Button(root,text="Create new USER",bg='black', fg='white', command = newUser)
    btn9.place(relx=0.1,rely=0.5, relwidth=0.15,relheight=0.05)
    root.mainloop()
    

def clear():
    uname.delete(0, END)
    entry.delete(0, END)





try:
    mycon=msql.connect(host='localhost', user='root', passwd='root', database='lib')
    if mycon.is_connected():
        print('Successfully connected!')
    if mycon.is_connected()==False:
        print('Error!') 
    mycon.close()
except:

    import mysql.connector

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE lib")
    mydb.close()
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database='lib'
    )

    mycursor = mydb.cursor()
    mycursor.execute("create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));")
    mycursor.execute("create table books_issued(bid varchar(20) primary key, issuedto varchar(30), issuedate varchar(20));")
    print('Database does not exist!\n---------CREATING DATABASE---------\n---------DATABASE CREATED---------\n---------Rerun the Program---------')
try:
    mycon=msql.connect(host='localhost', user='root', passwd='root', database='login')
    if mycon.is_connected():
        print('Successfully connected!')
    if mycon.is_connected()==False:
        print('Error!')
    cur=mycon.cursor()
    try:
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database='login'
        )

        mycursor = mydb.cursor()
        mycursor.execute("select * from uname;")
        f=mycursor.fetchall()
        e=('master','root','y')
        if e not in f:
            mycursor.execute("insert into uname values('master','root','y');")
            mydb.commit()
        else:
            print('continue')
    except:
        print('continue2')
        
    def next1(event):
        entry.focus_set()

    def next2(event):
        enter.focus_set() 
    win = Tk()
    win.geometry("400x200")
    password = StringVar()
    username = StringVar()
    try:
        cur.execute("select * from uname")
        f=cur.fetchall()
        def log():
            p = password.get()
            u = username.get()
            z = ['y','n']
            for i in z:
                x = (u,p,i)
                if x in f:
                    win.destroy()
                    if i=='y':    
                        main()
                    else:
                        user()
                    break
                else:
                    ttk.Label(win, text="Wrong Username or Password").pack()

        def log2(event):
            p = password.get()
            u = username.get()
            z = ['y','n']
            for i in z:
                x = (u,p,i)
                if x in f:
                    win.destroy()
                    if i=='y':    
                        main()
                    else:
                        user()
                    break
                else:
                    ttk.Label(win, text="Wrong Username or Password").pack()
        ttk.Label(win, text="Username").pack()
        uname = Entry(win, width=25, textvariable=username)
        uname.pack(pady=10)
        uname.bind('<Return>', next1)

        ttk.Label(win, text="Password").pack()
        entry = Entry(win, width=25, textvariable=password, show="*")
        entry.pack(pady=10)
        entry.bind('<Return>', next2)
        
        enter = Button(win, text="Login", command=log)
        enter.bind('<Return>', log2)
        enter.pack()

        ttk.Label(win, text="(Keep hitting Enter to navigate / submit or\n            or press button to submit!)").pack()

        win.mainloop()
    except:
        print('Cannot fetch data from db')
   
    mycon.close()
except:
    import mysql.connector
    try:
        mycon=msql.connect(host='localhost', user='root', passwd='root', database='login')
        mycon.close()
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database='login'
        )

        mycursor = mydb.cursor()
        mycursor.execute("create table uname(uname varchar(30) primary key, pass varchar(30), trueadmin varchar(1));")
        mycursor.execute("select * from uname;")
        f=mycursor.fetchall()
        e=('master','root','y')
        if e in f:
            print('continue')
        else:
            mycursor.execute("insert into uname values('master','root','y');")
            print('Database does not exist!\n---------CREATING DATABASE---------\n---------DATABASE CREATED---------\n---------Rerun the Program---------')

    except:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
        )

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE login")
        mydb.close()
        
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database='login'
    )

    mycursor = mydb.cursor()
    mycursor.execute("create table uname(uname varchar(30) primary key, pass varchar(30), trueadmin varchar(1));")
    mycursor.execute("select * from uname;")
    f=mycursor.fetchall()
    e=('master','root','y')
    if e in f:
        print('continue')
    else:
        mycursor.execute("insert into uname values('master','root','y');")
        print('Database does not exist!\n---------CREATING DATABASE---------\n---------DATABASE CREATED---------\n---------Rerun the Program---------')

