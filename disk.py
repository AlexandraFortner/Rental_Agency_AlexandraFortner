import core


def open_inventory():
    """() -> [[string(item name), int(quantity)]]
    
    Opens the inventory and splits it.
    
    """
    count = 0
    new_inventory1 = {}
    with open('inventory.txt', 'r') as file_2:
        file_2.readline()
        inventory = file_2.readlines()
    for element in inventory:
        count += 1
        item, how_many, price = element.split(', ')
        new_inventory1[count] = {
            'Number': count,
            'Name': item,
            'How Many': how_many,
            'Price': price
        }
        # .append([item.strip(), int(how_many.strip()), float(price.strip())])
    return new_inventory1


def append_history(item, price, how_many, id_letters):
    '''str, float, float -> str
    
    Adds to the log(history.txt) with every purchase.
    '''
    with open('history.txt', 'a') as file_1:
        file_1.write('\n' + item + " , " + str(price) + " , " + str(how_many) +
                     ", " + str(id_letters))


def resupply(inventory):
    """() -> None

    If any item stock is lower than or at 100, restocks to 1000.

    """
    for item in inventory:
        if int(inventory[item]['How Many']) <= 10:
            inventory[item]['How Many'] = 100
    with open('inventory.txt', 'w') as file_2:
        new_inventory = core.convert_back(inventory)
        file_2.write(new_inventory)


def open_log(file):
    """() -> [[string](item name), int(quanity)]]
    Opens history.txt with every purchase. Shortcut.
    """
    new_inventory = {}
    with open(file, 'r') as file_3:
        file_3.readline()
        inventory = file_3.readlines()
    for element in inventory:
        item, price, how_many, id_letters = element.split(', ')
        new_inventory[id_letters.strip()] = {
            'Name': item,
            'Price': price,
            'How Many': how_many,
            'Id Letters': id_letters.strip()
        }
        # .append([(item.strip()), float(price.strip()), how_many.strip(), id_letters.strip()])
    return new_inventory


def update_inventory(item, how_many1, inventory, s):
    """
    Updates the inventory to subtract how_many with every rent.
    """
    how_many = int(how_many1)
    inventory[int(s)][
        'How Many'] = int(inventory[int(s)]['How Many']) - how_many
    with open('inventory.txt', 'w') as file_2:
        new_inventory = core.convert_back(inventory)
        file_2.write(new_inventory)


def update_inventory_returning(item, how_many, inventory, s):
    """
    Updates the inventory to add from returning it.
    """
    how_many = int(how_many1)
    inventory[int(s)][
        'How Many'] = int(inventory[int(s)]['How Many']) + how_many
    with open('inventory.txt', 'w') as file_2:
        new_inventory = core.convert_back(inventory)
        file_2.write(new_inventory)


def returning_update_history(log):
    """
    When customer is returning audio file with
    their specific inputted code, update the history.
    """

    with open('history.txt', 'w') as file:
        file.write(log)