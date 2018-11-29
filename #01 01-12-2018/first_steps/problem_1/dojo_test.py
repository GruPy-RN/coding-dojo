import pytest
from dojo_solution import solve_bhaskara

def test_bhaskara():
    assert solve_bhaskara(1.0, -3, 2) == ('Raiz 1: 2.00000', 'Raiz 2: 1.00000')
