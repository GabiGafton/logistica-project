import tkinter
import time
from tkinter import ttk

root = tkinter.Tk()

def start():

    for k in range(1, 11):
        progress_var.set(k)
        print("STEP", k)
        k += 1
        time.sleep(1)
        root.update_idletasks()

b1 = tkinter.Button(root, text="START", command=start)
b1.pack(side="left")

progress_var = tkinter.IntVar()

pb = ttk.Progressbar(root, orient="horizontal",
                     length=200, maximum=10,
                     mode="determinate",
                     var=progress_var)
pb.pack(side="left")

pb["value"] = 0

root.mainloop()