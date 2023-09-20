EXERCISE 1

1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.
"""
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.
"""

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

# EXAMPLE

def manage_time(text):
    """return time taken to read texts

    Parameters: (string)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (return float/int)
        a number (e.g. ["1.30"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
3. Create Examples as Tests
Make a list of examples of what the function will take and return.

# EXAMPLE
"""
Given empty string
It returns a 0
"""
manage_time("") => 0

"""
Given a single word
It returns time taken to read
"""
manage_time("word") => 0.3

1 word = 0.3 secs
200 words = 60 secs

"""

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.manage_time import *

"""
Given empty string
It returns a 0
"""
def test_empty_string():
    result = manage_time("")
    assert result == 0



EXERCISE 2

1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.
"""
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
"""
We will ignore any intermediate sentences

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

def verify_grammar(text):
    # Parameters:
    #   text: a string representing human-readable text (e.g. "Hello world!")
    # Returns:
    #   bolean, true if valid, false othervise

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.

3. Create Examples as Tests
Make a list of examples of what the function will take and return.

"""
Given empty string
It returns error message
"""
verify_grammar("") => No text provided!

"""
Sentence starts with a lowercase letter
It returns False
"""
verify_grammar("hello world") => False

"""
Sentence ends with one of the wrong punctuation marks (e.g. ', : ; "  etc)
It returns False
"""
verify_grammar("Hello world:") => False

"""
Given a valid sentence  with a capital letter and correct punctuation marks
It returns True
"""
verify_grammar("Hello word!") => True


4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE


