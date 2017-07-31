import core, shell
def open_inventory():
    """() -> [[string(item name), int(quantity)]]
    
    Opens the inventory and splits it.
    
    """
    new_inventory1 = []
    with open ('inventory.txt', 'r') as file_2:
        file_2.readline()
        inventory = file_2.readlines()
    for element in inventory:
        item, how_many, price = element.split(', ')
        new_inventory1.append([item.strip(), int(how_many.strip()), float(price.strip())])
    return new_inventory1

def append_history(item, price, how_many):
    '''str, float, float -> str
    
    Adds to the log(history.txt) with every purchase.
    '''
    with open('history.txt', 'a') as file_1:
        file_1.write(item + " , " + str(price)+ " , " + str(how_many) + "\n")

def resupply(inventory):
    """() -> None

    If any item stock is lower than or at 100, restocks to 1000.

    """
    for item in inventory:
        if item[1] <= 100:
            item[1] = 1000

    with open ('inventory.txt', 'w') as file_2:
        new_inventory = core.convert_back(inventory)
        file_2.write(new_inventory)

def open_log(file):
    """() -> [[string](item name), int(quanity)]]
    
    Opens history.txt with every purchase. Shortcut.

    """
    new_inventory = []
    
    with open(file, 'r') as file_3:
        file_3.readline()
        inventory = file_3.readlines()
    for element in inventory:
        item, price, how_many = element.split(', ')
        new_inventory.append([(item.strip()), price.strip(), how_many.strip()])
    return new_inventory

def update_inventory(item, how_many, inventory):
    """
    Updates the inventory with every purchase.
    """
    how_many = int(how_many)
    if item == 'Dr. Crane\'s "A Study In Fear"':
        inventory[0][1] = inventory[0][1] - how_many
    elif item == 'Jervis Tetch\'s "Wonderful Wonderland Fairy Tales!"':
        inventory[1][1] = inventory[1][1] - how_many
    elif item == 'Edward Nygma\'s "Riddles To Blow The Mind...Literally!"':
        inventory[2][1] = inventory[2][1] - how_many
    elif item == 'Bane\'s "Breaking The Bat: It\'s A Snap!"':
        inventory[3][1] = inventory[3][1] - how_many
    elif item == 'Hugo Strange\'s "The Dark History Of The Medical Practice"':
        inventory[4][1] = inventory[4][1] - how_many

    with open ('inventory.txt', 'w') as file_2:
        new_inventory = core.convert_back(inventory)
        file_2.write(new_inventory)