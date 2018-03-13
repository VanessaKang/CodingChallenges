import random

def random_case(x):

    #Create an Empty String
    newString = ""

    #Go through characters in string and concatenate randomly selected upper or lower
    for i in x:
        newString+=random.choice([i.upper(), i.lower()])
    return newString
