#DO NOT IMPORT ANY FILE

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
    
def deposit_and_rental_fee(price):
    """(float) -> float

    Adds the deposit of the rented item and the
    standard 1.00 rental fee.

    >>> deposit_and_rental_fee(20.00)
    3.0
    >>> deposit_and_rental_fee(0)
    0.0
    >>> deposit_and_rental_fee(-12)
    0.0
    """
    if '-' in str(price):
        return 0.0
    elif '0' == str(price):
        return 0.0

    price1 = price / 10
    return price1 + 1.00


    