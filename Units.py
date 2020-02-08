# A file for defining units
from pgzero.builtins import Actor


class Unit:
    def __init__(self, name, hp, weapons, movement_value, quantity, def_colour, value, state, action_value,
                 action_taken):
        self.name = name
        self.hp = hp
        self.weapons = weapons
        self.movement_value = movement_value
        self.quantity = quantity
        self.def_colour = def_colour
        self.value = value
        self.state = state
        self.action_value = action_value
        self.action_taken = action_taken


stormtrooper = Unit("Stormtrooper", 1, 1, 2, 5, 0, 50, 0, 2, 0)
vader = Unit("Vader", 5, 0, 1, 1, 2, 50, 0, 2, 0)

rebel_trooper = Unit("Rebel Squad", 1, 1, 2, 5, 0, 50, 0, 2, 0)
luke_skywalker = Unit("Luke Skywalker", 5, 0, 2, 1, 2, 50, 0, 2, 0)


def set_up_rebel():
    rebels = [[0] * 2 for i in range(3)]

    rebels[0][0] = Actor('rebels')
    rebels[0][1] = rebel_trooper

    rebels[1][0] = Actor('rebels')
    rebels[1][1] = rebel_trooper

    rebels[2][0] = Actor('luke')
    rebels[2][1] = luke_skywalker

    return rebels


def set_up_imperial():
    imperial = [[0] * 2 for i in range(3)]

    imperial[0][0] = Actor('stormtrooper')
    imperial[0][1] = stormtrooper

    imperial[1][0] = Actor('stormtrooper')
    imperial[1][1] = stormtrooper

    imperial[2][0] = Actor('vader')
    imperial[2][1] = vader

    return imperial
