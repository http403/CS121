import math
import random


def sorting_hat():
    return random.choice(["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"])


def letter_grade(grade):
    # just little fun
    if grade > 100:
        return "DISQUALIFIED. No cheating"
    if grade >= 90:
        return "A"
    if grade >= 80:
        return "B"
    if grade >= 67:
        return "C"
    return "F"


def coin_flip():
    # print("Coin filp result is heads." if bool(random.getrandbits(1)) else "Coin filp result is tails.")
    # if bool(random.getrandbits(1)):
    if random.randint(0, 1) == 1:
        # print('Coin filp result is tails.')
        print("Coin flip result is tails.")
    else:
        # print('Coin filp result is heads.')
        print("Coin flip result is heads.")


def hypotenuse(a, b):
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))


def emojify(name):
    emojis = {
        "pig": "🐽",
        "rhinoceros": "🦏",
        "pizza": "🍕",
        "balloon": "🎈"
    }
    name = name.lower()
    if name in emojis:
        return emojis[name]
    return name


def weekly_pay(hours_worked, rate):
    if hours_worked > 40:
        print("ALLERT: OVERTIME")
        return 40 * rate + (hours_worked - 40) * rate * 1.5
    else:
        return hours_worked * rate
