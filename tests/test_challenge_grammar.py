# File: tests/challenge_grammar.py
#from lib.challenge_grammar import GrammarStats
from lib.challenge_grammar import *

# Exceptions?

# Add some text which constitutes good grammar.
def check_good():
    myObj = GrammarStats()
    result = GrammarStats.check("Here is some text.")
    assert result == True

# Add some text which constitutes bad grammar.
def check_bad():
    myObj = GrammarStats()
    result = GrammarStats.check("here is some text")
    assert result == False

#  def check(self, text):
# Confirm percentage with no submissions
def check_percentage_1():
    myObj = GrammarStats()
    result = myObj.percentage_good()
    assert result == 0

# Confirm percentage with 1 good submission
def check_percentage_2():
    myObj = GrammarStats()
    result = GrammarStats.check("Here is some text.")
    assert myObj.percentage_good() == 100

# Confirm percentage with 1 bad submission
def check_percentage_3():
    myObj = GrammarStats()
    result = GrammarStats.check("here is some text")
    assert myObj.percentage_good() == 0

# Confirm percentage with 1 good and 1 bad submission
def check_percentage_4():
    myObj = GrammarStats()
    result = GrammarStats.check("here is some text")
    result = GrammarStats.check("There is some text.")
    assert myObj.percentage_good() == 50

'''
This is a multi line comment.
'''


