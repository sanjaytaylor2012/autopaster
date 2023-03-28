import keyboard
import pyperclip
import time


# your info here
strings = ["sup", "bro" , "dude", 'ski']

current_index = 0


def on_hotkey_press():
    global current_index
    s = strings[current_index]
    # time.sleep(0.1)
    pyperclip.copy(s)
    current_index = (current_index + 1) % len(strings)
    print(f"Pasting: {s}")
    time.sleep(0.1)


def reset():
    global current_index
    current_index = 0
    print("resetting cycle")
    time.sleep(0.1)

pyperclip.copy("")
keyboard.add_hotkey("ctrl+v", on_hotkey_press)
keyboard.add_hotkey("ctrl+q", reset)


keyboard.wait()
