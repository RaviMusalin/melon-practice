############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, name, first_harvest, color, is_seedless, is_bestseller 
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType("musk","Muskmelon",1998,"green",True,True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas","Casaba",2003,"orange",False,False)
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType("cren", "Crenshaw", 1996, "green", False, False)
    cren.add_pairing("proscuitto")
    all_melon_types.append(cren)

    yw = MelonType("yw", "Yellow Watermelon", 2013, "yellow", False, True)
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types
    


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for item in melon_types:
        print(f'{item.name} pairs with') 
        for pair in item.pairings:
            print(f'- {pair}')   


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_code_lookup = {}
    for melon in melon_types:
        melon_code_lookup[melon.code] = melon

    return melon_code_lookup 

print(make_melon_type_lookup(make_melon_types()))

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Needs __init__ and is_sellable methods
    # Melon type: yw
    # Shape rating: 8
    # Color rating: 7
    # Harvested from Field 2
    # Harvested by Sheila
    def __init__(
        self, melon_type, shape_rating, color_rating, harvested_from, harvested_by 
    ):
        self.malon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by
    # shape and color ratings are greater than 5, and it didn’t come from field 3
    def is_sellable(self):
        """a melon is able to be sold if both its shape 
        and color ratings are greater than 5, and it didn’t come from field 3"""
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from != 3:
            return True
        else:
            return False
        
        
def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons = []

    all_melon_types = make_melon_types() # this is a list with all Melon Types

    melon_type_lookup = make_melon_type_lookup(make_melon_types()) # dictionary

    # melon_0 = Melon(melonType, )

    melon_1 = Melon(melon_type_lookup["yw"], 8, 7, 2, "Sheila")
    melons.append(melon_1)
    melon_2 = Melon(melon_type_lookup["yw"], 3, 4, 2, "Sheila")

    melon_3 = Melon(melon_type_lookup["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melon_type_lookup["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melon_type_lookup["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melon_type_lookup["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melon_type_lookup["cren"], 2, 3, 4, "Michael")


    melon_8 = Melon(all_melon_types[0], 6, 7, 4, "Michael")



    melon_9 = Melon(melon_type_lookup["yw"], 7, 10, 3, "Michael")
    


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest

