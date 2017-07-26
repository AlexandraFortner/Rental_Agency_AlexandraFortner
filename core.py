#DO NOT IMPORT ANY FILE

def pretty_menu(list_strings):
    """[strings] -> str"""
    message = list_strings

    return message

def make_pretty(inventory):
    stringy = ''
    for item in inventory:
       stringy += "\n {:<60}{:>40}".format(item[0], "Stocked Inventory: " + str(item[1]))
    return stringy + '\n\n -'