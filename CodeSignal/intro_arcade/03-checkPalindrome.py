def checkPalindrome(inputString):
    """
    Description: Given the string, check if it is a palindrome.
    
    Args: 
    
        inputString (str): A non-empty string consisting of lowercase characters.
        
    Returns: 
        bool: True/False indicating if its a Palindrome or not
        
    Assumptions: 
    - All lowercase non-empty characters
    - All characters are letters
    
    Examples: 
    
    >>> checkPalindrome("aabaa")
    True
    >>> checkPalindrome("abac")
    False
    >>> checkPalindrome("a")
    True
    
    """
    
    fptr = 0
    bptr = len(inputString) - 1

    while fptr < bptr:
        if inputString[fptr] != inputString[bptr]:
            return False
        else:
            fptr += 1
            bptr -= 1
        
    return True
    
