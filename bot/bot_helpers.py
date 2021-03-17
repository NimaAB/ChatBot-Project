import random


def content_choice(is_interested: bool, contents: dict) -> str:
    """
    The method will choose a content:str from the dictionary object that is given
    based on the interest boolean.
    :param is_interested: boolean
    :param contents: dictionary
    :return: string
    """
    if is_interested:
        content = random.choice(contents['interested'])
    else:
        content = random.choice(contents['not_interested'])

    return content


def is_bot_interested(action_type: str, my_action_type: str) -> bool:
    """
    The method will take in to action strings and return true if they are equal,
    other ways it will choose a boolean randomly.
    :param action_type: string
    :param my_action_type: string
    :return: boolean
    """
    if action_type == my_action_type:
        return True  # The bot is interested in the suggestion
    else:
        return random.choice([True, False, False, False])  # the bot is not sure yet.


def change_to_present(verb: str) -> str:
    """
    This method will take in a verb, and changes it's form to present.
    :param verb: string
    :return: string
    """
    verbs_that_get_double_consonant = ["run", "swim"]
    verbs_that_that_miss_e = ["write", "code"]

    if verb in verbs_that_get_double_consonant:
        last_char_of_verb = verb[-1]
        return verb + last_char_of_verb + "ing"
    elif verb in verbs_that_that_miss_e:
        return verb.replace("e", "ing", 1)
    else:
        return verb + "ing"


def adding_subject(action: str) -> str:
    """
    The method takes an action and adds a subject to it,
    if it has any.
    :param action: string
    :return: string
    """
    subjects = {
        "play": ['volleyball', 'football', 'tennis'],
        "watch": ['movie', 'TV', 'theater'],
        "drink": ['beer', 'tea', 'coffee', 'wine'],
        "study": ['math', 'networking', 'database', 'physics'],
        "write": ['essay', 'the rapport'],
        "read": ['novell', 'poem', 'comic book']
    }
    present_form = change_to_present(action)
    if action in subjects:
        return f"{present_form} {random.choice(subjects[action])}"
    else:
        return present_form
