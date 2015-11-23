# Given a number, return the prime factors of the number. The question required the use of a class

class PrimeFactorizer:
    def __init__(self, n):
        self.n = n
        self.factors = []
        d = 2
        while self.n > 1:
            while self.n%d == 0:

                # if d is a factor of the number, then keep appending it to the factor list
                self.n /= d
                self.factors.append(d)

            # increment by 1 when the remainder is no longer zero
            d += 1

            # not strictly needed as incrementing will eventually find the prime factors; however, this speeds up the calculations
            # the remaining n is appended as it is a prime number
            if d*d > self.n:
                if self.n > 1:
                    self.factors.append(self.n)
                break # the break is necessary to stop the appending or else it will go until d == n and n !> 1
            
