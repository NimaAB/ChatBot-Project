import random
from models.person import Person

"""
p1 = Person(name="Nima", address=('123', 22), connection="connection1")
p2 = Person(name="Na", address=('124', 23), connection="connection2")
p3 = Person(name="Ba", address=('125', 24), connection="connection3")

persons = {}
persons[1] = p1
persons[2] = p2
persons[3] = p3

print(persons[1])
print(len(persons))
"""

action = random.choice(["work", "play", "eat", "cry", "sleep", "fight"])
name = "NIMA  hellO HeleleE lEl"
new_name = name.title()
print(new_name)
