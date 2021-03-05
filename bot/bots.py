from models.message import Message

actions = {
    "sporty": ["run", "bike", "play"],
    "chilly": ["watch", "drink"],
    "nerdy": ["study", "read", "write"],
    "bad": ["fight", "steal", "smock"]
}


# A active person, but she likes other activities that include physical activities.
def alice(action, sender=None):
    bot_name = "Alice"

    return Message(sender=bot_name, content=f"Hello I am Alice! {action}", action=action, action_type="good")


# A chilly guy, that likes watching movies and drinking. In addition, he likes to read and write .
def bob(action, sender=None):
    bot_name = "Bob"
    return Message(sender=bot_name, content=f"Hello I am Bob! {action}", action=action, action_type="good")


# The nerdy girl likes everything about school. Her hobbies aside to school is watching movies and reading.
def dora(action, sender=None):
    bot_name = "Dora"
    return Message(sender=bot_name, content=f"Hello I am Dora! {action}", action=action, action_type="good")


# The bad boy tries everything, but he favourite activities are the bas stuff.
def chuck(action, sender=None):
    bot_name = "Chuck"
    return Message(sender=bot_name, content=f"Hello I am Chuck! {action}", action=action, action_type="good")

