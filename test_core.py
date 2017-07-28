import core

def test_CountySalesTax():
    assert core.CountySalesTax(23.00) == 1.61

def test_StateSalesTax():
    assert core.StateSalesTax(15.00) == 1.2

def test_deposit_and_rental_fee():
    assert core.deposit_and_rental_fee(45.00) == 5.5