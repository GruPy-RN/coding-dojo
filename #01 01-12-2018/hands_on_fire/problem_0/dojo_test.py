import pytest
from dojo_solution import count_users

def test_std_file_5_users():
    assert count_users("input.txt") == 5