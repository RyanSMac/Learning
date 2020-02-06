class Weapons:
    def __init__(self, name, atk_colour, min_range, max_range, number_dice):
        self.name = name
        self.atk_colour = atk_colour
        self.min_range = min_range
        self.max_range = max_range
        self.number_dice = number_dice


rs_blaster = Weapons("Rebel Blaster", 0, 1, 3, 1)
st_blaster = Weapons("Stormtrooper Blaster", 0, 1, 3, 1)
troop_melee = Weapons("Punch", 0, 1, 1, 1)

vader_lightsaber = Weapons("Vader's Lightsaber", 2, 1, 1, 6)
luke_lightsaber = Weapons("luke's Lightsaber", 2, 1, 1, 6)
