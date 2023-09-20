from lib.make_snippet import make_snippet

# A function called make_snippet that takes a string 
# as an argument and returns the first five words and 
# then a '...' if there are more than that.

"""
Given an empty string
It returns an empty string
"""
def test_given_empty_string_returns_empty_string():
    result = make_snippet("")
    assert result == ""

"""
Given a string of five words
It returns the same string
"""
def test_given_five_words_returns_same_string():
    result = make_snippet("My sentance has five words.")
    assert result == "My sentance has five words."

"""
Given a string of six words
It returns the first five words then a "..."
"""
def test_given_six_words_returns_first_five_and_ellipsis():
    result = make_snippet("Now my sentance has six words.")
    assert result == "Now my sentance has six..."
