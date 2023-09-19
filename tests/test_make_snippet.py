from lib.make_snippet import *

"""
If it is emty string should return empty string
"""
def test_emty_string():
    result = make_snippet("")
    assert result == ""

"""
If there is a string with 5 words then should return 1st 5 words
"""
def test_5_words():
    assert make_snippet('One two three four five') == 'One two three four five'

"""
If there is a string with more then 5 words then should return 1st 5 words 
+ '...'
"""
def test_6_words():
    assert make_snippet('One two three four five six') == 'One two three four five ...'

