import sys
sys.setrecursionlimit(100000)
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def is_prime(n):
    if n ==2 or n==3:
        return True
    if n%2 ==0 or n%3 == 0:
        return False
    square_root = int(n**0.5)
    f = 5
    while f <= square_root:
        if n%f == 0 or n%(f+2) == 0:
            return False
        f +=6
    return True


def spiral():
    diags = 5
    prime_diags = 3
    i = 3
    while prime_diags/diags >= .1:
        i +=2
        diags +=4
        for j in range(1,4):
            if is_prime(i**2-j*(i-1)):
                prime_diags +=1
    print(i)


print(spiral())
