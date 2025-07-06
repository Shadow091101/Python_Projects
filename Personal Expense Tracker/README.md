# 💸 Personal Expense Tracker

A powerful yet simple **Personal Expense Tracker** app built using **Tkinter** (for GUI) and **MySQL** (for database storage). This desktop-based application helps you **add**, **view**, **sort**, **filter**, and **export** your personal expenses with ease.

---

## ✨ Features

### 📝 Add Expenses
- Enter **amount** of expense.
- Choose a **category** from options like `Food`, `Travel`, etc. using a dropdown (OptionMenu).
- Select a **date** using a **custom date picker window** (defaults to current date).
- Add a **description** for each expense.

### 👁️ View Expenses
- View all expenses in a **scrollable format**.
- **Sort** expenses by:
  - `Amount` (ascending or descending)
  - `Date` (ascending or descending)
- **Filter** expenses by:
  - `Amount`
  - `Category`
  - *(More filters like month/week coming soon!)*

### 📤 Export to CSV
- One-click **Export** of all expenses to a **CSV file**.

---

## 🛠️ Tech Stack
- **Frontend**: `Tkinter` (Python standard GUI library)
- **Backend/Database**: `MySQL`

---

## 📁 Project Structure

```
├── main.py                  # Main app file
├── db_config.sample.py     # Sample DB credentials file (excluded from Git)
├── README.md               # This file
└── other_source_files/     # Associated GUI, logic, and utility files
```

---

## ⚙️ Setup Instructions
As this folder is inside a repository, it cannot be cloned directly, follow the steps to clone this folder inside Python_Projects repository.

1. Create an empty folder and initialize Git

    ```bash
    mkdir Personal Expense Tracker
    cd Personal Expense Tracker
    git init
    ```

2. Add the remote repository:
    ```bash
    git remote add origin https://github.com/Shadow091101/Python_Projects.git
    ```
3. Enable sparse checkout:
    ```bash
    git config core.sparseCheckout true
    ```

4. Tell Git which folder you want
    ```bash
    echo "Personal Expense Tracker/" >> .git/info/sparse-checkout
    ```

5. Pull only that folder:
    ```bash
    git pull origin main
    ```

6. Install dependencies (if not already installed):
    ```bash
    pip install mysql-connector-python tk
    ```

7. Set up your MySQL database.

8. Create a `db_config.py` file using the template below 👇

---

## 🔐 `db_config.sample.py`

```python
# db_config.sample.py

db_config = {
    "host": "your_host",
    "user": "your_username",
    "password": "your_password"
}
```

> ⚠️ **Note**: `db_config.py` is ignored in `.gitignore` to protect your credentials.

---

## 📦 Dependencies

- Python >= 3.7
- `mysql-connector-python`
- `tkinter` (comes with standard Python)
- MySQL Server (local or remote)

---

## 🧠 Future Plans

- Filter by **month**, **week**
- Graphical analytics
- Edit/delete expenses
- Light/Dark mode toggle

---

## 📃 License

MIT License © 2025

---

> Built with ❤️ and Python