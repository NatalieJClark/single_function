import pytest
from lib.estimate_reading_time import estimate_reading_time
"""
Given a text of 200 words
It returns 1.0
"""
def test_two_hundred_words():
    text = " ".join(["word" for i in range(200)])
    result = estimate_reading_time(text)
    assert result == 1.0

"""
Given a text of 400 words
It returns 2.0
"""
def test_four_hundred_words():
    text = " ".join(["word" for i in range(400)])
    result = estimate_reading_time(text)
    assert result == 2.0

"""
Given a text of 300 words
It returns 1.5
"""
def test_three_hundred_words():
    text = " ".join(["word" for i in range(300)])
    result = estimate_reading_time(text)
    assert result == 1.5

"""
Given an empty string
It will raise an error
"""
def test_empty_text():
    with pytest.raises(Exception) as e:
        estimate_reading_time("")
    error_message = str(e.value)
    assert error_message == "Can't estimate reading time for an empty text."