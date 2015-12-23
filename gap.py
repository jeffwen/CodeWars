# Prime generators

# Faster implementation
def gap(gap,start,stop):
    not_prime = []
    prime = []
    for i in xrange(2, stop+1):
        for j in xrange(i*i, stop+1, i):
            not_prime.append(j)
        if (i>=start) and (i not in not_prime):
            try:
                if (i-prime[-1]==gap):
                    return [prime[-1],i]
            except:
                pass
            prime.append(i)

# Slow implementation    
def gap_1(gap,start,stop):
    not_prime = []
    last_prime = 2
    for i in xrange(2, stop+1):
        if i not in not_prime:
            if last_prime >= start and i-last_prime == gap:
                return [last_prime,i]
            for j in xrange(i*i, stop+1, i):
                not_prime.append(j)
            last_prime = i

# Fastest implementation 
def gap_2(gap,start,stop):
    last_prime = 2

    # only check from the start to the stop range
    for i in xrange(start, stop+1):
        prime = True

        # prime checker
        for j in xrange(2,int(stop**.5)+1):
            if i%j == 0:
                prime = False
                break

        # setting the last_prime and substituting the last prime/ calculating if gap matches
        if prime:
            if i - last_prime == gap:
                return [last_prime,i]
            else:
                last_prime = i

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
