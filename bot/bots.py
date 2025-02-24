from bot.bot_helpers import *  # includes all the helper methods that's used by bots.
from models.message import Message

"""
bots.py includes all the bots that will join the chatroom.
Each bot method is responsible to return a Message object based on their interest.
"""

ACTIONS = {
    "sport": ["run", "swim", "play"],
    "chill": ["watch", "drink"],
    "nerd": ["study", "read", "write", "code"],
    "bad": ["fight", "steal", "smock"]
}


def me() -> Message:
    action_types = ["sport", "chill", "nerd", "bad"]
    action_type = random.choice(action_types)
    action = random.choice(ACTIONS[action_type])
    print(action_type)
    print(action)
    action_and_subject = adding_subject(action)
    contents = [
        f"How about {action_and_subject}?",
        f"What do you folks think about {action_and_subject}?",
        f"{action_and_subject} would be nice to do?"
    ]
    return Message(sender="Host", content=random.choice(contents),
                   action=action, action_and_subject=action_and_subject, action_type=action_type, thoughts=None)


def alice(message: Message) -> Message:
    bot_name = "Alice"
    my_action_type = "sport"
    is_interested = is_bot_interested(message.action_type, my_action_type)
    another_choice = adding_subject(random.choice(ACTIONS[my_action_type]))

    contents = {
        'interested': [
            f"Yes, I am in.",
            f"{message.action_and_subject} is my favourite thing.",
        ],
        'not_interested': [
            f"That one isn't fair, I would like {another_choice}",
            f"I am sorry! But I have some other stuff todo.",
        ],
        'thoughts': [
            f"(I am not interested at all!)",
            f"(I am dont like it, but okay I will join)",
            f"(Hell yes!)"
        ]
    }

    content = content_choice(is_interested, contents)
    return Message(sender=bot_name, content=content)


def bob(message: Message) -> Message:
    bot_name = "Bob"
    my_action_type = "chill"
    is_interested = is_bot_interested(message.action_type, my_action_type)

    contents = {
        'interested': [
            f"Yes, let's do it!",
            f"{message.action_and_subject}, WOW I can't wait for it!",
        ],
        'not_interested': [
            f"What?! we had other plans, didn't we?",
            f"{message.action_and_subject} isn't my thing, you have a great time!",
        ],
        'thoughts': [
            "(I am not interested at all!)",
            "(I dont like it, but okay I will join)",
            "(yeah, i will join!)"
        ]
    }
    content = content_choice(is_interested, contents)
    return Message(sender=bot_name, content=content)


def dora(message: Message) -> Message:
    bot_name = "Dora"
    my_action_type = "nerd"
    is_interested = is_bot_interested(message.action_type, my_action_type)
    another_choice = adding_subject(random.choice(ACTIONS[my_action_type]))

    my_content = "I am in."
    if message.action == "nerd":
        my_content = f"what a good choice {message.action_and_subject}?! let's go for it."

    contents = {
        "interested": [
            my_content,
        ],
        "not_interested": [
            f"That one isn't fair, I would like {another_choice}.",
            "I have lots of homework folks, you have fun.",
        ],
        "thoughts": [
            "(I have lots of home work todo!)",
            "(I am dont like it, but okay I will join)",
            "(Hell yes!)"
        ]
    }

    content = content_choice(is_interested, contents)
    return Message(sender=bot_name, content=content)


def chuck(message: Message) -> Message:
    bot_name = "Chuck"
    my_action_type = "bad"
    is_interested = is_bot_interested(message.action_type, my_action_type)
    another_choice = adding_subject(random.choice(ACTIONS[my_action_type]))

    contents = {
        "interested": [
            f"Yeah, my folks let's go for it!",
            f"{message.action_and_subject} is so fun folks, let's go!",
        ],
        "not_interested": [
            f"That is boring, what about {another_choice}?",
            "Sorry! I am not available!",
        ],
        "thoughts": [
            f"({message.action_and_subject} sucks!)",
            f"({message.action_and_subject} isn't my thing, but okay I will join them)",
            "(Hell yes!)"
        ]
    }

    content = content_choice(is_interested, contents)
    return Message(sender=bot_name, content=content)
