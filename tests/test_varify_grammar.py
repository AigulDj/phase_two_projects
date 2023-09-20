import pytest
from lib.verify_grammar import *


"""
Given empty string
It returns er
"""
def test_emty_string_given():
    with pytest.raises(Exception) as e:
        verify_grammar("")
    error_message = str(e.value)
    assert error_message == "No text provided!"

"""
Sentence starts with a lowercase letter
It returns False
"""
def test_text_starts_with_lowercase():
    result = verify_grammar('hello world.')
    assert result == False

"""
Sentence ends with one of the wrong punctuation marks (e.g. ', : ; "  etc)
It returns False
"""
def test_text_ends_with_wrong_punctuation():
    result = verify_grammar('Hello world')
    assert result == False

"""
Sentence starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
It returns True
"""
def test_coorect_text():
    result = verify_grammar("Hello world!")
    assert result == True