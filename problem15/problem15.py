class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def problem15(x, y):
    if x == 20 or y == 20:
        return 1
    else:
        return problem15(x,y+1) + problem15(x+1, y)

problem15 = Memoize(problem15)

print(problem15(0,0))
