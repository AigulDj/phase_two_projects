from lib.manage_time import *

"""
Given empty string
It returns a 0
"""
def test_empty_string():
    result = manage_time("")
    assert result == 0

"""
Given a string of words
It returns time taken to read string of words
"""
def test_string_of_words():
    result = manage_time("one two three four five")
    assert result == 1.5