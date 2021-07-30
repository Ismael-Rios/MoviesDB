# -*- coding: utf-8 -*-

import sys
import tkinter as tk

from modules.md5 import *

def login():
    def send():
        userName = userEntry.get()
        userPass = passEntry.get()
        
        hash = md5(userName, userPass)
        print(hash)
        
    def close():
        window.destroy()

    window = tk.Tk()
    
    loginFrame = tk.Frame()
    loginFrame.pack()
    
    userLabel = tk.Label(
        master=loginFrame, 
        text="Username"
    )
    userLabel.pack()
    
    userEntry = tk.Entry(
        master=loginFrame
    )
    userEntry.pack()
    
    passLabel = tk.Label(
        master=loginFrame, 
        text="Password"
    )
    passLabel.pack()
    
    passEntry = tk.Entry(
        master=loginFrame
    )
    passEntry.pack()
    
    loginButton = tk.Button(
        master=loginFrame,
        text="Login",
        width=7,
        height=1,
        command=send,
    )
    loginButton.pack()
    
    closeButton = tk.Button(
        master=loginFrame,
        text="Close",
        width=7,
        height=1,
        command=close,
    )
    closeButton.pack()
    
    window.mainloop()
    return()
