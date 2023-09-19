import pytest
from lib.manage_time import *

"""
Given empty string
It returns an error message
"""
def test_empty_string():
    with pytest.raises(Exception) as e:
        manage_time("")
    error_message = str(e.value)
    assert error_message == "No text given!"

"""
Given a string of words
It returns time taken to read string of words
"""
def test_string_of_words():
    result = manage_time("one two three four five")
    assert result == 1.5