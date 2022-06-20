import random

from user_interface import UserInterface
import json

def create_app():
    """
    Configure a UserInterface with data and return app.
    """
    filepath = './files/word_list.json'
    hundred_words = get_one_hundred_words(filepath)
    app = UserInterface(hundred_words)

    return app


def get_one_hundred_words(filepath: str):
    """
    Set a random selection of 100 words from the given file to a list and return it.
    :param filepath: str
    :return: list
    """
    with open(filepath, 'r') as file:
        word_list = json.loads(file.read())
    words = []
    for _ in range(100):

        rand = random.choice(word_list)
        if len(rand) < 8 and rand.count("\'") == 0:
            words.append(rand)

    return words


if __name__ == '__main__':
    app = create_app()
    app.root.mainloop()
