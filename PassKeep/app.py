import tkinter as tk
import os
from tkinter import filedialog, Text


# Functions to save the Entries in Text file
def saveit():
    with open('save.txt', 'a+') as f:
            f.write(e1.get() + ";@USERNAME:")
            f.write(e2.get() + ";@PASSWORD:")
            f.write(e3.get() + ".\n")
    clear()


# Function to clear out the Entries
def clear():
    e1.delete(0,'end')
    e2.delete(0,'end')
    e3.delete(0,'end')


# Root of the Application
root = tk.Tk()
root.title("Password Keeper")
root.geometry("300x100") # Width X height

# Creating Frame named Master
master = tk.Frame(root, bg="#A9CCE3")
master.place(relwidth=1 ,relheight=1)

tk.Label(master, text="Title",bg="#A9CCE3").grid(row=0)
tk.Label(master,text="Username/Emaild",bg="#A9CCE3").grid(row=1)
tk.Label(master,text="Password",bg="#A9CCE3").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)

save = tk.Button(master, text="Save" , padx=10 , pady=5, fg ="white" ,bg="#16A085",command=saveit)
save.grid(row=3)

clearit = tk.Button(master, text="Clear/Reset" , padx=10 , pady=5, fg ="white" ,bg="#16A085",command=clear)
clearit.grid(row=3,column=1)

master.mainloop()






