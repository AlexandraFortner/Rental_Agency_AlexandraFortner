import core

def test_CountySalesTax():
    assert core.CountySalesTax(23.00) == 1.38
    assert core.CountySalesTax(0) == 0.0
    assert core.CountySalesTax(-23) == 0.0

def test_StateSalesTax():
    assert core.StateSalesTax(15.00) == 1.05
    assert core.StateSalesTax(0) == 0.0
    assert core.StateSalesTax(-12) == 0.0

def test_deposit():
    assert core.deposit(-45.00) == 0.0
    assert core.deposit(0) == 0.0
    assert core.deposit(-87) == 0.0
    assert core.deposit(20) == '2.0'

def test_rent_price():
    assert core.rent_price(0.0, 12) == '13.0'
    assert core.rent_price(0, 0) == 0.0
    assert core.rent_price(-23, -1) == 0.0

def test_convert_back():
    inventory = [['Crane', 29, 40.00],['Jervis', 100, 20.00],['Edward', 99, 30.50]]
    assert core.convert_back(inventory) == '\nCrane, 29, 40.00\nJervis, 100, 20.00\nEdward, 99, 30.50'
def test_revenue1():
    inventory = [['Edward Nygma\'s "Riddles To Blow The Mind...Literally!"', 4.05, 1, 'oeEae']]
    assert core.revenue1(inventory) == 4.05
def test_math_for_receipt():
    assert core.math_for_receipt(2.00, 2) == 4.26
def test_convert_into_string():
    inventory = [['Edward', 4.05, 1, 'oeEae'],['Nygma' , 4.05 , 2, 'odYku']]
    assert core.convert_into_string(inventory) == '\nEdward, 4.05, 1, oeEae\nNygma, 4.05, 2, odYku'