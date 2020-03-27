from Calculator import Calculator

def test_add_empty_returns_zero():
    assert Calculator().Add("") == 0

def test_add_single_number():
    assert Calculator().Add("1") == 1

def test_add_two_numbers():
    assert Calculator().Add("1,2") == 3

def test_add_multiple_numbers():
    assert Calculator().Add("1,2,3,4,5") == 15

# def test_add_with_newlines():
#     assert Calculator().add()