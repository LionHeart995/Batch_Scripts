import pyautogui
import ctypes
import time
import random

# Prevent the computer from going to sleep
ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)  # Prevent sleep and screen saver

# Move the mouse pointer every second
while True:
    try:
        # Generate random x and y coordinates for mouse movement
        x = random.randint(-50, 50)
        y = random.randint(-50, 50)

        # Move the mouse to a new position
        try:
            pyautogui.move(x, y, duration=0.2)
        except pyautogui.FailSafeException:
            # Handle the exception here, e.g., log an error message.
            pyautogui.FAILSAFE = False

        print("CAUTION:\tSTRICTLY PROHIBITED TO POWER DOWN OR INTERACT WITH THE SYSTEM\n")

        # Wait for a second
        time.sleep(5)
    except KeyboardInterrupt:
        break
