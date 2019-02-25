#!/usr/bin/python
from tkinter import *

from .apps.calc import Calculator


class Home(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Annoying GUI")
        self.master.geometry("400x400")
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.title = Label(self, text="This GUI will annoy you!")
        self.title.pack()

        self.say_hello = Button(self, text="Open Calculator", command=self.open_calculator)
        self.say_hello.pack()

    def open_calculator(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("Annoying Calculator")
        self.newWindow.geometry("400x400")
        self.app = Calculator(self.newWindow)


def main():
    root = Tk()
    app = Home(root)
    app.mainloop()

if __name__ == '__main__':
    main()