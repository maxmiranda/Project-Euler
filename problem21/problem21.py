class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def d(n):
    "sum of proper divisors"
    total = 0
    for i in range(1,int(n/2 +1)):
        if n%i ==0:
            total += i
    return total

d= Memoize(d)

def amicables(limit):
    amicables =[]
    n= 1
    while n< limit:
        if d(d(n))== n and n!= d(n):
            amicables.append(n)
        n=n+1
    print(sum(amicables))

amicables(10000)
