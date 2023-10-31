from ex4 import encryptThis

def test_encryptThis_1():
    assert encryptThis("Hello") == '72olle'

def test_encryptThis_2():
    assert encryptThis("good") == '103doo'

def test_encryptThis_3():
    assert encryptThis("hello world") == '104olle 119drlo'

def test_encryptThis_4():
    assert encryptThis("") == ''

def test_encryptThis_5():
    assert encryptThis("A") == '65'

if __name__ == "__main__":
    test_encryptThis_1()
    test_encryptThis_2()
    test_encryptThis_3()
    test_encryptThis_4()
    test_encryptThis_5()
    print("Todos os testes passaram!")