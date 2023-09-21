def estimate_reading_time(text):
    if text == "":
        raise Exception("Can't estimate reading time for an empty text.")
    words_list = text.split()
    reading_time = len(words_list)/200
    return reading_time