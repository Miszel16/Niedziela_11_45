import funkcje

# - nazwy metod od 'test' (np. test_add)

# python -m <nazwa_modulu> <nazwa_programu>
# python -m pytest test_with_pytest.py -v

def test_add():
    assert funkcje.add(2,4) == 6
    assert not funkcje.add(2,3) == 6
