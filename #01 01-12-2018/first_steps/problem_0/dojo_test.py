import pytest
import contextlib
from io import StringIO
from dojo_solution import print_hello_worlds

def test_1_hello_world():
    temp_stdout = StringIO()
    with contextlib.redirect_stdout(temp_stdout):
        print_hello_worlds()
    output = temp_stdout.getvalue().strip()
    assert output == "Hello world!"