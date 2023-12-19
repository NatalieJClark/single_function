def check_sentance_grammar(text):
    if text == "":
        raise Exception("Can't check the grammar of an empty string")
    is_valid = text[0].isupper() and text[-1] in ".?!"
    return is_valid