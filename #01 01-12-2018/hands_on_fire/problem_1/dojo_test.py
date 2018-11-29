import pytest 
from dojo_solution import count_time

def test_1_person():
    assert count_time(input_file="input_1.txt") == 10
