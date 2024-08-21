import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital clock")

def time():
    string = strftime('%H:%M:%S \n %D/%M/%Y')
    label.config(text= string)
    label.after(1000,time)

label = tk.Label(root,font=('calibri',40,'bold'),background='black',foreground='yellow')
label.pack(anchor='center')
time()

root.mainloop()