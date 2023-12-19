import pytest
from lib.check_sentance_grammar import check_sentance_grammar

"""
Given a valid text, starting with a capital and ending with a full stop
It returns True
"""
def test_given_capital_and_full_stop_returns_true():
    result = check_sentance_grammar("Hello, it's nice to meet you.")
    assert result == True

"""
Given a text, starting with a lowercase letter and ending with a full stop
It returns False
"""
def test_given_lowercase_and_full_stop_returns_false():
    result = check_sentance_grammar("hello, it's nice to meet you.")
    assert result == False

"""
Given a valid text, starting with a capital and ending with a question mark
It returns True
"""
def test_given_capital_and_question_mark_returns_true():
    result = check_sentance_grammar("Hello, how are you?")
    assert result == True

"""
Given a valid text, starting with a capital and ending with an exclamation mark
It returns True
"""
def test_given_capital_and_exclamation_mark_returns_true():
    result = check_sentance_grammar("Hello, it's a fine day!")
    assert result == True

"""
Given a sentance starting with a capital letter, but ending without a full stop or other mark
It returns False
"""
def test_given_capital_and_no_ending_punctuation_returns_false():
    result = check_sentance_grammar("Hi, what's your name")
    assert result == False

"""
Given a sentance starting with a capital letter, but ending with a comma
It returns False
"""
def test_given_capital_and_ending_comma_returns_false():
    result = check_sentance_grammar("It's lovely weather,")
    assert result == False

"""
Given a sentance starting with a capital letter, but ending with a colon
It returns False
"""
def test_given_capital_and_ending_colon_returns_false():
    result = check_sentance_grammar("It's lovely weather:")
    assert result == False

"""
Given an empty string 
It raises an error message "Can't check the grammar of an empty string"
"""
def test_given_empty_string_raises_error():
    with pytest.raises(Exception) as e:
        check_sentance_grammar("")
    error_message = str(e.value)
    assert error_message == "Can't check the grammar of an empty string"
