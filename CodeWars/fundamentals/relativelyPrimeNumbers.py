def relatively_prime(n, l):
    # Find multiples for the number n
    nMultiples = [i for i in range(1, n + 1) if n % i == 0]

    # Find multiple in other numbers in array l and return numbers that dont have multiples that exists in nMultiples
    return [j for j in l if (set(nMultiples[1:]).intersection(set([a for a in range(1, j + 1) if j % a == 0])) == set())]
