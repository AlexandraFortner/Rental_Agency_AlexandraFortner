import core

def open_inventory():
    """() -> [[string(item name), int(quantity)]]
    
    Opens the inventory and splits it.
    
    """
    new_inventory = []
    with open ('inventory.txt', 'r') as file_2:
        file_2.readline()
        inventory = file_2.readlines()
    for element in inventory:
        item, how_many, price = element.split(', ')
        new_inventory.append([item.strip(), int(how_many.strip()), float(price.strip())])
    return new_inventory

def append_log(item, price, how_many):
    '''str, float, float -> str
    
    Adds to the log with every purchase.
    '''
    with open('history.txt', 'a') as file_1:
        file_1.write(item + " , " + str(price)+ " , " + str(how_many) + "\n")

def resupply(item, inventory):
    """() -> None

    If a certain item stock is lower than or at 100, restocks to 1000.

    """

    if item == '1. Dr. Crane\'s "A Study In Fear"':
        if inventory[0][1] <= 100:
            inventory[0][1] = 1000
    elif item == '2. Jervis Tetch\'s "Wonderful Wonderland Fairy Tales!"':
        if inventory[1][1] <= 100:
            inventory[1][1] = 1000
    elif item == '3. Edward Nygma\'s "Riddles To Blow The Mind...Literally!"':
        if inventory[2][1] <= 100:
            inventory[2][1] = 1000
    elif item == '4. Bane\'s "Breaking The Bat: It\'s A Snap!"':
        if inventory[1][1] <= 100:
            inventory[1][1] = 1000
    elif item == '5. Hugo Strange\'s "The Dark History Of The Medical Practice"':
        if inventory[1][1] <= 100:
            inventory[1][1] = 1000
   
  
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
    if item == '1. Dr. Crane\'s "A Study In Fear"':
        inventory[0][1] = inventory[0][1] - how_many
    elif item == '2. Jervis Tetch\'s "Wonderful Wonderland Fairy Tales!"':
        inventory[1][1] = inventory[1][1] - how_many
    elif item == '3. Edward Nygma\'s "Riddles To Blow The Mind...Literally!"':
        inventory[2][1] = inventory[2][1] - how_many
    elif item == '4. Bane\'s "Breaking The Bat: It\'s A Snap!"':
        inventory[2][1] = inventory[2][1] - how_many
    elif item == '5. Hugo Strange\'s "The Dark History Of The Medical Practice"':
        inventory[2][1] = inventory[2][1] - how_many
  

    with open ('inventory.txt', 'w') as file_2:
        new_inventory = core.convert_back(inventory)
        file_2.write(new_inventory)
    