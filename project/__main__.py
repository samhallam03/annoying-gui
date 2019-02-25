from tkinter import *


class Home(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.intro = Label(self, text="This GUI will annoy you!")
        self.intro.pack()

        self.say_hello = Button(self, text="Open Calculator", command=self.open_calculator)
        self.say_hello.pack()

    def open_calculator(self):
        self.newWindow = Toplevel(self.master)
        self.app = Calculator(self.newWindow)


class Calculator(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.pack()


def main():
    root = Tk()
    root.title("Annoying GUI")
    app = Home(root)
    app.mainloop()

if __name__ == '__main__':
    main()