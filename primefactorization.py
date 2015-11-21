class PrimeFactorizer:
    def __init__(self, n):
        self.n = n
        self.factors = []
        d = 2
        while self.n > 1:
            while self.n%d == 0:
                self.n /= d
                self.factors.append(d)
            d += 1
            if d*d > self.n:
                if self.n > 1:
                    self.factors.append(self.n)
                break
            
