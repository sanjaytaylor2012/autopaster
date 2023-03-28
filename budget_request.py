import keyboard
import pyperclip
import time
import pyautogui

# your info here
strings = [["sup", "bro" , "dude", 'ski'], ["whats", "good", "homie"], ["not", "much", "hbu"]]


current_index = 0
current_array = 0


def on_hotkey_press():
    global current_index
    global current_array
    s = strings[current_array][current_index]
    pyperclip.copy(s)
    current_index = (current_index + 1) % len(strings[current_array])
    print(f"Pasting: {s}")
    pyautogui.write(s)
    time.sleep(0.1)


def reset():
    global current_index
    current_index = 0
    print("resetting cycle")
    time.sleep(0.1)

def increment_array():
    global current_array
    global current_index
    current_index = 0
    if current_array == len(strings) - 1:
        current_array = 0
    else:
        current_array += 1
    print("incrementing arrays")
    time.sleep(0.1)

def decrement_array():
    global current_array
    global current_index
    current_index = 0
    if current_array == 0:
        current_array = len(strings) - 1
    else:
        current_array -= 1
    print("decrementing arrays")
    time.sleep(0.1)




pyperclip.copy("")
keyboard.add_hotkey("left arrow", on_hotkey_press)
keyboard.add_hotkey("right arrow", reset)
keyboard.add_hotkey("up arrow", increment_array)
keyboard.add_hotkey("down arrow", decrement_array)






keyboard.wait()
