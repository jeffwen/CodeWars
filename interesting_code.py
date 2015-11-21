# Prime Factorization
def primefactors(n):
    factors = []
    d = 2
    while n > 1:
        while n%d == 0:
            n /= d
            factors.append(d)
        d += 1
        if d*d > n:
            if n > 1:
                factors.append(n)
            break
    return factors
