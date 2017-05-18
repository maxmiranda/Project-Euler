class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def is_prime(n):
  if n < 0:
      return False
  if n%2 ==0:
      return False
  if n%3 == 0:
      return False
  square_root = int(n**0.5)
  f = 5
  while f <= square_root:
    if n%f == 0 or n%(f+2) == 0:
        return False
    f +=6
  return True

def quadratic_check(a,b):
    counter = 0
    for i in range(80):
        if is_prime(i**2 + a*i + b):
            counter +=1
        else:
            return counter

maximum = [0,0]
for i in range(999,-1000, -2):
    for j in range(999,-1000, -2):
        if quadratic_check(i, j) > quadratic_check(maximum[0],maximum[1]):
            maximum = [i,j]

print(maximum[0] * maximum[1])
