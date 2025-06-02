
# 🗣️ RoboSpeaker 1.1

Welcome to **RoboSpeaker 1.1** — a simple voice-based script created using PowerShell and Python. It uses your system's **text-to-speech** capability to pronounce any sentence you provide.

---

## ✨ Features

- 🔊 **Text-to-Speech**  
  Speaks out whatever text you input using the built-in Windows voice engine.

- ⌨️ **Live Input**  
  Continuously asks the user for new lines to pronounce.

- 🧠 **Simple & Lightweight**  
  No external Python libraries needed — works directly with Windows' PowerShell.

---

## ⚙️ How It Works

1. Takes input from the user via the terminal.
2. Executes a PowerShell command using `os.system()` that speaks the input aloud.
3. Runs in an infinite loop for continuous interaction.

---

## 📦 Dependencies

- ✅ Python 3.x
- ✅ Windows OS (PowerShell)
- ❌ No external Python packages needed

---

## ▶️ How to Use

1. Save the script (e.g., as `robospeaker.py`).
2. Open a **Windows terminal or command prompt**.
3. Run the script:

```bash
python robospeaker.py
```

4. Type anything — and hear your computer speak it aloud!

---

## ⚠️ Notes

- This script **only works on Windows** because it uses PowerShell and the `System.Speech` namespace.
- You can stop it anytime with `Ctrl+C`.

---

Made with ❤️ using Python and PowerShell.
