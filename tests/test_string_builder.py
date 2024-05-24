# File: tests/string_builder.py
from lib.String_builder import StringBuilder

def test_string_initially_reports_zero():
    mySB = StringBuilder()
    assert mySB.output() ==  ""
    
def test_string_first_increment():
    mySB = StringBuilder()
    mySB.add('rokesby')
    assert mySB.size() ==  7

def test_string_second_increment():
    mySB = StringBuilder()
    mySB.add('place')
    assert mySB.size() ==  5

def test_string_second_output():
    mySB = StringBuilder()
    mySB.add('rokesby')
    mySB.add('place')
    assert mySB.output() ==  "rokesbyplace"

