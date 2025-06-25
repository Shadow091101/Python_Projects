from tkinter import *
import time
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime,timedelta
from tkcalendar import Calendar
from tkinter import messagebox
class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('780x500')
        self.title("Personal Expense Tracker")
        self.init_db()
        
    def on_closing(self):
        if messagebox.askokcancel("Quit","Do you want to quit?"):
            try:
                if self.cursor:self.cursor.close()
                if self.connection:self.connection.close()
                print("Database connection closed")
            except:
                pass
            self.destroy()
            
    def ensure_connection(self):
        try:
            if self.connection is None or not self.connection.is_connected():
                self.init_db()
        except:
            self.init_db()
    def init_db(self):
        try:
            self.connection=mysql.connector.connect(
                host="localhost",
                user="root",
                password="manavnaik@123"
            )
            self.cursor=self.connection.cursor()
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS expense_tracker")
            print("Database Created Successfully")
            self.connection.database="expense_tracker"
            
            self.cursor.execute("""
                           CREATE TABLE IF NOT EXISTS expenses(
                               id INT AUTO_INCREMENT PRIMARY KEY,
                               amount DECIMAL(10,2) NOT NULL,
                               category VARCHAR(100),
                               datetime DATETIME,
                               description TEXT
                           )
                           """)
            print("Table created/checked.")
        except mysql.connector.Error as err:
            print("MySQL Error : ",err)
        
              
    def setMainFrame(self):
        mainFrame=Frame(self)
        mainFrame.pack()
        l1=Label(mainFrame,text="Personal Expense Tracker",font=("Arial",30),pady=10)
        l1.pack()
        
        # top_frame = Frame(mainFrame)
        # top_frame.pack(side="top", anchor="n", pady=20)
        
        b1=Button(mainFrame,text="Add Expense",font=(20),command=self.sql_add_expense)
        b1.pack(side="left", expand=True,pady=10,padx=20,)
        b2=Button(mainFrame,text="View Expense",font=(20),command=self.View_Expense)
        b2.pack(side="left", expand=True,pady=10,padx=20)            
        b3=Button(mainFrame,text="Export CSV",font=(20))
        b3.pack(side="left", expand=True,pady=10,padx=20)
        self.f1=LabelFrame(self,text="",font=(30))
        self.f1.pack(ipadx=20,ipady=20,padx=30,pady=30)    
        self.AddExpense()        
        
    def date_and_time(self):
        curr_year=time.strftime("%Y")
        curr_month=time.strftime("%m")
        curr_date=time.strftime("%d")
        curr_hour=time.strftime("%H")
        curr_minute=time.strftime("%M")
        curr_second=time.strftime("%S")
        
        return f"{curr_year}-{curr_month}-{curr_date} {curr_hour}:{curr_minute}:{curr_second}"        
    
    def AddExpense(self):
        self.categories=["Food","Beverages","Emergency","Study","Medical Expenses","Entertainment","Travel","Clothing","Utilities/Bills","Lend","Gifts","Family","Friends","Others"]
        self.opt=StringVar()
        self.opt.set(value="Others")
        self.datetime=StringVar()    
        self.datetime.set(self.date_and_time())
        for widget in self.f1.winfo_children():
            widget.destroy()
        self.f1.config(text="Add Expense")
        self.l1=Label(self.f1,text="Amount      ",font=("Arial",15))
        self.l1.grid(row=1,column=1,sticky="w")
        self.e1=Entry(self.f1,width=80)
        self.e1.grid(row=1,column=2,sticky="w")
        
        self.l2=Label(self.f1,text="Category    ",font=("Arial",15))
        self.l2.grid(row=2,column=1,sticky="w")
        self.e2=OptionMenu(self.f1,self.opt,*self.categories)
        self.e2.grid(row=2,column=2,sticky="w")
        
        self.l3=Label(self.f1,text="Date         ",font=("Arial",15))
        self.l3.grid(row=3,column=1,sticky="w")
        self.e3=Entry(self.f1,width=80,textvariable=self.datetime,state="readonly")
        self.e3.grid(row=3,column=2,sticky="w")
        self.b1=Button(self.f1,text="Custom",command=self.select_custom_date_time)
        self.b1.grid(row=3,column=3,padx=10)
        
        self.l4=Label(self.f1,text="Description  ",font=("Arial",15))
        self.l4.grid(row=4,column=1,columnspan=2,sticky="w")
        self.tf1=Text(self.f1,height=6,width=60)
        self.tf1.grid(row=4,column=2,sticky="w")
        
        self.submit_button=Button(self.f1,text="Submit",anchor="e",font=("Arial",15),command=lambda : self.submit_to_sql())
        self.submit_button.grid(row=5,column=2,pady=20)
        
        self.reset_button=Button(self.f1,text="Reset",anchor="e",font=("Arial",15),command=self.reset_records)
        self.reset_button.grid(row=5,column=3,pady=20)
    
    def reset_records(self):
        if messagebox.askyesno("Reset","Do you want to reset the entries? "):
            self.e1.delete(0,END)
            self.opt.set(value="Others")
            self.datetime.set(self.date_and_time())
            self.tf1.delete("1.0","end")
    
    def submit_to_sql(self):
        self.ensure_connection()
        if messagebox.askyesno("Submit","Do you confirm your submission ?"):
            submit_query = """
                INSERT INTO expenses(amount,category,datetime,description)
            VALUES (%s,%s,%s,%s)
                        """
            values = (
                self.e1.get(),
                self.opt.get(),
                self.e3.get(),
                self.tf1.get("1.0", "end-1c")
            )

            try:
                self.cursor.execute(submit_query,values)
                messagebox.showinfo("Saved", "Your expense has been saved to the database!")
                self.e1.delete(0,END)
                self.opt.set(value="Others")
                self.datetime.set(self.date_and_time())
                self.tf1.delete("1.0","end")
                self.connection.commit()
            except mysql.connector.Error as err:
                messagebox.showerror("Error","Something went wrong while saving your expense! Please try again later.")
                print(err)
            
        
    def select_custom_date_time(self):
        
        toplevel1=Toplevel(self)
        
        f1=Frame(toplevel1)
        f1.pack(padx=10,pady=10)
        
        calenderLabel=Label(f1,text="Date",anchor="center",font=("Arial",20))
        calenderLabel.grid(row=0,column=1)
        hourLabel=Label(f1,text="H",anchor="w",font=("Arial",20))
        hourLabel.grid(row=0,column=2)
        minuteLabel=Label(f1,text="M",anchor="w",font=("Arial",20))
        minuteLabel.grid(row=0,column=3)
        secondLabel=Label(f1,text="S",anchor="w",font=("Arial",20))
        secondLabel.grid(row=0,column=4)
        self.calender1=Calendar(f1,selectmode='day')
        self.calender1.grid(row=1,column=1)
        
        hour_list_frame=Frame(f1)
        hour_list_frame.grid(row=1,column=2)
        hour_scrollbar=Scrollbar(hour_list_frame)
        hour_scrollbar.pack(side="right",fill="y")
        
        self.hour_listbox=Listbox(
            hour_list_frame,height=8,width=3,font=("Arial",14),
            exportselection=False,yscrollcommand=hour_scrollbar.set
        )
        
        for hour in range(24):
            self.hour_listbox.insert(END,f"{hour:02d}")
        
        self.hour_listbox.pack(side="left",fill="y")
        hour_scrollbar.config(command=self.hour_listbox.yview)
        
        minute_list_frame=Frame(f1)
        minute_list_frame.grid(row=1,column=3)
        minute_scrollbar=Scrollbar(minute_list_frame)
        minute_scrollbar.pack(side="right",fill="y")
        
        self.minute_listbox=Listbox(
            minute_list_frame,height=8,width=3,font=("Arial",14),
            exportselection=False,yscrollcommand=minute_scrollbar.set
        )
        
        for minute in range(60):
            self.minute_listbox.insert(END,f"{minute:02d}")
        
        self.minute_listbox.pack(side="left",fill="y")
        minute_scrollbar.config(command=self.minute_listbox.yview)
        
        second_list_frame=Frame(f1)
        second_list_frame.grid(row=1,column=4)
        second_scrollbar=Scrollbar(second_list_frame)
        second_scrollbar.pack(side="right",fill="y")
        
        self.second_listbox=Listbox(
            second_list_frame,height=8,width=3,font=("Arial",14),
            exportselection=False,yscrollcommand=second_scrollbar.set
        )
        
        for second in range(60):
            self.second_listbox.insert(END,f"{second:02d}")
        
        self.second_listbox.pack(side="left",fill="y")
        second_scrollbar.config(command=self.second_listbox.yview)
        
        l1=Label(f1,text="Select Date and Time from above : ",anchor="center")
        l1.grid(row=2,column=1,columnspan=4)
        
        okbutton=Button(f1,text="OK",anchor="center",command=lambda : self.return_selection(toplevel1))
        okbutton.grid(row=4,column=1,columnspan=4)
        
    def return_selection(self,toplevel1):
        if not self.hour_listbox.curselection() or not self.minute_listbox.curselection() or not self.second_listbox.curselection():
            messagebox.showwarning("No Selection","Please select appropriate time.")
            return
        selected_date=self.calender1.get_date() 
        hour=self.hour_listbox.get(self.hour_listbox.curselection()[0])
        print(hour)
        minute=self.minute_listbox.get(self.minute_listbox.curselection()[0])
        print(minute)
        second=self.second_listbox.get(self.second_listbox.curselection()[0])
        print(second)
        dt_obj = datetime.strptime(selected_date, "%m/%d/%y")
        formatted_date = dt_obj.strftime("%Y-%m-%d")
        
        final_datetime = f"{formatted_date} {hour}:{minute}:{second}"
        if messagebox.askyesno("Confirmation",f"The Date is {formatted_date} and Time is {hour}:{minute}:{second}"):
            self.datetime.set(final_datetime)
            toplevel1.destroy()
        

    def sql_add_expense(self):
        self.AddExpense() 
        self.init_db()  
        
    select_query_="SELECT amount,category,description,datetime FROM expenses ORDER BY datetime DESC ;"
    def View_Expense(self,query=None):
        def filter_window():
            filter_top_level=Toplevel(self.f1)
            filter_window_frame=Frame(filter_top_level)
            filter_window_frame.pack(padx=10,pady=10,ipadx=10,ipady=10)
            filter_window_label_1=Label(filter_window_frame,text="Select What you want to sort : ")
            filter_window_label_1.grid(row=0,column=0,columnspan=2)
            
            amount_filter_var=StringVar()
            amount_filter_var.set("")
            amount_filter_options=["BETWEEN 0 AND 10","BETWEEN 10 AND 50","BETWEEN 50 AND 100","BETWEEN 100 AND 500",">500"]
            
            category_filter_var=StringVar()
            category_filter_var.set()
            category_filter_options=self.categories
            
            def op(*args):
                query=f"SELECT amount,category,description,datetime FROM expenses WHERE amount {amount_filter_var.get()} ORDER BY datetime DESC ;"
                print("Select :",query)
                self.View_Expense(query)
                print("Success",amount_filter_var.get())
                
            def category(*args):
                query=f"SELECT amount,category,description,datetime FROM expenses WHERE category = {category_filter_var.get()} ORDER BY datetime DESC ;"
                print("Select :",query)
                self.View_Expense(query)
                print("Success",category_filter_var.get())
            
            amount_filter_var.trace_add("write",op)
            amount_filter_label=Label(filter_window_frame,text="Amount")
            amount_filter_label.grid(row=1,column=0)
            amount_option_filter=OptionMenu(filter_window_frame,amount_filter_var,*amount_filter_options)
            amount_option_filter.grid(row=1,column=1)
            
            category_filter_var.trace_add("write",category)
            category_filter_label=Label(filter_window_frame,text="Category")
            category_filter_label.grid(row=2,column=0)
            category_option_filter=OptionMenu(filter_window_frame,category_filter_var,*category_filter_options)
            category_option_filter.grid(row=2,column=1)
            
            
        if query==None:
            query=self.select_query_
        for widget in self.f1.winfo_children():
            widget.destroy()
        self.f1.config(text="View Expense")
        self.f1.config()
        
        self.canvas=Canvas(self.f1,width=800)
        self.scrollbar=Scrollbar(self.f1,command=self.canvas.yview,orient="vertical")
        self.horizontal_scrollbar=Scrollbar(self.f1,command=self.canvas.xview,orient='horizontal')
        self.scroll_frame=Frame(self.canvas)
        
        self.scroll_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0,0),window=self.scroll_frame,anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set,xscrollcommand=self.horizontal_scrollbar.set)
        
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.horizontal_scrollbar.grid(row=1, column=0, sticky="ew")

        self.f1.grid_rowconfigure(0, weight=1)
        self.f1.grid_columnconfigure(0, weight=1)
        try:
            select_query=query
            self.cursor.execute(select_query)
            result=self.cursor.fetchall()
            if not result:
                Label(self.scroll_frame,text="No records found").grid(row=0,column=0,padx=10,pady=10)
                button1=Button(self.f1,text="Filter",command=filter_window)
                button1.grid(row=2,column=1,sticky="ew",padx=10,pady=10)
                return
            
            column_width={
                'id':5,
                'amount':10,
                'category':15,
                'description':55,
                'datetime':15
            }
            column_names=[desc[0] for desc in self.cursor.description]
            for col,name in enumerate(column_names):
                self.width=column_width.get(name,15)
                self.col_label=Label(self.scroll_frame,text=name,font=("Arial",10,"bold"), borderwidth=1, relief="solid", width=self.width)
                self.col_label.grid(row=0,column=col,sticky="nsew")
        
            for row_num,row_data in enumerate(result,start=1):
                for col_num,cell_data in enumerate(row_data):
                    col_name = column_names[col_num]
                    width = column_width.get(col_name, 15)
                    sticky = "nsew" if col_name == 'description' else "nsew"
                    row_labels=Label(self.scroll_frame,text=cell_data,borderwidth=1, relief="solid", width=width,anchor="w")
                    row_labels.grid(row=row_num,column=col_num,sticky=sticky)
            
            
        except mysql.connector.Error as err:
            Label(self.scroll_frame, text=f"Database error: {err}").grid(row=0, column=0)
            print(err)
        
        def filter_window():
            filter_top_level=Toplevel(self.f1)
            filter_window_frame=Frame(filter_top_level)
            filter_window_frame.pack(padx=10,pady=10,ipadx=10,ipady=10)
            filter_window_label_1=Label(filter_window_frame,text="Select What you want to sort : ")
            filter_window_label_1.grid(row=0,column=0,columnspan=2)
            
            amount_filter_var=StringVar()
            amount_filter_var.set("")
            amount_filter_options=["BETWEEN 0 AND 10","BETWEEN 10 AND 50","BETWEEN 50 AND 100","BETWEEN 100 AND 500",">500"]
            
            def op(*args):
                query=f"SELECT amount,category,description,datetime FROM expenses WHERE amount {amount_filter_var.get()} ORDER BY datetime DESC ;"
                print("Select :",query)
                self.View_Expense(query)
                print("Success",amount_filter_var.get())
            
            amount_filter_var.trace_add("write",op)
            amount_filter_label=Label(filter_window_frame,text="Amount")
            amount_filter_label.grid(row=1,column=0)
            amount_option_filter=OptionMenu(filter_window_frame,amount_filter_var,*amount_filter_options)
            amount_option_filter.grid(row=1,column=1)
            
            # category_filter_button1=Button(filter_window_frame,text="Category",command=filter_categroy)
            # category_filter_button1.grid(row=1,column=0)
            
            
                
            
            pass
        
        button1=Button(self.f1,text="Filter",command=filter_window)
        button1.grid(row=2,column=1,sticky="ew",padx=10,pady=10)
        
            
        
        
        

if __name__=="__main__":
    app=App()
    app.setMainFrame()
    app.protocol("WM_DELETE_WINDOW",app.on_closing)
    app.mainloop()



