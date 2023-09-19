def make_snippet(string):
    word_count = len(string.split())
    five_words = ' '.join(string.split()[:5])

    if word_count > 5:
        return five_words + ' ...'
    else:
        return five_words
