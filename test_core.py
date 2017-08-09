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
    inventory = {1: {'Name': 'Crane', 'Price': '40.00\n', 'How Many': '101'}}
    assert core.convert_back(inventory) == '\nCrane, 101, 40.00'


def test_revenue1():
    inventory = {
        'XkEXa': {
            'Id Letters': 'XkEXa',
            'Price': '5.0 ',
            'Name': 'Dr. Crane\'s "A Study In Fear" ',
            'How Many': '1',
            'Current State': 'returned'
        }
    }
    assert core.revenue1(inventory) == 5.0


def test_math_for_receipt():
    assert core.math_for_receipt(2.00, 2) == 4.26


def test_convert_into_string():
    inventory = {
        'XkEXa': {
            'Id Letters': 'XkEXa',
            'Price': '5.0 ',
            'Name': 'Crane',
            'How Many': '1',
            'Current State': 'returned'
        }
    }
    assert core.convert_into_string(
        inventory) == '\nCrane, 5.0 , 1, XkEXa, returned'
