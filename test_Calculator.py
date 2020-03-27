from Calculator import Calculator

def test_add_empty_returns_zero():
    assert Calculator().Add("") == 0