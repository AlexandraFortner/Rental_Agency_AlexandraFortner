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
    assert core.convert_back('inventory.txt') == """\n1. Dr. Crane's "A Study In Fear", 29, 40.00\n2. Jervis Tetch's "Wonderful Wonderland Fairy Tales!", 100, 20.00\n3. Edward Nygma's "Riddles To Blow The Mind...Literally!", 99, 30.50\n4. Bane's "Breaking The Bat: It's A Snap!", 100, 36.00\n5. Hugo Strange's "The Dark History Of The Medical Practice", 96, 12.00"""

# def test_revenue1():
#     assert core.revenue1('history.txt') == 55.05