# A file for defining units


class Unit:
    def __init__(self, name, hp, weapons, movement_value, quantity, def_colour, value, state):
        self.name = name
        self.hp = hp
        self.weapons = weapons
        self.movement_value = movement_value
        self.quantity = quantity
        self.def_colour = def_colour
        self.value = value
        self.state = state


stormtrooper = Unit("Stormtrooper", 1, 1, 2, 5, 0, 50, 0)
vader = Unit("Vader", 5, 0, 1, 1, 2, 50, 0)

rebel_trooper = Unit("Rebel Squad", 1, 1, 2, 5, 0, 50, 0)
luke_skywalker = Unit("Luke Skywalker", 5, 0, 2, 1, 2, 50, 0)
