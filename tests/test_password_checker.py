# File: tests/password_checker.py
from lib.password_checker import PasswordChecker
import pytest

'''

'''

# Test happy case.
def test_normal_flow():
    myPassword = PasswordChecker()
    result = myPassword.check("Television set")
    assert result == True

# Test too short a password
def test_too_short():
    myPassword = PasswordChecker()
    with pytest.raises(Exception) as e:
        result = myPassword.check("Tele")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
