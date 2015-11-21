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

# Levenshtein distance (2-matrix row implementation)
# god resource: http://www.let.rug.nl/~kleiweg/lev/
def levenshtein(s, t):
        if s == t: return 0
        elif len(s) == 0: return len(t)
        elif len(t) == 0: return len(s)
        v0 = [None] * (len(t) + 1)
        v1 = [None] * (len(t) + 1)
        for i in range(len(v0)):
            v0[i] = i
        for i in range(len(s)):
            v1[0] = i + 1
            for j in range(len(t)):
                cost = 0 if s[i] == t[j] else 1
                v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
            for j in range(len(v0)):
                v0[j] = v1[j] 
        return v1[len(t)]
