from tkinter import *

import mysql.connector as msql
from tkinter import messagebox

mycon=msql.connect(host='localhost', user='root', passwd='root', database='lib')

cur=mycon.cursor()
def View(): 
    global bookInfo1 ,bookInfo2, bookInfo3, bookInfo4, Canvas1, mycon, cur, bookTable, root
    bookTable = "books"
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font = ('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    Label(labelFrame, text="%-10s%-40s%-30s%-20s"%('BID','Title','Author','Status'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        for i in cur:
            Label(labelFrame,text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
        mycon.commit()
    except:
        messagebox.showinfo("Error","Failed to fetch files from database")
    def export():
        ex='select * from books'
        cur.execute(ex)
        l=cur.fetchall()
        fh=open(".//Exports//data.txt","w")
        for i in l:
            i=str(i)+'\n'
            fh.write(str(i))
        messagebox.showinfo("Success","File exported to CS_Project/Exports/data.txt")
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.6,rely=0.9, relwidth=0.18,relheight=0.08)
    exBtn = Button(root,text="Export",bg='#f7f1e3', fg='black', command=export)
    exBtn.place(relx=0.2,rely=0.9, relwidth=0.18,relheight=0.08)    
    root.mainloop()
