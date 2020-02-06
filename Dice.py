import random


def roll(x):
    return random.randrange(x)


def roll_white_dice(x):

    hit = 0

    for dice in range(x):
        if roll(7) > 4:
            hit += 1

    return hit


def roll_black_dice(x):
    hit = 0

    for dice in range(x):
        if roll(7) > 2:
            hit += 1

    return hit


def roll_red_dice(x):
    hit = 0

    for dice in range(x):
        if roll(7) > 0:
            hit += 1

    return hit
