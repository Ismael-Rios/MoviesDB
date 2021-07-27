#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import tkinter as tk
#sys.path.append('modules/')
#sys.path.append('resources/')

def main():
    window()
    
def window():
    window = tk.Tk()
    
    label = tk.Label(text="Name")
    entry = tk.Entry()
    
    label.pack()
    entry.pack()
    
    login = tk.Button(
        text="Login",
        width=7,
        height=1,
    )
    login.pack()
    
    close = tk.Button(
        text="Close",
        width=7,
        height=1,
    )
    close.pack()

    window.mainloop()
    return()
    
if __name__ == "__main__":
    main()
