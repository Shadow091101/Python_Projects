
# Birthday Message Automation

This repository contains two Python scripts designed to automate sending personalized birthday messages via WhatsApp. The system connects to a MySQL database to store birthday details and sends messages to contacts on their special day using the `pywhatkit` library. The application also offers an interface for users to easily input and save birthday information.

## Files

### 1. **`saving_birthday.py`**
This script provides an interface for users to input and save birthday details into the MySQL database. Users can store the name, birthdate, WhatsApp number (including country code), and a custom message for each person.

- **Features**:
  - Input validation for date, name, message, and phone number.
  - Save birthdays to a MySQL database (`whatauto`).
  - Option to exit the program.

### 2. **`sending_message.py`**
This script automates the process of sending birthday messages. It checks the database every day and sends personalized WhatsApp messages at a scheduled time.

- **Features**:
  - Retrieves birthday details from the database.
  - Sends WhatsApp messages using `pywhatkit` at a scheduled time.
  - Supports sending messages at intervals to avoid conflicts.

## Requirements

- Python 3.x
- MySQL Server (locally or cloud-based)
- Required Python Libraries:
  - `pywhatkit`
  - `schedule`
  - `mysql-connector-python`

To install the required Python libraries, use:

```bash
pip install pywhatkit schedule mysql-connector-python
```

## Setup

1. **MySQL Setup**:
   - Create a MySQL database called `whatauto`.
   - Create a table called `whatauto` with the following columns:
     ```sql
     CREATE TABLE whatauto (
         name VARCHAR(255),
         number VARCHAR(20),
         date DATE,
         message TEXT
     );
     ```

2. **Configure MySQL Connection**:
   - Edit the `connect_to_db()` function in both scripts to match your local MySQL connection details (username, password, host, etc.).

3. **Run the Scripts**:
   - Run `saving_birthday.py` to save birthdays to the database.
   - Run `sending_message.py` to automate sending birthday messages at the scheduled time.

   Example:

   ```bash
   python saving_birthday.py
   python sending_message.py
   ```

   The `sending_message.py` script will automatically check for birthdays and send messages according to the schedule.

## Features & Improvements

- **Automation**: The system sends birthday wishes on time, reducing the need for manual reminders.
- **Personalization**: Custom messages can be sent with each birthday wish.
- **Scheduling**: Messages are sent at a specific time, ensuring timely delivery.
- **Improvement Suggestions**:
  - **Cloud Integration**: Sync data across devices by using a cloud database (e.g., Firebase or AWS RDS).
  - **GUI Interface**: Replace the terminal-based interface with a GUI for easier use.
  - **Error Handling**: Improve the retry logic for message failures or database connection issues.

## Usage When Offline

- **MySQL Database**: Ensure MySQL is installed locally, and the database is accessible even when offline.
- **Library Installation**: Install libraries offline by downloading `.whl` files and transferring them between devices.
- **Offline Testing**: You can test saving birthdays in the database and check the scheduling functionality without an internet connection. Sending messages will require an internet connection.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
