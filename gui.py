import tkinter as tk
from tkinter import ttk

# How to create a big label box that has a number of words?
# Use the word file and select a 10 random words to set a string.
# as the person is typing move the cursor to match the current word.
# If there is three lines of text in the label box when it gets to the end of the third line
# take the last line and add it to however many words are short in the required
# set to create the string.
# for n in range(0, 12):
#     string = string + random.choice(words)

# event
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Type Speed Test')

        self.mainframe = ttk.Frame(self, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.text = tk.StringVar()
        self.text_entry = ttk.Entry(self.mainframe, width=10, textvariable=self.text)
        self.text_entry.grid(column=2, row=1, sticky=('W', 'E'))

        self.words = tk.StringVar()
        self.entry_label = ttk.Label(self.mainframe, textvariable=self.words)
        self.entry_label.grid(column=2, row=2, sticky=('W', 'E'))

        self.current_word = ''
        self.words.set('Test')
        self.bind("<Key>", self.key_handler)

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

    def key_handler(self, event):
        if event.keysym == 'space':
            self.current_word = ''
        else:
            self.current_word = self.current_word + event.char
        self.words.set(self.current_word)
        # self.words.set(event.keysym)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())
