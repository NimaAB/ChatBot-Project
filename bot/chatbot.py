import random
from bot.bots import *
from models.message import Message

# Global variables
ACTIONS = ["drink", "eat", "play", "fight", "steal", "write", "sleep", "read"]
BOTS = ["Alice", "Bob", "Dora", "Chuck"]


def peak_bot(person=None) -> Message:
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
