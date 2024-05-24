# File: tests/report_length.py
from lib.report_length import *

def test_correct_case():
    result = report_length("Reza")
    assert result == "This string was 4 characters long."


def test_null_case():
    result = report_length("")
    assert result == "This string was 0 characters long."   


def test_correct_case2():
    result = report_length("abcdef")
    assert result == "This string was 6 characters long."   