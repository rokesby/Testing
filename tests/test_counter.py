# File: tests/counter.py
from lib.counter import Counter

def test_counter_initially_reports_zero():
    myCounter = Counter()
    assert myCounter.report() ==  "Counted to 0 so far."
    

def test_counter_first_increment():
    myCounter = Counter()
    myCounter.add(1)
    assert myCounter.report() ==  "Counted to 1 so far."

def test_counter_first_increment():
    myCounter = Counter()
    myCounter.add(1)
    myCounter.add(1)
    assert myCounter.report() ==  "Counted to 2 so far."


def test_counter_more_increments():
    myCounter = Counter()
    myCounter.add(1)
    myCounter.add(1)
    myCounter.add(100)
    assert myCounter.report() ==  "Counted to 102 so far."