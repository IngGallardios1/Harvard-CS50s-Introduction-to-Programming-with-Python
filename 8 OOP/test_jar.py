from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(10) 
    assert str(jar) == "🍪"
    jar.withdraw(1)
    assert str(jar) == ""


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(4) 
    assert jar.size == 5
    jar.deposit(7)
    assert jar.size == 12


def test_withdraw():
    jar = Jar(12, 12)
    jar.withdraw(1)
    assert jar.size == 11
    jar.withdraw(4) 
    assert jar.size == 7
    jar.withdraw(7) 
    assert jar.size == 0