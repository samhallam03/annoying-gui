#!/usr/bin/python
from tkinter import *

from .apps.calc import Calculator


class Home(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("annoying gui")
        self.master.geometry("300x300")
        self.pack()
        
        self.create_widgets()
    
    def create_widgets(self):
        self.title = Label(self, text="annoying gui", font=("Century Gothic", 20))
        self.title.pack()

        self.say_hello = Button(self, text="calculator", width=25, height=2,
            bg="lightgreen", command=self.open_calculator)
        self.say_hello.pack()

    def open_calculator(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("annoying calculator")
        self.newWindow.geometry("100x100")
        self.app = Calculator(self.newWindow)


def main():
    root = Tk()
    app = Home(root)
    app.mainloop()

if __name__ == '__main__':
    main()