
# 📚 Library Management System

This is a simple **console-based Library Management System** written in Python. It allows students to **borrow** and **return** books from a central library.

---

## ✨ Features

- 🧾 **View Available Books**  
  Check which books are available and how many copies remain. Out-of-stock books are marked clearly.

- 🙋‍♂️ **Student Profile**  
  Each student gets a profile that keeps track of all borrowed books.

- 📥 **Borrow Books**  
  Students can request to borrow a book (if available), and it updates the library stock automatically.

- 📤 **Return Books**  
  Students can return borrowed books, which updates both their profile and the library’s stock.

- 📊 **Real-time Inventory Display**  
  The system shows the number of copies available with a visual marker:
  - `*` Available
  - `#` Out of Stock

- 🧠 **Memory of Borrowed Books**  
  Remembers how many books each student has borrowed — and ensures they can’t return books they never took.

---

## ⚙️ How It Works

1. 🏫 The library starts with a predefined list of books and quantities.
2. 👨‍🎓 A student logs in by providing their name.
3. 📚 Through a menu-driven interface, the student can:
   - View library stock
   - See their borrowed books
   - Borrow a book
   - Return a book
4. 🔁 The menu repeats until the student chooses to exit.

---

## 📦 Dependencies

✅ **Only Python is needed!**  
This system is built using **standard Python**, so no external libraries or installations are required.

- ✅ Python 3.x

### Run the script:

```bash
python library_management.py
```

---

## 📝 Notes

- All **book names** are automatically **converted to uppercase** for consistency.
- ⚠️ Be careful with typos — the system won't recognize books that are not exactly named (even casing matters when stored).
- Borrowing or returning invalid books will trigger appropriate warnings.
- The system is built for **one student at a time**, but can be extended to support multiple users more robustly.

---

Made with ❤️ using Python.
