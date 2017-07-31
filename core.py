#DO NOT IMPORT ANY FILE

def CountySalesTax(price):
    """(float) -> float

    Calculates the County Sales Tax of the price.

    >>> CountySalesTax(23.00)
    1.38
    >>> CountySalesTax(0)
    0.0
    >>> CountySalesTax(-23)
    0.0
    """
    if '-' in str(price):
        return 0.0
    elif '0' == str(price):
        return 0.0
    county_tax = 0.06
    return float(price) * county_tax

def StateSalesTax(price):
    """(float) -> float

    Calculates the State Sales Tax of the price.

    >>> StateSalesTax(15.00)
    1.05
    >>> StateSalesTax(0)
    0.0
    >>> StateSalesTax(-15)
    0.0
    """
    if '-' in str(price):
        return 0.0
    elif '0' == str(price):
        return 0.0

    state_tax = 0.07
    return float(price) * state_tax
    
def deposit(price):
    """(float) -> float

    Calculates the deposit of the rented item.

    >>> deposit(20.00)
    '2.0'
    >>> deposit(0)
    0.0
    >>> deposit(-12)
    0.0
    """
    if '-' in str(price):
        return 0.0
    elif '0' == str(price):
        return 0.0
    else:
        price1 = price / 10
        return str(price1)

def rent_price(pricey, deposit):
    """(float, float) -> float

    Adds the rental price
    to the deposit for a total.

    >>> rent_price(1.00, 4.00)
    '5.0'
    >>> rent_price(0, 4.44)
    0.0
    >>> rent_price(-23, 23.33)
    0.0
    """
    if '-' in str(pricey):
        return 0.0
    elif '0' == str(pricey):
        return 0.0
    total = float(deposit) + 1.00
    return str(total)

def convert_back(inventory):
    """[[string(item name), int(quantity)]] -> str
    
    Formats the inventory.
    
    """
    new_inventory = ''
    for item in inventory:
        new_inventory += '\n{}, {}, {:.2f}'.format(item[0], int(item[1]), float(item[2]))
    return new_inventory

def convert_for_history(inventory):
        """[[string(item name), int(quantity)]] -> str
    
        Formats the inventory.
        
        """
        new_inventory = ''
        for item in inventory:
            new_inventory += '\n{}, {}, {:.2f}'.format(item[0], float(item[1]), float(item[2]))
        return new_inventory

def revenue1(log):
    """
    Gives the added revenue of all the money of each purchase in the log.
    """
    print(log)
    revenue = 0.0
    for item in log:
        item[1] = float(item[1])
        revenue += item[1]
    return revenue