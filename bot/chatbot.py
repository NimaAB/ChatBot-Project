import random
from bot.bots import *
from models.message import Message

# Global variables
ACTIONS = ["drink", "eat", "play", "fight", "steal", "code", "write", "sleep", "swim", "read"]
BOTS = ["Alice", "Bob", "Dora", "Chuck"]


def peak_bot(person=None) -> Message:
    """
    This will method will take in a name as a String.
    And if the name not belongs to any of the bots, then it will
    randomly choose one of them. And, other way. At the end it will return
    a Message Object where is it sender will be the chosen bot.
    :param person: String
    :return: Message Object
    """

    if (person is None) or (person not in BOTS):
        user = random.choice(BOTS)
    else:
        user = person

    action = random.choice(ACTIONS)
    switch = {
        "Alice": alice(action),
        "Bob": bob(action),
        "Dora": dora(action),
        "Chuck": chuck(action)
    }
    return switch[user]
