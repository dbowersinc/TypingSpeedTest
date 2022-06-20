import random
import tkinter as tk
from tkinter import ttk


class UserInterface:
    def __init__(self, word_set):
        self.root = tk.Tk()
        self.root.title('Type Speed Test')

        self.word_set = word_set
        self.displayed_words = [random.choice(self.word_set) for x in range(12)]
        self.current_word = ''
        self.typed_chars = ''
        self.set_current_word(0)
        self.words = tk.StringVar()
        self.typing = tk.StringVar()
        self.update_words()
        self.correct_words = []
        self.incorrect_words = []
        self.total_chars = 0
        self.current_chars = 0
        self.word_index = 0

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.seconds = tk.StringVar()
        self.timer = ttk.Label(self.mainframe, width=10, textvariable=self.seconds)
        self.timer.grid(column=1, row=0, sticky='e')
        self.seconds.set('60')
        self.timer_label = ttk.Label(self.mainframe, width=10, text="Seconds")
        self.timer_label.grid(column=2, row=0, sticky='e')

        self.text_entry = ttk.Entry(self.mainframe, width=30, textvariable=self.typing)
        self.text_entry.grid(columnspan=3, column=0, row=2, sticky=('W', 'E'))

        self.entry_label = ttk.Label(self.mainframe, width=60, textvariable=self.words, padding="5 5 10 10")
        self.entry_label.grid(columnspan=3, column=0, row=1, sticky=('W', 'E'))
        self.root.bind("<Key>", self.key_handler)

    def update_words(self):
        """Convert displayed words list to string, and set StringVar."""
        temp_string = ''
        word_ctr = 0
        for word in self.displayed_words:
            if temp_string == '':
                temp_string = word
                word_ctr = 1
            elif word_ctr <= 4:
                temp_string = f'{temp_string} {word}'
                word_ctr += 1
            else:
                temp_string = f'{temp_string}\n{word}'
                word_ctr = 0
        self.words.set(temp_string)

    def update_displayed(self):
        """Update the displayed words list."""
        del self.displayed_words[0]
        self.displayed_words.append(random.choice(self.word_set))

    def set_current_word(self, index: int):
        self.current_word = self.displayed_words[index]

    def display_results(self):
        self.entry_label.config(state='disabled', width=0)
        word_count = len(self.correct_words)
        incorrect = len(self.incorrect_words)
        results = f'You typed {word_count} words per minute.\n' \
                  f'You missed typed {incorrect} words.'
        self.words.set(results)

    def update_timer(self):
        """Start the timer, and recursively countdown."""
        seconds = int(self.seconds.get())
        if seconds > 0:
            seconds -= 1
            self.seconds.set(str(seconds))
            self.root.after(1000, self.update_timer)
        else:
            self.display_results()

    def next_word(self):
        """Update the display, and setup the next word."""
        self.update_words()
        self.set_current_word(self.word_index)

    def key_handler(self, event):
        """
        Collect the key, and test it against the next character in the current word.
        The space bar updates the current word and adjusts the score depending
        on if the last word typed matches the previous word.
        :param event:
        :return:
        """
        if self.seconds.get() == '60':
            self.update_timer()
        if event.keysym == 'space':
            if self.typed_chars == self.current_word:
                print(self.typed_chars)
                self.correct_words.append(self.current_word)
            else:
                self.incorrect_words.append((self.current_word, self.typed_chars))

            if self.word_index <= 5:
                self.word_index += 1
            else:
                self.update_displayed()
                self.update_words
            # advance display_chars
            # advance total char count
            self.total_chars += 1
            self.typed_chars = ''
            self.next_word()
        else:
            # decorate the character typed on the display screen
            self.typed_chars = self.typed_chars + event.keysym
            self.total_chars += 1



