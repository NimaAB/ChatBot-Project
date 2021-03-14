import random
from bot.bots import *
from models.message import Message

# Global variables
BOTS = ["Alice", "Bob", "Dora", "Chuck"]


def peak_bot(person: str, message: Message) -> Message:
    switch = {
        "Alice": alice(message),
        "Bob": bob(message),
        "Dora": dora(message),
        "Chuck": chuck(message)
    }
    return switch[person]
