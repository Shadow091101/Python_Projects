from tkinter import *
import time
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime,timedelta
from tkcalendar import Calendar
from tkinter import messagebox
import csv
from tkinter import filedialog
from db_config import db_config
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
                host=db_config["host"],
                user=db_config["user"],
                password=db_config["password"]
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
        self.b3=Button(mainFrame,text="Export CSV",font=(20),command=self.export_to_csv,state=DISABLED)
        self.b3.pack(side="left", expand=True,pady=10,padx=20)
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
        self.b3.config(state=DISABLED)
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
        self.b1=Button(self.f1,text="Custom",command=lambda:self.select_custom_date_time(self.datetime))
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
            
        
    def select_custom_date_time(self,target_datetime_var):
        
        toplevel1=Toplevel(self)
        toplevel1.grab_set()
        self.custom_date_target_var=target_datetime_var
        self.custom_date_window=toplevel1
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
        
        okbutton=Button(f1,text="OK",anchor="center",command=self.return_selection)
        okbutton.grid(row=4,column=1,columnspan=4)
        
    def return_selection(self):
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
            self.custom_date_target_var.set(final_datetime)
            self.custom_date_window.destroy()
        

    def sql_add_expense(self):
        self.AddExpense() 
        self.init_db()  
       
    select_query_="SELECT amount,category,description,datetime FROM expenses ORDER BY datetime DESC ;"
    
    query_array=[]
    def export_to_csv(self):
        self.ensure_connection()
        export_query=self.query_array[0] if self.query_array else self.select_query_
        try:
            self.cursor.execute(export_query)
            result = self.cursor.fetchall()
            columns = [desc[0] for desc in self.cursor.description]
            
            if not result:
                messagebox.showwarning("No Data", "No data to export.")
                return
            
            # Ask for save location
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if not file_path:
                return  # User cancelled

            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(columns)  # Write headers
                writer.writerows(result)  # Write data
            
            messagebox.showinfo("Export Successful", f"Data exported successfully to:\n{file_path}")
            
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error while exporting to CSV:\n{err}")

        
    def View_Expense(self,query=None):
        self.b3.config(state=ACTIVE)
        def edit_rows(id):
            query=f"SELECT amount,category,datetime,description FROM expenses WHERE id={id}"
            self.cursor.execute(query)
            result=self.cursor.fetchone()
            # print("Selected row : "+str(result))
            column_names = ['amount', 'category', 'datetime', 'description']
            if result:
                for col_name, cell_data in zip(column_names, result):
                    print(f"{col_name}: {cell_data}")
            edit_top_level=Toplevel(self.f1)
            edit_top_level.grab_set() 
            # edit_top_level.attributes("-topmost", True)
            edit_window_frame=Frame(edit_top_level)
            edit_window_frame.pack(padx=10,pady=10,ipadx=10,ipady=10)
            l1=Label(edit_window_frame,text="Select what you want to do with this record: ")
            l1.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky=NSEW)
            delete_button=Button(edit_window_frame,text="Delete",command=lambda:delete_record(id))
            delete_button.grid(row=1,column=0,padx=5,pady=5)
            update_button=Button(edit_window_frame,text="Update",command=lambda:update_record(id))
            update_button.grid(row=1,column=1,padx=5,pady=5)
            
            def update_record(id):
                
                def reset_update():
                    if messagebox.askyesno("Reset","Do you want to reset the entries? "):
                        update_amount.set(row_data[0])
                        update_category_var.set(row_data[1])
                        update_datetime.set(row_data[2])
                        tf2.delete("1.0",END)
                        tf2.insert("1.0",row_data[3])
                        
                def submit_update():
                    self.ensure_connection()
                    if messagebox.askyesno("Submit","Do you confirm your updation ?"):
                        update_query ="""
                            UPDATE expenses
                            SET amount=%s,
                                category=%s,
                                datetime=%s,
                                description=%s
                            WHERE id=%s
                        """
                        values=(
                            update_amount.get(),
                            update_category_var.get(),
                            update_datetime.get(),
                            tf2.get("1.0","end-1c"),
                            id
                        )
                        try:
                            self.cursor.execute(update_query,values)
                            messagebox.showinfo("Update Saved", "Your expense has been updated successfully to the database!")
                            self.connection.commit()
                            edit_top_level.destroy()
                            self.View_Expense(self.select_query_)
                        except mysql.connector.Error as err:
                            messagebox.showerror("Error","Something went wrong while updating your expense! Please try again later.")
                            print(err)
                    
                row_data=[]
                try:
                    self.cursor.execute(f"SELECT amount,category,datetime,description FROM expenses WHERE id={id}")
                    result=self.cursor.fetchone()
                    if result:
                        for col_name, cell_data in zip(column_names, result):
                            print(f"{cell_data}")    
                            row_data.append(cell_data)
                except mysql.connector.Error as err:
                    print(err)
                
                update_datetime=StringVar() 
                update_datetime.set(row_data[2])
                update_amount=StringVar()
                update_amount.set(row_data[0])
                update_category_var=StringVar()
                update_category_var.set(row_data[1])
                for widgets in edit_window_frame.winfo_children():
                    widgets.destroy()
                l1=Label(edit_window_frame,text="Update Record")
                l1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
                for i in range(1,5):
                    l=Label(edit_window_frame,text=f"{column_names[i-1]}")
                    l.grid(row=i,column=0,pady=10,padx=10)
                e1=Entry(edit_window_frame,textvariable=update_amount)
                e1.grid(row=1,column=1,sticky="w")
                e2 = OptionMenu(edit_window_frame, update_category_var, *self.categories)
                e2.grid(row=2,column=1,sticky="w")
                e3=Entry(edit_window_frame,textvariable=update_datetime,state="readonly")
                e3.grid(row=3,column=1,sticky="w")
                b1=Button(edit_window_frame,text="Custom",command=lambda:self.select_custom_date_time(update_datetime))
                b1.grid(row=3,column=2,padx=10,sticky="w")
                tf2=Text(edit_window_frame,height=6,width=60)
                tf2.grid(row=4,column=1,sticky="w")  
                tf2.insert("1.0",row_data[3])
                submit_btn=Button(edit_window_frame,text="Submit",command=submit_update)
                submit_btn.grid(row=5,column=1,sticky="e",pady=10)
                reset_btn=Button(edit_window_frame,text="Reset",command=reset_update)
                reset_btn.grid(row=5,column=2,sticky="e",pady=10)  
            def delete_record(id):
                query=f"DELETE FROM expenses WHERE id={id}"
                try:
                    self.cursor.execute(query)
                    self.connection.commit()
                    messagebox.showinfo("Success","Record deleted")
                    edit_top_level.destroy()
                    self.View_Expense(self.select_query_)
                except mysql.connector.Error as err:
                    messagebox.showerror("ERROR","Error occured while deleting the record. Please try again later.")
            pass
        
        def sort_window():
            sort_top_level = Toplevel(self.f1)
            sort_window_frame = Frame(sort_top_level)
            sort_window_frame.pack(padx=10, pady=10, ipadx=10, ipady=10)

            # Configure columns for equal expansion
            for i in range(2):
                sort_window_frame.grid_columnconfigure(i, weight=1)

            # SORT BY Title
            sort_window_label_1 = Label(
                sort_window_frame,
                text="SORT BY",
                font=("Arial", 12, "bold"),
                borderwidth=1,
                relief="solid",
                padx=20,
                pady=5
            )
            sort_window_label_1.grid(row=0, column=0, columnspan=2, pady=(0, 15), sticky="ew")
            
            def apply_and_keep(query):
                self.View_Expense(query)

            # ----- Sorting functions -----
            def amount_sort_ascfunc():
                if self.query_array:
                    sort_query = str(self.query_array[0]).replace("BY datetime DESC", "BY amount ASC")
                    self.View_Expense(sort_query)
                else:
                    sorted_simple_query = self.select_query_.replace("BY datetime DESC", "BY amount ASC")
                    self.View_Expense(sorted_simple_query)

            def amount_sort_descfunc():
                if self.query_array:
                    sort_query = str(self.query_array[0]).replace("BY datetime", "BY amount")
                    self.View_Expense(sort_query)
                else:
                    sorted_simple_query = self.select_query_.replace("BY datetime", "BY amount")
                    self.View_Expense(sorted_simple_query)

            def date_sort_ascfunc():
                if self.query_array:
                    sort_query = str(self.query_array[0]).replace("DESC", "ASC")
                    self.View_Expense(sort_query)
                else:
                    self.View_Expense(self.select_query_.replace("DESC", "ASC"))

            def date_sort_descfunc():
                if self.query_array:
                    self.View_Expense(self.query_array[0])
                else:
                    self.View_Expense(self.select_query_)

            # ----- Amount section -----
            amount_label = Label(sort_window_frame, text="Amount", font=("Arial", 10, "bold"))
            amount_label.grid(row=1, column=0, pady=(0, 5))

            amount_sort_asc = Button(sort_window_frame, text="Ascending", width=12, command=lambda: apply_and_keep(
               str(self.query_array[0]).replace("BY datetime DESC", "BY amount ASC")
               if self.query_array else self.select_query_.replace("BY datetime DESC", "BY amount ASC")))
            amount_sort_asc.grid(row=2, column=0, pady=5)

            amount_sort_desc = Button(sort_window_frame, text="Descending", width=12, command=lambda: apply_and_keep(
               str(self.query_array[0]).replace("BY datetime", "BY amount")
               if self.query_array else self.select_query_.replace("BY datetime", "BY amount")))
            amount_sort_desc.grid(row=3, column=0, pady=5)

            # ----- Date section -----
            date_label = Label(sort_window_frame, text="Date", font=("Arial", 10, "bold"))
            date_label.grid(row=1, column=1, pady=(0, 5))

            date_sort_asc = Button(sort_window_frame, text="Ascending", width=12, command=lambda: apply_and_keep(
               str(self.query_array[0]).replace("DESC", "ASC")
               if self.query_array else self.select_query_.replace("DESC", "ASC")))
            date_sort_asc.grid(row=2, column=1, pady=5)

            date_sort_desc = Button(sort_window_frame, text="Descending", width=12, command=lambda: apply_and_keep(
               self.query_array[0] if self.query_array else self.select_query_))
            date_sort_desc.grid(row=3, column=1, pady=5)
            
            Button(sort_window_frame, text="Close", width=25, command=sort_top_level.destroy)\
        .grid(row=4, column=0, columnspan=2, pady=(15, 5))
            
            # asc_button=Button(sort_window_frame,text="Ascending",command=asc_sort)
            # asc_button.grid(row=1,column=0,padx=10,pady=10)
            # desc_button=Button(sort_window_frame,text="Descending",command=desc_sort)
            # desc_button.grid(row=2,column=0,padx=10,pady=10)
            
        def filter_window():
            filter_top_level=Toplevel(self.f1)
            filter_window_frame=Frame(filter_top_level)
            filter_window_frame.pack(padx=10,pady=10,ipadx=10,ipady=10)
            filter_window_label_1=Label(filter_window_frame,text="Select What you want to sort : ")
            filter_window_label_1.grid(row=0,column=0,columnspan=2)
            
            category_filter_var=StringVar()
            category_filter_var.set("")
            category_filter_options=self.categories
            
            amount_filter_var=StringVar()
            amount_filter_var.set("")
            amount_filter_options=["BETWEEN 0 AND 10","BETWEEN 10 AND 50","BETWEEN 50 AND 100","BETWEEN 100 AND 500",">500"]
                
            selected_query={"query":None}
            
            def category(*args):
                print(category_filter_var.get())
                query=f"SELECT amount,category,description,datetime FROM expenses WHERE category ='{category_filter_var.get()}' ORDER BY datetime DESC ;"
                self.query_array.clear()
                self.query_array.append(query)
                # print("Select :",query)
                # self.View_Expense(query)
                selected_query["query"]=query
                # print("Success",category_filter_var.get())
            
            def op(*args):
                query=f"SELECT amount,category,description,datetime FROM expenses WHERE amount {amount_filter_var.get()} ORDER BY datetime DESC ;"
                self.query_array.clear()
                self.query_array.append(query)
                # print("Select :",query)
                # self.View_Expense(query)
                selected_query["query"] = query
                # print("Success",amount_filter_var.get())
            
            def apply_filter():
                if selected_query["query"]:
                    self.View_Expense(selected_query["query"])
                
            category_filter_var.trace_add("write",category)
            category_filter_label=Label(filter_window_frame,text="Category")
            category_filter_label.grid(row=1,column=0)
            category_option_filter=OptionMenu(filter_window_frame,category_filter_var,*category_filter_options)
            category_option_filter.grid(row=1,column=1)
            
            amount_filter_var.trace_add("write",op)
            amount_filter_label=Label(filter_window_frame,text="Amount")
            amount_filter_label.grid(row=2,column=0)
            amount_option_filter=OptionMenu(filter_window_frame,amount_filter_var,*amount_filter_options)
            amount_option_filter.grid(row=2,column=1) 
            
            Button(filter_window_frame, text="Apply", command=apply_filter).grid(row=3, column=0, columnspan=2, pady=10)
            Button(filter_window_frame, text="Close", command=filter_top_level.destroy).grid(row=4, column=0, columnspan=2)
            
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
                'edit':7,
                'amount':10,
                'category':15,
                'description':55,
                'datetime':15
            }
            self.cursor.execute("SELECT * FROM expenses")
            result = self.cursor.fetchall()
            column_names=[desc[0] for desc in self.cursor.description]
            column_names[0]="edit"
            print(column_names)
            for col,name in enumerate(column_names):
                self.width=column_width.get(name,15)
                self.col_label=Label(self.scroll_frame,text=name,font=("Arial",10,"bold"), borderwidth=1, relief="solid", width=self.width)
                self.col_label.grid(row=0,column=col,sticky="nsew")
        
           
            for row_num,row_data in enumerate(result,start=1):
                userid = str(row_data[0])
                edit_button=Button(self.scroll_frame,text="Edit",command=lambda uid =userid:edit_rows(uid))
                edit_button.grid(row=row_num,column=0,padx=5)
                for col_num,(col_name, cell_data) in enumerate(zip(column_names[1:], row_data[1:]), start=1):
                    # col_name = column_names[col_num]
                    width = column_width.get(col_name, 15)
                    sticky = "nsew" if col_name == 'description' else "nsew"
                    row_labels=Label(self.scroll_frame,text=cell_data,borderwidth=1, relief="solid", width=width,anchor="w")
                    row_labels.grid(row=row_num,column=col_num,sticky=sticky)
            
            
        except mysql.connector.Error as err:
            Label(self.scroll_frame, text=f"Database error: {err}").grid(row=0, column=0)
            print(err)
        
        # def filter_window():
        #     filter_top_level=Toplevel(self.f1)
        #     filter_window_frame=Frame(filter_top_level)
        #     filter_window_frame.pack(padx=10,pady=10,ipadx=10,ipady=10)
        #     filter_window_label_1=Label(filter_window_frame,text="Select What you want to sort : ")
        #     filter_window_label_1.grid(row=0,column=0,columnspan=2)
            
        #     amount_filter_var=StringVar()
        #     amount_filter_var.set("")
        #     amount_filter_options=["BETWEEN 0 AND 10","BETWEEN 10 AND 50","BETWEEN 50 AND 100","BETWEEN 100 AND 500",">500"]
            
        #     def op(*args):
        #         query=f"SELECT amount,category,description,datetime FROM expenses WHERE amount {amount_filter_var.get()} ORDER BY datetime DESC ;"
        #         print("Select :",query)
        #         self.View_Expense(query)
        #         print("Success",amount_filter_var.get())
            
        #     amount_filter_var.trace_add("write",op)
        #     amount_filter_label=Label(filter_window_frame,text="Amount")
        #     amount_filter_label.grid(row=1,column=0)
        #     amount_option_filter=OptionMenu(filter_window_frame,amount_filter_var,*amount_filter_options)
        #     amount_option_filter.grid(row=1,column=1)
            
            # category_filter_button1=Button(filter_window_frame,text="Category",command=filter_categroy)
            # category_filter_button1.grid(row=1,column=0)
            
            
                
            
            pass
        
        button1=Button(self.f1,text="Filter",command=filter_window)
        button1.grid(row=2,column=1,sticky="ew",padx=10,pady=10)
        sort_button=Button(self.f1,text="Sort",command=sort_window,)
        sort_button.grid(row=2,column=0,padx=10,pady=10,sticky="e")
        
    
        
        
        

if __name__=="__main__":
    app=App()
    app.setMainFrame()
    app.protocol("WM_DELETE_WINDOW",app.on_closing)
    app.mainloop()



