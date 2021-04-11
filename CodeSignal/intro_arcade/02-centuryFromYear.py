def centuryFromYear(year):
    """  
    Descriptions: Given a year, return the century it is in. 
      
    Args:
        year (int): Positive integer given by user

    Returns:
        integer: The number of the century the year is in.
    
    Assumptions: 
    - Input: Positive Integer, designating the year
    - Input: Guaranteed constraints (1 ≤ year ≤ 2005)
    
    Examples:
    
    >>>centuryFromYear(1905)
    20
    
    >>>centuryFromYear(1700)
    17
    
    """
    
    if year%100 == 0: 
        return year//100
    else:
        return year//100 + 1
