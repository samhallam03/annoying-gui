from tkinter import *


class Calculator(Frame):
    def __init__(self, calc):
        Frame.__init__(self, calc)
        self.calc = calc
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        # this will be where the annoying answer will be shown
        self.answer = StringVar()
        self.answer.set("the text hasn't changed")
        self.ans_label = Label(self, textvariable=self.answer)
        self.ans_label.pack()

        self.change = Button(self, text="Change text", command=self.change_text)
        self.change.pack()

    def change_text(self):
        self.answer.set("the text changed...")