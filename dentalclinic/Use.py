from tkinter import *

FONT = ('Tahoma', 12,'bold')
padingx = 10
padingy = 10

def center(root):
    root.resizable(False,False)
    width, height = 700, 500
    w=root.winfo_screenwidth()
    h=root.winfo_screenheight()
    x=int((w-width)/2)
    y=int((h-height)/2)
    root.geometry(f"{width}x{height}+{x}+{y}")