import random
from bot.bots import *
from models.message import Message


def peak_bot(person: str, message: Message) -> Message:
    switch = {
        "Alice": alice(message),
        "Bob": bob(message),
        "Dora": dora(message),
        "Chuck": chuck(message)
    }
    return switch[person]
