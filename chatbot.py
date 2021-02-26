'''
chatbot.py
This code will include four caracters with different roles and personalities.
The user must provide an action among the given actions to start the chatbot.
Actions:
    ["eat","play","fight","steal","code","write","sleep","swim","read"]...
'''

import sys
import random #temporarly
from person import *

#Global variables
ACTIONS = ["drink","eat","play","fight","steal","code","write","sleep","swim","read"]
PERSONS = ["Alice", "Bob", "Dore", "Chuck"]

def peak_person(person=None):
    if (person == None) or (person not in PERSONS):
        person = random.choice(PERSONS)
        return person
    else:
        return person

def peak_method(person=None):
    person = peak_person(person)
    switch():


