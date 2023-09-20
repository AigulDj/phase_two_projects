def verify_grammar(text):
    if text == "":
        raise Exception("No text provided!")
    else:
        return text[0].isupper() and text[-1] in '.!?'
    
