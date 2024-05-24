# File: tests/test_count_words.py
from lib.count_words import count_words
# import pytest

# Test complex string
def test_complex_case():
    result = count_words("The quick brown fox jumps over the lazy dog.")
    assert result == 9

# Test simple string
def test_simple_case():
    result = count_words("Hello world")
    assert result == 2

# Test simple string
def test_simple_case_2():
    result = count_words("Dongle")
    assert result == 1

# Test empty case
def test_empty_string():
    result = count_words("0")
    assert result == 1


