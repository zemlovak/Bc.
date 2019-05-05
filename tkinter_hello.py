from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, window):
        self.window = window
        window.title("Tkinter")
        self.label = Label(window, text="My first GUI")
        self.label.pack()
        self.hello_button = Button(window, text="Hello world!", command=self.sayhello)
        self.hello_button.pack()
        self.close_button = Button(window, text="       Close      ", command=window.quit)
        self.close_button.pack()

    def sayhello(self):
        print("Hello world!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()