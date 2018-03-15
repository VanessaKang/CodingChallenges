def DNA_strand(dna):
    # Creating a Dictionary of Complements
    dictionary = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    # Access each character and change it with its complements
    return "".join(dictionary[dna[i]] for i in range(len(dna)))
