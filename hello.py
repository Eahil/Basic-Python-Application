#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Feet To Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")

root.mainloop()
