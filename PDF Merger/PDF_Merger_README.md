
# 🧾 PDF Merger Script

This is a simple Python script that **merges all PDF files** in the current directory into a single `merged.pdf` file.

---

## ✨ Features

- 📂 **Auto-Detect PDFs**  
  Automatically finds all `.pdf` files in the current directory.

- 🔗 **Merges All PDFs**  
  Combines them in the order they appear in the directory listing.

- 📄 **Single Output File**  
  Creates a merged PDF file named `merged.pdf`.

---

## ⚙️ How It Works

1. 📁 Lists all files in the current folder.
2. 🔍 Filters for files ending with `.pdf`.
3. 📚 Uses `PyPDF2` to read and merge all detected PDFs.
4. 💾 Outputs the final merged PDF as `merged.pdf`.

---

## 📦 Dependencies

You only need the following Python module:

- `PyPDF2`

### Install it via pip:

```bash
pip install PyPDF2
```

---

## ▶️ How to Use

1. Place the script in the folder containing all your PDF files.
2. Run the script:

```bash
python merge_pdfs.py
```

3. The output file `merged.pdf` will appear in the same folder.

---

## ⚠️ Notes

- Make sure all files you want to merge are **.pdf files**.
- The order of merging depends on the order returned by `os.listdir()`.
- This script reads files in **binary mode** for proper PDF handling.

---

Made with ❤️ to simplify document management.
