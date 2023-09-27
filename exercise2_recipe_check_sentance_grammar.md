# {Exercise Two} Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

We'll assume the given text is only one sentance.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def check_sentance_grammar(text):
    # Parameters:
    #   text: a string representing a human-readable sentance
    # Returns:
    #   a boolean: True if valid, False otherwise


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

"""
Given a valid text, starting with a capital and ending with a full stop
It returns True
"""
check_sentance_grammar("Hello, it's nice to meet you.")
=> True

"""
Given a valid text, starting with a capital and ending with a question mark
It returns True
"""
check_sentance_grammar("Hello, how are you?")
=> True

"""
Given a valid text, starting with a capital and ending with an exclamation mark
It returns True
"""
check_sentance_grammar("Hello, it's a fine day!")
=> True

"""
Given a sentance starting with a capital letter, but ending without a full stop or other mark
It returns False
"""
check_sentance_grammar("Hi, what's your name")
=> False

"""
Given a sentance starting with a capital letter, but ending with a comma
It returns False
"""
check_sentance_grammar("It's lovely weather,")
=> False

"""
Given a sentance starting with a capital letter, but ending with a colon
It returns False
"""
check_sentance_grammar("It's lovely weather:")
=> False

"""
Given an empty string 
It raises an error
"""
check_sentance_grammar("")
=> Raises error: "Can't check the grammar of an empty string"

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
Ensure all test function names are unique, otherwise pytest will ignore them!