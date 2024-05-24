# File: tests/test_gratitudes.py
from lib.gratitudes import *


def test_one_thing():
    myGratitude = Gratitudes()
    myGratitude.add('good health')
    result = myGratitude.format()
    assert result == "Be grateful for: good health"   


def test_null_case():
    
    myGratitude = Gratitudes()
    result = myGratitude.format()
    assert result == "Be grateful for: "   


"""
This is some text which can be ignored

"""    

def test_two_things():
    myGratitude = Gratitudes()
    myGratitude.add('good health')
    myGratitude.add('warm food')
    result = myGratitude.format()
    assert result == "Be grateful for: good health, warm food"   


def test_three_things():
    myGratitude = Gratitudes()
    myGratitude.add('good health')
    myGratitude.add('warm food')
    myGratitude.add('friends to speak with')
    result = myGratitude.format()
    assert result == "Be grateful for: good health, warm food, friends to speak with"   
