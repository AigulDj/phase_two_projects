def manage_time(text):
    if text == "":
        raise Exception ("No text given!")
    else:
        number_of_words = len(text.split())
        calculate_seconds = number_of_words * 0.3
        return calculate_seconds
        