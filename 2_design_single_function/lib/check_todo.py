def check_todo(text):
    if text == "":
        raise Exception("Can't check an empty string")
    return "#TODO" in text
    