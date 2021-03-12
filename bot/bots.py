from models.message import Message
import random

actions = {
    "sport": ["run", "swim", "play"],
    "chill": ["watch", "drink"],
    "nerd": ["study", "read", "write"],
    "bad": ["fight", "steal", "smock"]
}


def me():
    action_types = ["sport", "chill", "nerd", "bad"]
    action_type = random.choice(action_types)
    action = random.choice(actions[action_type])
    action_and_subject = adding_subject(action)
    contents = [
        f"How about {action_and_subject}?",
        f"What do you thing about {action_and_subject} for today?"
    ]
    return Message(sender="HOST", content=random.choice(contents), action=action, action_type=action_type)


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


def adding_subject(action) -> str:
    if action == 'play':
        return f"{action}ing {random.choice(['volleyball', 'football', 'tennis'])}"
    elif action == 'watch':
        return f"{action}ing {random.choice(['movie', 'TV', 'theater'])}"
    elif action == 'drink':
        return f"{action}ing some {random.choice(['beer', 'tea', 'coffee', 'wine'])}"
    else:
        return f"{action}ing"
