from lib.e_extractor import e_extractor

"""
Given an empty string
It returns an empty string
"""
def test_given_an_empty_string_returns_empty():
    result = e_extractor("")
    assert result == ""

"""
Given a string without any "e"s in it
It returns the same string it was given
"""
def test_given_no_es_returns_same():
    result = e_extractor("python")
    assert result == "python"

"""
Given a string with one e in it
It returns that string with that e relocated to the start
"""
def test_given_one_e_returns_string_with_e_at_start():
    result = e_extractor("yellow")
    assert result == "eyllow"

"""
Given a string with multiple "e"s in it
It returns the string with all the "e"s relocated to the start
"""
def test_given_mutliple_es_return_string_with_all_es_at_start():
    result = e_extractor("elephant")
    assert result == "eelphant"

"""
Given a string with "e"s already at the start
It returns the same string
"""
def test_given_es_at_start_return_same_string():
    result = e_extractor("epiphany")
    assert result == "epiphany"