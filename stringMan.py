import random


switch = {
    "good": ["reading", "writing"],
    "bad": ["fighting", "stealing"]
}


print(random.choice(switch["good"]))
print(random.choice(switch["bad"]))
