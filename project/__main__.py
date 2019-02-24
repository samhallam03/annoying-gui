from tkinter import *


class Application:
    def __init__(self, master):
        self.master = master
        master.title = "Annoying GUI"

        self.label = Label(master, text="This GUI will be annoying.")
        self.label.pack()

root = Tk()
gui = Application(root)
root.mainloop()