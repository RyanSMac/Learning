# A file for defining units
from pgzero.builtins import Actor
import Weapons


class Unit:
    def __init__(self, name, hp, weapons, movement_value, quantity, def_colour, value, state, action_value,
                 action_taken, locked):
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
        self.locked = locked


stormtrooper1 = Unit("Stormtrooper", 1, Weapons.st_blaster, 2, 5, 0, 50, 0, 2, 2, False)
stormtrooper2 = Unit("Stormtrooper", 1, Weapons.st_blaster, 2, 5, 0, 50, 0, 2, 2, False)
vader = Unit("Vader", 5, Weapons.vader_lightsaber, 1, 1, 1, 50, 0, 2, 2, False)
rebel_trooper1 = Unit("Rebel Squad", 1, Weapons.rs_blaster, 2, 5, 0, 50, 0, 2, 2, False)
rebel_trooper2 = Unit("Rebel Squad", 1, Weapons.rs_blaster, 2, 5, 0, 50, 0, 2, 2, False)
luke_skywalker = Unit("Luke Skywalker", 5, Weapons.luke_lightsaber, 2, 1, 1, 50, 0, 2, 2, False)


def set_up_rebel():
    rebels = [[0] * 2 for i in range(3)]

    rebels[0][0] = Actor('rebels')
    rebels[0][1] = rebel_trooper1

    rebels[1][0] = Actor('rebels')
    rebels[1][1] = rebel_trooper2

    rebels[2][0] = Actor('luke')
    rebels[2][1] = luke_skywalker

    return rebels


def set_up_imperial():
    imperial = [[0] * 2 for i in range(3)]

    imperial[0][0] = Actor('stormtrooper')
    imperial[0][1] = stormtrooper1

    imperial[1][0] = Actor('stormtrooper')
    imperial[1][1] = stormtrooper2

    imperial[2][0] = Actor('vader')
    imperial[2][1] = vader

    return imperial
