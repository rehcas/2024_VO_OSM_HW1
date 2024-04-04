from calc import add

#Test Add()
def test_add():
    assert add(1, 1) == 2
    assert add(10, 10) == 100
    assert add(10, -1) == 9
    assert add(100, 100) == 1000
