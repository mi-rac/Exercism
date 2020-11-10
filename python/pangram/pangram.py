def is_pangram(sentence):
    """
    Checks if sentence contains all letters in the alphabet at least once.
    """
    from string import ascii_lowercase as letters

    #building dictionary for alphabet:
    d = {}
    for x in letters:
        d[x] = 0

    #looping through the letters in the sentence:
    for letter in sentence.lower():
        if letter.isalpha():
            d[letter] += 1

    #checking for missing letters:
    if 0 in d.values():
        return False
    else:
        return True
