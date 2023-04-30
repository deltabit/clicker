import time
import random
import threading
import tkinter as tk
from tkinter import ttk
import keyboard


class Clicker:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            sleep_time = random.uniform(1, 2)
            time.sleep(sleep_time)
            if self.running:
                keyboard.press_and_release('alt')

    def stop(self):
        self.running = False


class ClickerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Helper")
        self.geometry("300x100")

        self.clicker = Clicker()

        self.start_button = ttk.Button(self, text="Start", command=self.start_clicker)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(self, text="Stop", command=self.stop_clicker, state="disabled")
        self.stop_button.pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def start_clicker(self):
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"

        self.t = threading.Thread(target=self.clicker.start)
        self.t.start()

    def stop_clicker(self):
        self.clicker.stop()
        self.start_button["state"] = "normal"
        self.stop_button["state"] = "disabled"

    def on_closing(self):
        self.clicker.stop()
        self.destroy()


if __name__ == "__main__":
    app = ClickerApp()
    app.mainloop()
