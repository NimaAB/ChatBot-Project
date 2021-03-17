from bot.bots import *


def pick_bot(name: str, message: Message) -> Message:
    """
    This methods takes a name and Message object and returns a bot with
    the given name.
    :param name: string
    :param message: Message
    :return: Message
    """
    switch = {
        "Alice": alice(message),
        "alice": alice(message),
        "Bob": bob(message),
        "bob": bob(message),
        "Dora": dora(message),
        "dora": dora(message),
        "Chuck": chuck(message),
        "chuck": chuck(message),
    }
    return switch[name]
