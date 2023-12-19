# A function called count_words that takes a string as an argument 
# and returns the number of words in that string.

def count_words(str):
    words_list = str.split()
    number_of_words = len(words_list)
    return number_of_words