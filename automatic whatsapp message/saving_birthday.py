import mysql.connector as mysql
from datetime import datetime

def connect_to_db():
    try:
        return mysql.connect(user='root', password='your_db_password', host='Your-host', port=3306, database='your_db_name')#host can be localhost
    except mysql.Error as err:
        print(f"Error connecting to database: {err}")
        exit(1)

def is_valid_phone_number(phone):
    return phone.startswith("+") and phone[1:].isdigit() and len(phone) >= 10

def set_birthday():
    
    conn=connect_to_db()
    cursor=conn.cursor()
    
    
    while(True):
        print("\n 1. To Save birthdate to Database\t 2. Quit \t Enter your choice : ")
        choice=input("\nEnter your choice : ").strip()
        if choice=="1" :
            try:
                birthdate=input("\nEnter the birthdate(YYYY-MM-DD) of whom U which to send Wishes :").strip()
                Name=input("\n Enter the name of the person to whom you wish to send wishes : ").strip()
                Message=input("\n Enter the message you wants to send : ").strip()
                Phone_number=input("\n Enter their Whatapp no.(with country code) : ").strip()
            
                if not birthdate or not Name or not Message or not Phone_number:
                    print("All fields are required. Please try again.")
                    continue 
                
                try:
                    datetime.strptime(birthdate, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    continue
                
                if not is_valid_phone_number(Phone_number):
                    print("Invalid phone number. Please include the country code (e.g., +1234567890).")
                    continue
                
                # Check for duplicates
                cursor.execute("SELECT * FROM whatauto WHERE name = %s AND date = %s", (Name, birthdate))
                if cursor.fetchone():
                    print("This birthday is already saved in the database.")
                    continue
                
                query = "INSERT INTO whatauto (name, number, date, message) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (Name, Phone_number, birthdate, Message))
                conn.commit()
 
                print("Birthdate added to database successfully.")
            except mysql.Error as err:
                print(f"Database error: {err}")
            except Exception as e:
                print(f"Unexpected error: {e}")           
                
        elif choice=="2" :
            print("Exiting the program.")
            break
        else:
            print("Invalid Choice Please enter 1 or 2 : ")
    cursor.close()
    conn.close()
            
if __name__ == "__main__":
    set_birthday()
    
            
            
            
        
             
            
            

