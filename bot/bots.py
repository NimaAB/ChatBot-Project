from models.message import Message


# First person:
def alice(action):
    return Message(sender="Alice", content=f"Hello I am Alice! {action}", action=action, action_type="good")


# second person:
def bob(action):
    return Message(sender="Bob", content=f"Hello I am Bob! {action}", action=action, action_type="good")


# third person:
def dora(action):
    return Message(sender="Dora", content=f"Hello I am Dora! {action}", action=action, action_type="good")


# forth person:
def chuck(action):
    return Message(sender="Chuck", content=f"Hello I am Chuck! {action}", action=action, action_type="good")

