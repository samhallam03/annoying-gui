from tkinter import *


class Calculator(Frame):
    def __init__(self, calc):
        Frame.__init__(self, calc)
        self.calc = calc
        self.pack()