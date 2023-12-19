import pytest
from lib.check_todo import check_todo

"""
Given an empty string
Raises an error "Can't check an empty string"
"""
def test_given_empty_string_raises_error():
    with pytest.raises(Exception) as e:
        check_todo("")
    error_message = str(e.value)
    assert error_message == "Can't check an empty string"

"""
Given a string containing the word "#TODO"
Returns True
"""
def test_string_containing_hashTODO():
    result = check_todo("#TODO Walk the dog")
    assert result == True

"""
Given a string containing the word "#todo"
Returns False
"""
def test_string_containing_hashtodo():
    result = check_todo("Walk the dog #todo")
    assert result == False