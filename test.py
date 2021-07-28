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
    
    frame = tk.Frame()
    
    label = tk.Label(
        master=frame, 
        text="Username"
        )
    label.pack()
    
    userEntry = tk.Entry(
        master=frame
        )
    userEntry.pack()
    
    user = userEntry.get()
    
    label = tk.Label(
        master=frame, 
        text="Password"
        )
    label.pack()
    
    passEntry = tk.Entry(
        master=frame
        )
    passEntry.pack()
    
    login = tk.Button(
        master=frame,
        text="Login",
        width=7,
        height=1,
        )
    login.pack()
    
    frame.pack()
    
    close = tk.Button(
        master=frame,
        text="Close",
        width=7,
        height=1,
        command=userEntry.delete(0, 4)
        )
    close.pack()

    window.mainloop()
    return()
    
if __name__ == "__main__":
    main()
