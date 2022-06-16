import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Type Speed Test')

        self.mainframe = ttk.Frame(self, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.text = tk.StringVar()
        self.text_entry = ttk.Entry(self.mainframe, width=10, textvariable=self.text)
        self.text_entry.grid(column=2, row=1, sticky=(W, E))


        # # Create the application variable.
        # self.contents = tk.StringVar()
        # # Set it to some value.
        # self.contents.set("this is a variable")
        # # Tell the entry widget to watch this variable.
        # self.entrythingy["textvariable"] = self.contents
        #
        # # Define a callback for when the user hits return.
        # # It prints the current value of the variable.
        # self.entrythingy.bind('<Key-Return>',
        #                      self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())
