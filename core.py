#DO NOT IMPORT ANY FILE

def pretty_menu(list_strings):
    """[strings] -> str"""
    message = list_strings

    return message

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

def receipt(money):
    """(float) -> float

    prints all information to user in the form of a receipt.

    >>> receipt(2.00)
    <BLANKLINE>
    ___________________________________
    |
    |Original Price:2.0
    |+ State Tax:0.16
    |+ County Tax:0.14
    |Total:2.3000000000000003
    |__________________________________
    <BLANKLINE>
    Here's your receipt! Thank you for shopping with us!
    """
    revenue = 0
    inventory = 0
    print('\n___________________________________\n|\n|Original Price:' + str(money))
    state_taxes = StateSalesTax(money)
    print('|+ State Tax:' + str(state_taxes))
    county_taxes = CountySalesTax(money)
    print('|+ County Tax:' + str(county_taxes))
    total = money + state_taxes + county_taxes
    print('|Total:' + str(total))
    print('|__________________________________\n\nHere\'s your receipt! Thank you for shopping with us!')