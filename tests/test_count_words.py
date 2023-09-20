from lib.count_words import count_words

"""
Given an empty string
It returns 0
"""
def test_given_empty_string_returns_zero():
    result = count_words("")
    assert result == 0

"""
Given a string with three words
It returns 3
"""
def test_given_one_word_returns_1():
    result = count_words("one two three")
    assert result == 3

"""
Given a string with four words with punctuation
It returns 4
"""
def test_given_one_word_returns_1():
    result = count_words("one, two, three, four.")
    assert result == 4

"""
Given a string with five words delimited by commas
It returns 1
"""
def test_given_one_word_returns_1():
    result = count_words("one,two,three,four,five")
    assert result == 1