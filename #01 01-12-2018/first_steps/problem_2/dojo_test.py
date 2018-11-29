import pytest
from dojo_solution import largest_sequence

def test_largest_sequence_until_10():
    assert largest_sequence(5) == (3, 8)
