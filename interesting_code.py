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

def primefactors_1(n):
    factors = []
    d = 2
    while n > 1:
        while n%d == 0:
            n /= d
            factors.append(d)
        d += 1
        if d*d > n and n > 1:
            factors.append(n)
            break
    return factors

# Levenshtein distance (2-matrix row implementation)
# good resource: http://www.let.rug.nl/~kleiweg/lev/
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

# Long hand mutiplication implementation
def long_mult(x,y):
    xStr = str(x)
    yStr = str(y)
    aList = []
    for letters in yStr:
        aList.append([])
    for ydig in range(len(yStr)-1,-1,-1):
        store = 0
        for xdig in range(len(xStr)-1,-1,-1):
            calc = str(int(xStr[xdig])*int(yStr[ydig]) + store)
            if xdig == 0:
                aList[ydig].append(calc)
                continue
            if len(calc) > 1:
                aList[ydig].append(calc[-1])
                store = int(calc[0])
            else:
                aList[ydig].append(calc)
    reverse_a = aList[::-1]
    total = 0
    for row in range(len(aList)):
        total += int(''.join(reverse_a[row][::-1]) + ('0'*row))
    return total


# Sieve of Eratosthenes               
def primeSieve(sieveSize):
     # Returns a list of prime numbers calculated using
     # the Sieve of Eratosthenes algorithm.
     sieve = [True] * sieveSize
     sieve[0] = False # zero and one are not prime numbers
     sieve[1] = False

     # create the sieve
     for i in range(2, int((sieveSize)**0.5) + 1):
         pointer = i * 2
         while pointer < sieveSize:
             sieve[pointer] = False
             pointer += i

     # compile the list of primes
     primes = []
     for i in range(sieveSize):
         if sieve[i] == True:
             primes.append(i)

     return primes
 
