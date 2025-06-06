from tkinter import *
import time
import mysql.connector
from mysql.connector import errorcode

  
class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('780x500')
        self.title("Personal Expense Tracker")
    def setMainFrame(self):
        mainFrame=Frame(self)
        mainFrame.pack()
        l1=Label(mainFrame,text="Personal Expense Tracker",font=("Arial",30),pady=10)
        l1.pack()
        
        # top_frame = Frame(mainFrame)
        # top_frame.pack(side="top", anchor="n", pady=20)
        
        b1=Button(mainFrame,text="Add Expense",font=(20),command=sql_add_expense)
        b1.pack(side="left", expand=True,pady=10,padx=20,)
        b2=Button(mainFrame,text="View Expense",font=(20))
        b2.pack(side="left", expand=True,pady=10,padx=20)            
        b3=Button(mainFrame,text="Export CSV",font=(20))
        b3.pack(side="left", expand=True,pady=10,padx=20)    
        self.AddExpense()        
        
    def date_and_time(self):
        curr_year=time.strftime("%Y")
        curr_month=time.strftime("%m")
        curr_date=time.strftime("%d")
        curr_hour=time.strftime("%H")
        curr_minute=time.strftime("%M")
        curr_second=time.strftime("%S")
        
        return (curr_year,curr_month,curr_date,curr_hour,curr_minute,curr_second)        
    
    def AddExpense(self):    
        f1=LabelFrame(self,text="Add Expense",font=(5))
        f1.pack(ipadx=10,ipady=10)
        
        l1=Label(f1,text="Amount      ",font=("Arial",10))
        l1.grid(row=1,column=1,sticky="w")
        e1=Entry(f1,width=80)
        e1.grid(row=1,column=2,sticky="w")
        
        l2=Label(f1,text="Category    ",font=("Arial",10))
        l2.grid(row=2,column=1,sticky="w")
        e2=Entry(f1,width=80)
        e2.grid(row=2,column=2,sticky="w")
        
        l3=Label(f1,text="Date         ",font=("Arial",10))
        l3.grid(row=3,column=1,sticky="w")
        e3=Entry(f1,width=80)
        e3.grid(row=3,column=2,sticky="w")
        b1=Button(f1,text="hello").grid(row=3,column=3,padx=10)
        
        l4=Label(f1,text="Description  ",font=("Arial",10))
        l4.grid(row=4,column=1,columnspan=2,sticky="w")
        tf1=Text(f1,height=4,width=60)
        tf1.grid(row=4,column=2,sticky="w")
    
    def sql_add_expense(self):
        self.connect_to_db()



if __name__=="__main__":
    app=App()
    app.setMainFrame()
    app.mainloop()


