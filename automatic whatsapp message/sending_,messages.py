import time
from datetime import datetime, timedelta
import schedule
import pywhatkit
import mysql.connector as mysql

def connect_to_db():
     return mysql.connect(user='root', password='your_db_password', host='Your-host', port=3306, database='your_db_name')#host can be localhost
    # cursor=conn.cursor()

def send_message(number,message):
    now = datetime.now()
    scheduled_time = now + timedelta(minutes=2)  # Schedule 2 minutes from now
    hour, minute = scheduled_time.hour, scheduled_time.minute

    print(f"Scheduling message to {number} at {hour}:{minute:02d}")
    pywhatkit.sendwhatmsg(number, message, hour, minute)
    time.sleep(60) 


def check_birthday():
    try:
        conn=connect_to_db()
        print('Connected to database Successfully')
        cursor=conn.cursor(dictionary=True)
    except Exception as e:
        print("Error occured in database = ",e)
    
    today=datetime.now().strftime("%m-%d")
    print(today)
    try:
        cursor.execute(
        'SELECT name,number,message FROM whatauto WHERE DATE(date) = CURDATE()'
        )
        results=cursor.fetchall()
        print('Results = ',results)
        if results:
            for idx, result in enumerate(results, start=1):
                
                print('sending',idx,'message')
                message=f"{result['message']} {result['name']} . May God Bless You"
                
                send_message(result['number'],message)
                i+=1
            print('Today\'s birthday wishes have been sent' )
                
        else:
            print("No Birthday Found on Today")   
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        
schedule.every().day.at("00:01").do(check_birthday)

print("Birthday check scheduled, Waiting for midnight...")
while True:
    schedule.run_pending()
    time.sleep(20)
