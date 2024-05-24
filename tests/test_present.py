# File: tests/present.py
from lib.present import Present
import pytest

'''
Add contents and try to wrap again.
'''

# Test normal case.
def test_normal_flow():
    myPresent = Present()
    myPresent.wrap("Television set")
    result = myPresent.unwrap()
    assert result == 'Television set'


# Test creation of the class and check that no contents have been wrapped.
def test_wrap_twice():
    myPresent = Present()
    myPresent.wrap("Television set")
    with pytest.raises(Exception) as e:
        myPresent.wrap("Games console")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."


# Try to unwrap a present with no contents
def test_unwrap():
    myPresent = Present()
    with pytest.raises(Exception) as e:
        myPresent.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."


