from harvest import (
    make_melon_type_lookup,
    make_melon_types,
    Melon,
    get_sellability_report,
)

melon_types = make_melon_types() # list with MelonTypes
melons_by_id = make_melon_type_lookup(melon_types) # dictionary


def melon_data(textfile):
    """Opens and loops over the file, 
    creating a melon object for each line of the file"""

    melons_from_file = []

    melons_log = open(textfile)
    for line in melons_log:
        attributes = line.rstrip().split(" ")
        shape_rating = attributes[1]
        color_rating = attributes[3]
        melon_type_code = attributes[5] # MelonType.code
        harvested_by = attributes[8]
        harvested_from = attributes[11]


        melons_from_file.append(
            Melon(
            melon_type = melons_by_id.get(melon_type_code),
            shape_rating = int(shape_rating), 
            color_rating = int(color_rating), 
            harvested_from = harvested_from, 
            harvested_by = harvested_by)
        )
        
    return melons_from_file

melons_from_file = melon_data('harvest_log.txt')
get_sellability_report(melons_from_file)