from lib.check_codeword import *

def test_check_codeword_success():
    result = check_codeword("horse")
    assert result == "Correct! Come in."


def test_check_codeword_partial():
    result = check_codeword("hXXXe")
    assert result == "Close, but nope."


def test_check_codeword_fail():
    result = check_codeword("donkey")
    assert result == "WRONG!"
