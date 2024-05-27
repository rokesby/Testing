from lib.grammar import *

def check_good():
    myObj = GrammarStats()
    result = GrammarStats.check("Here is some text.")
    assert result == True
