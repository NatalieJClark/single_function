Exercise One - Design Recipe
# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

def estimate_reading_time(text):
    # Calculates reading time of a text
    # Parameters: 
    #    text: a string representing humam-readable text
    # Returns:
    #    float: representing reading time
    pass

## 3. Create Examples as Tests

"""
Given a text of 200 words
It returns 1.0
"""
estimate_reading_time("...200..."):
# => 1.0

"""
Given a text of 400 words
It returns 2.0
"""
estimate_reading_time("...400..."):
# => 2.0

"""
Given a text of 300 words
It returns 1.5
"""
estimate_reading_time("...300..."):
# => 1.5

"""
Given an empty string
It will raise an error
"""
estimate_reading_time(""):
# Raises error: "Can't estimate reading time for an empty text."

## 4. Implement the Behaviour


Ensure all test function names are unique, otherwise pytest will ignore them!