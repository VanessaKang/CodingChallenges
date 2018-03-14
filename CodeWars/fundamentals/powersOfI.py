def pofi(n):

    # Create a list of proper values
    myList = ['1', 'i', '-1', '-i']

    # Modulo will provide the correct index to list
    n = n % 4

    return myList[n]
