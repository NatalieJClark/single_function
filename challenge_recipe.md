# {Exercise Two} Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._
def check_todo(text):
    # Parameters:
    #   text: a human-readable string
    # Return:
    #   Boolean: True if text includes "#TODO", False otherwise

Assume #TODO can appear anywhere in the given string


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

"""
Given an empty string
Raises an error "Can't check an empty string"
"""
check_todo("")
=> "Can't check an empty string"

"""
Given a string containing the word "#TODO"
Returns True
"""
check_todo("#TODO Walk the dog")
Return True

"""
Given a string containing the word "#todo"
Returns False
"""
check_todo("Walk the dog #todo")



_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
Ensure all test function names are unique, otherwise pytest will ignore them!