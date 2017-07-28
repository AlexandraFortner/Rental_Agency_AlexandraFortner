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