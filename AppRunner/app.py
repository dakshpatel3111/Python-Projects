import tkinter as tk
import os
from tkinter import filedialog, Text

apps = []

if os.path.isfile('save.txt') :
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps =tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]


def addapp():
    for widget in frame.winfo_children():
        widget.destroy()


    filename = filedialog.askopenfilename(initialdir="/",title="Select File" ,
                                          filetypes=(("executables","*.exe"),("all Files","*.*")))
    apps.append(filename)
    print(filename)

    for app in apps:
        label = tk.Label(frame, text=app,bg ="gray")
        label.pack()


def runapps():
    for app in apps:
        os.startfile(app)


root = tk.Tk()

canvas = tk.Canvas(root , height= 600 , width=600,bg="#16A085")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8 ,relheight=0.8 , relx =0.1 ,rely = 0.1)

openapps = tk.Button(root, text="Open App" , padx=10 , pady=5, fg ="white" ,bg="#16A085",command=addapp)
openapps.pack()

runapps = tk.Button(root, text="Run App" , padx=10 , pady=5, fg ="white" ,bg="#16A085" ,command =runapps)
runapps.pack()

for app in apps:
    label = tk.Label(frame, text=app )
    label.pack()

root.mainloop()


with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',' )