
import pytest
from operaciones import suma, resta, multiplicacion, division

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-2, -3) == -5

def test_resta():
    assert resta(5, 3) == 2
    assert resta(-5, -3) == -2

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(-2, -3) == 6

def test_division():
    assert division(6, 3) == 2
    assert division(-6, -3) == 2
    with pytest.raises(ValueError):
        division(5, 0)
