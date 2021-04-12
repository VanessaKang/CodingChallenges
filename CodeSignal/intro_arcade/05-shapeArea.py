def shapeArea(n):
    """
    Description: Below we will define an n-interesting polygon. 
    Your task is to find the area of a polygon for a given n.
    
    Args: 
    n (integer): n - interesting polygon
    
    Returns:
    area (integer): The area of the n-interesting polygon
    
    Assumptions: 
    - n = 1 ≤ n < 10**4
    - n is never negative
    
    >>> shapeArea(1)
    1
    >>> shapeArea(2)
    5
    >>> shapeArea(3)
    13
    >>> shapeArea(4)
    21
    
    """
    
    total = 1
    for i in range(2, n + 1):
        total = total + 4*(i - 1)
    return total
