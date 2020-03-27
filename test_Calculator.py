from Calculator import Calculator

def test_add_empty_returns_zero():
    assert Calculator().Add("") == 0

def test_add_single_number():
    assert Calculator().Add(1) == 1