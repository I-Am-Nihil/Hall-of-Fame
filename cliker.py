import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

push_button = KeyCode(char='z')
clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(0.3)


def toggle_event(key):
    if key == push_button:
        global clicking
        clicking = not clicking


def main():
    clicking_thread = threading.Thread(target=clicker)
    clicking_thread.start()

    with Listener(on_press=toggle_event) as listener:
        listener.join()


if __name__ == '__main__':
    main()
