# ✅ Auto Clicker Script (Python)

A simple, lightweight Python-based auto-clicker that uses `pyautogui` and `pynput` to automate mouse clicking based on keystrokes.

---

## ✨ Features

- ✅ Start/Stop auto-clicking using keyboard keys  
- ✅ Cross-platform support (macOS, Windows, Linux)  
- ✅ Configurable click speed and mouse button  
- ✅ Built with clean, readable Python code  
- ✅ No GUI dependencies or bloat  

---

## 🛠 How It Works

| Key | Action              |
|-----|---------------------|
| `s` | Start auto-clicking |
| `e` | Stop auto-clicking  |
| `q` | Quit the program    |

> Clicking occurs at the current mouse position at a set interval (default: `0.1` seconds).

---

## 📦 Requirements

To install all necessary dependencies:

```bash
pip install -r requirements.txt
```

---

## 🛡 macOS Accessibility Setup

If you're using macOS, you must **grant accessibility permissions** to allow the script to control your mouse and monitor keystrokes. This is a required step for full functionality.

### ✅ Final Setup Steps for macOS:

1. **Open System Settings**  
   Click the  Apple icon → **System Settings**

2. **Go to**:  
   `Privacy & Security` → `Accessibility`

3. **Add the following apps**:  
   - **Visual Studio Code**  
   - **Terminal** (or **iTerm** if you're using it)

4. **Enable permissions**  
   - Toggle both apps **ON** (✔️)

5. **Unlock settings if needed**  
   - Click the 🔒 lock icon and enter your password

6. **Restart**  
   - Quit and reopen both **VS Code** and **Terminal**

Once done, rerun:

```bash
python main.py
```

> Without this step, keystroke detection will not work due to macOS security restrictions.

---
