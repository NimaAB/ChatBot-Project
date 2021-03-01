import sys
import random
from bots import *

# Global variables
ACTIONS = ["drink", "eat", "play", "fight", "steal", "code", "write", "sleep", "swim", "read"]
PERSONS = ["Alice", "Bob", "Dora", "Chuck"]


def peak_person(person=None):
    if (person is None) or (person not in PERSONS):
        person = random.choice(PERSONS)
        return person
    else:
        return person


def peak_bot(person=None):
    person = peak_person(person)
    action = random.choice(ACTIONS)
    switch = {
        "Alice": alice(action),
        "Bob": bob(action),
        "Dora": dora(action),
        "Chuck": chuck(action)
    }
    return switch[person]
