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
    for i in range(1,int(n**.5)+1):
        if n/i == i:
            total += i
        elif n%i ==0:
            total += i
            total += n/i
    return total - n

d= Memoize(d)

abuns = [i for i in range(28123) if d(i)>i]

set_abuns = set(abuns)
def is_abundant_sum(n):
    for i in abuns:
        if i < n and (n-i) in set_abuns:
            return True
    return False

is_abundant_sum = Memoize(is_abundant_sum)

ints = [i for i in range(28123) if not is_abundant_sum(i)]


print(sum(ints))
