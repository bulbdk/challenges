from data import DICTIONARY, LETTER_SCORES

def load_words(file_name):
    """Load dictionary into a list and return list"""
    wordfile = open(file_name,"r")
    clean_word_list = [i[:-1] for i in wordfile]
    wordfile.close()
    return clean_word_list


def calc_word_value():
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    pass

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    ord_liste = load_words("01\dictionary.txt")
    
    pass # run unittests to validate
