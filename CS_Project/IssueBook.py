from tkinter import *

import mysql.connector as msql
from tkinter import messagebox

mycon=msql.connect(host='localhost', user='root', passwd='root', database='lib')

cur=mycon.cursor()
def issue():
    global bookInfo1 ,bookInfo2, bookInfo3, bookInfo4, Canvas1, mycon, cur, bookTable, root
    global issueBtn,labelFrame,lb1,inf1,inf2,inf3,quitBtn,root,Canvas1,status
    bookTable = "books"
    issueTable = "books_issued" 
    allBid = []
    bid = inf1.get()
    issueto = inf2.get()
    issuedate = inf3.get()
    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    inf3.destroy()
    
    extractBid = "select bid from "+bookTable
    try:
        cur.execute(extractBid)
        
        for i in cur:
            allBid.append(i[0])
        mycon.commit()
        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            
            for i in cur:
                check = i[0]
                
            if check == 'avail':
                status = True
            else:
                status = False
            mycon.commit()
        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    issueSql = "insert into "+issueTable+" values ('"+bid+"','"+issueto+"','"+issuedate+"')"
    show = "select * from "+issueTable
    
    updateStatus = "update "+bookTable+" set status = 'issued' where bid = '"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            mycon.commit()
            cur.execute(updateStatus)
            mycon.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    print(bid)
    print(issueto)
    
    allBid.clear()

def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,inf3,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    lb3 = Label(labelFrame,text="Issued Date : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.6)
        
    inf3 = Entry(labelFrame)
    inf3.place(relx=0.3,rely=0.6, relwidth=0.62)
    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()