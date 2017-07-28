import core

def test_CountySalesTax():
    assert core.CountySalesTax(23.00) == 1.61

def test_StateSalesTax():
    assert core.StateSalesTax(15.00) == 1.2

def test_deposit():
    assert core.deposit(-45.00) == 0.0

def test_rent_price():
    assert core.rent_price(0.0, 12) == '13.0'