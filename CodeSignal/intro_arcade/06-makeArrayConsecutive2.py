def makeArrayConsecutive2(statues):
    """
    Description: Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, 
    each statue having an non-negative integer size. Since he likes to make things perfect, 
    he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one 
    exactly by 1. He may need some additional statues to be able to accomplish that. 
    Help him figure out the minimum number of additional statues needed
    
    Args:
    statues (array.integer): An array of distinct non-negative integers.
    
    Returns: 
    integer : minimal number of statues that need to be added to existing statues such that it contains every integer size from an interval 
    [L,R] (for some L,R) and no other sizes.
    
    Assumptions: 
    - 1 ≤ statues.length ≤ 10
    - 0 ≤ statues[i] ≤ 20
    
    >>> makeArrayConsecutive2([6, 2, 3, 8])
    3
    >>> makeArrayConsecutive2([2, 3, 6, 8])
    3
    
    """
        
    return (max(statues) - min(statues) + 1- len(statues))
    
