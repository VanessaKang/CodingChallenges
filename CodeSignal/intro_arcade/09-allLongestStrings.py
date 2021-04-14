def allLongestStrings(inputArray):
    """
    Description: Given an array of strings, return another array containing all of its longest strings.
    
    Args: 
    inputArray (array.string): A non-empty array.
    1 ≤ inputArray.length ≤ 10
    1 ≤ inputArray[i].length ≤ 10
    
    Return: 
    array.stirng: Array of the longest strings, stored in the same order as in the inputArray.
    
    Assumptions: 
    - inputArray is not empty
    - outputArray should be same order as inputArray
    
    Examples:
    
    >>> allLongestStrings(["aba", "aa", "ad", "vcd", "aba"])
    ["aba", "vcd", "aba"]
    
    >>> allLongestStrings(["aba", "aa", "ad", "vcdc", "aba"])
    ["vcdc"]
    
    """
    
    longestdict = {}
    for element in inputArray:
        if not len(element) in longestdict:
            longestdict[len(element)] = [element]
        else:
            longestdict[len(element)].append(element)
    return longestdict[max(longestdict)]
    
