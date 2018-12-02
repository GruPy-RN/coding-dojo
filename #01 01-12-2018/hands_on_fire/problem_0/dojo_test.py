import pytest
from dojo_solution import count_users

def test_std_file_5_users():
    assert count_users("input.txt") == 5

def test_blank_file():
    assert count_users("input.1.txt") == 0

def test_big_file():
    assert count_users("input.2.txt") == 5

def test_very_big():
    assert count_users("verybig.txt") == 500