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
        "Bob": bob(message),
        "Dora": dora(message),
        "Chuck": chuck(message),
    }
    return switch[name]
