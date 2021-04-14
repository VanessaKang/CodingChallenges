def matrixElementsSum(matrix):
    """
    Description:
    Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, 
    your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).
    
    Args: 
    matrix (array.array.integer): A 2-dimensional array of integers representing the cost of each room in the building. 
    A value of 0 indicates that the room is haunted.
    1 ≤ matrix.length ≤ 5
    1 ≤ matrix[i].length ≤ 5
    0 ≤ matrix[i][j] ≤ 10
    
    Return: 
    Integer: total price of all the rooms that are suitable for the CodeBots to live in
    
    Assumptions: 
    - only the rooms that are 0 and below it are out of the question  (or any of the rooms below any of the free rooms)
    - Note that the free room in the final column makes the full column unsuitable for bots (not just the room directly beneath it
    - each row will be the same length
    
    >>> matrixElementsSum([[0, 1, 1, 2], 
                          [0, 5, 0, 0], 
                          [2, 0, 3, 3]])
    9

    >>>matrix = [[1, 1, 1, 0], 
                  [0, 5, 0, 1], 
                 [2, 1, 3, 10]]
    9
    """
    
    ghostcol = []
    total = 0
    rowlength = len(matrix[0])
    for row in matrix:
        for index in range(0, rowlength):
            if not index in ghostcol:
                if row[index] == 0:
                    ghostcol.append(index)
                else:
                    total+= row[index]
    return total
