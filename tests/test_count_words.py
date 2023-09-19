from lib.count_words import *

"""
If it is an empty string provided, 
should return 0
"""
def test_emty_string_given_return_zero():
    assert count_words("") == 0

"""
if it is a string given,
should return a number of words in it
"""
def test_string_given_return_word_count():
    assert count_words('One two three') == 3