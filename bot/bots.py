from models.message import Message


# First person:
def alice(action):
    return Message("Hello I am Alice!", "Alice", "am", "good")


# second person:
def bob(action):
    return Message("Hello I am Bob!", "Bob", "am", "good")


# third person:
def dora(action):
    return Message("Hello I am Dora!", "Dora", "am", "good")


# forth person:
def chuck(action):
    return Message("Hello I am Chuck!", "Chuck", "am", "good")
