import pyautogui
import time
import threading
from pynput import keyboard

# === CONFIGURATION ===
click_interval = 0.1  # seconds between clicks
click_button = 'left'  # 'left', 'right', or 'middle'

# === GLOBAL STATE ===
clicking = False
program_running = True

def click_loop():
    while program_running:
        if clicking:
            pyautogui.click(button=click_button)
            time.sleep(click_interval)
        else:
            time.sleep(0.1)

def start_clicking():
    global clicking
    clicking = True
    print("✅ Auto-clicking started...")

def stop_clicking():
    global clicking
    clicking = False
    print("🛑 Auto-clicking stopped.")

def on_press(key):
    global program_running

    try:
        if key.char == 's':
            start_clicking()
        elif key.char == 'e':
            stop_clicking()
        elif key.char == 'q':
            program_running = False
            print("🚪 Exiting auto-clicker...")
            return False
    except AttributeError:
        pass

# === RUN THREAD ===
threading.Thread(target=click_loop).start()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()