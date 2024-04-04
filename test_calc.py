from calc import add, sub, multi, div, mod
#Test add()
def test_add():
	assert add(1, 1) == 2
	assert add(10, 10) == 20
	assert add(10, -1) == 9
	assert add(100, 100) == 200
#Test sub()
def test_sub():
	assert sub(1, 1) == 0
	assert sub(10, 1) == 9
	assert sub(1, -1) == 2
	assert sub(100, -10) == 90
#Test multi()
def test_multi():
	assert multi(1, 1) == 1
	assert multi(1, -1) == -1
	assert multi(10, 10) == 100
	assert multi(100, -10) == -1000
#Test div()
def test_div():
	assert div(1, 1) == 1
	assert div(10, 2) == 5
	assert div(1, 10) == 0.1
	assert div(100, 10) == 10
#Test mod()
def test_mod():
	assert mod(1, 1) == 0
	assert mod(3, 2) == 1
	assert mod(1, 10) == 1
	assert mod(6, -4) == -2
