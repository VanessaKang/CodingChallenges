import math
def adjacentElementsProduct(inputArray):
    """
    Description:Given an array of integers, find the pair of adjacent elements that has the largest 
    product and return that product. 
    
    Args: 
    inputArray (array): array of integers containing at least two elements
    
    Returns:
    product (integer): largest product of adjacent elements
    
    Assumptions: 
    - 2 ≤ inputArray.length ≤ 10
    - -1000 ≤ inputArray[i] ≤ 1000
    
    >>> adjacentElementsProduct([3, 6, -2, -5, 7, 3])
    21
    >>> adjacentElementsProduct([0, -1, -2, -5, -9, -10])
    90
    >>> adjacentElementsProduct([0, 9, 2, 5, 9, 10])
    90
    >> adjacentElementsProduct([6, -1,])
    6
    
    """
    
    index = 0
    m_number = -math.inf
    
    while index + 1 < len(inputArray):
        if inputArray[index] * inputArray[index+1] > m_number:
             m_number = inputArray[index] * inputArray[index+1]
        else: 
            index += 1
    
    return m_number

