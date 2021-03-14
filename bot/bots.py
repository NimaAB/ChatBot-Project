from models.message import Message
import random

actions = {
    "sport": ["run", "swim", "play"],
    "chill": ["watch", "drink"],
    "nerd": ["study", "read", "writ"],
    "bad": ["fight", "steal", "smock"]
}


def me():
    action_types = ["sport", "chill", "nerd", "bad"]
    action_type = random.choice(action_types)
    action = random.choice(actions[action_type])
    action_and_subject = adding_subject(action)
    contents = [
        f"How about {action_and_subject}?",
        f"What do you guys think about {action_and_subject}?",
        f"{action_and_subject} would be nice to do?"
    ]
    return Message(sender="Host", content=random.choice(contents), action=action, action_type=action_type)


# A active person, but she likes other activities that include physical activities.
def alice(message) -> Message:
    bot_name = "Alice"
    my_action_type = "sport"
    is_interested = is_bot_interested(message.action_type, my_action_type)
    another_choice = adding_subject(random.choice(actions[my_action_type]))

    contents = {
        'interested': [
            f"Yes, I am in.",
            f"{message.action_and_subject} is my favourite thing",
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

    content, thought = content_choice(is_interested, contents)
    return Message(sender=bot_name, content=content, thoughts=thought)


# A chilly guy, that likes watching movies and drinking. In addition, he likes to read and write .
def bob(message: Message) -> Message:
    bot_name = "Bob"
    my_action_type = "chill"
    is_interested = is_bot_interested(message.action_type, my_action_type)
    another_choice = adding_subject(random.choice(actions[my_action_type]))

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
            f"(I am not interested at all!)",
            f"(I am dont like it, but okay I will join)",
            f"(Hell yes!)"
        ]
    }
    content, thought = content_choice(is_interested, contents)
    return Message(sender=bot_name, content=content, thoughts=thought)


# The nerdy girl likes everything about school. Her hobbies aside to school is watching movies and reading.
def dora(message: Message) -> Message:
    bot_name = "Dora"
    my_action_type = "nerd"
    is_interested = is_bot_interested(message.action_type, my_action_type)
    another_choice = adding_subject(random.choice(actions[my_action_type]))

    contents = {
        'interested': [
            f"",
            f"{message.action_and_subject}! I can't wait any longer.",
        ],
        'not_interested': [
            f"That one isn't fair, I would like {another_choice}",
            f"I am sorry! But I have some other stuff todo",
        ],
        'thoughts': [
            f"(I am not interested at all!)",
            f"(I am dont like it, but okay I will join)",
            f"(Hell yes!)"
        ]
    }

    content, thought = content_choice(is_interested, contents)
    return Message(sender=bot_name, content=content, thoughts=thought)


# The bad boy tries everything, but he favourite activities are the bas stuff.
def chuck(message: Message) -> Message:
    bot_name = "Chuck"
    my_action_type = "bad"
    is_interested = is_bot_interested(message.action_type, my_action_type)
    another_choice = adding_subject(random.choice(actions[my_action_type]))

    contents = {
        'interested': [
            f"Yeah, my guys let's go for it!",
            f"{message.action_and_subject} is so fun guys, let's go!",
        ],
        'not_interested': [
            f"That is boring, what about {another_choice}?",
            f"",
        ],
        'thoughts': [
            f"({message.action_and_subject} sucks!)",
            f"({message.action_and_subject} isn't my thing, but okay I will join)",
            f"(Hell yes!)"
        ]
    }

    content, thought = content_choice(is_interested, contents)
    return Message(sender=bot_name, content=content, thoughts=thought)


def adding_subject(action: str) -> str:
    subjects = {
        'play': ['volleyball', 'football', 'tennis'],
        'watch': ['movie', 'TV', 'theater'],
        'drink': ['beer', 'tea', 'coffee', 'wine'],
        'study': ['math', 'networking', 'database', 'physics'],
        # more to come...
    }
    if action in subjects:
        return f"{action}ing {random.choice(subjects[action])}"
    else:
        return f"{action}ing"


def is_bot_interested(action_type: str, my_action_type: str) -> bool:
    if action_type == my_action_type:
        return True  # The bot is interested in the suggestion
    else:
        return random.choice([True, False])  # the bot is not sure yet.


def content_choice(is_interested: bool, contents: dict) -> tuple:
    if is_interested:
        content = random.choice(contents['interested'])
        thought = contents['thoughts'][2]
    else:
        content = random.choice(contents['not_interested'])
        thought = random.choice([contents['thoughts'][0], contents['thoughts'][1]])
    return content, thought
