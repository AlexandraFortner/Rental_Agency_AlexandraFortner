#DO NOT IMPORT ANY FILE

def pretty_choice(choice):
    string = ''
    for item in choice:
        string == string.strip('\'')
    return string

def make_pretty(inventory):

    stringy = ''
    for item in inventory:
       stringy += "\n {:<60}{:>40}".format(item[0], "Stocked Inventory: " + str(item[1]))
    return stringy + '\n\n'

def CountySalesTax(price):
    """(float) -> float

    Calculates the County Sales Tax of the price.

    >>> CountySalesTax(23.00)
    1.61
    >>> CountySalesTax(0)
    0.0
    >>> CountySalesTax(-23)
    0.0
    """
    if '-' in str(price):
        return 0.0
    elif '0' == str(price):
        return 0.0

    county_tax = 0.07
    return float(price) * county_tax
    


def StateSalesTax(price):
    """(float) -> float

    Calculates the State Sales Tax of the price.

    >>> StateSalesTax(15.00)
    1.2
    >>> StateSalesTax(0)
    0.0
    >>> StateSalesTax(-15)
    0.0
    """
    if '-' in str(price):
        return 0.0
    elif '0' == str(price):
        return 0.0

    state_tax = 0.08
    return float(price) * state_tax
    
# def deposit():
    