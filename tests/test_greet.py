# File: tests/greet.py
from lib.greet import *

def test_greet():
    result = greet("Reza")
    assert result == "Hello, Reza!"