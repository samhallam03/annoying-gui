from tkinter import *


class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.hello = Label(self, text="This GUI will annoy you!")
        self.hello.pack()

    
root = Tk()
app = App(root)
app.mainloop()