class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def pandig(x, y, product):
    string = str(x) +str(y) +str(product)
    if ''.join(sorted(string)) == '123456789':
        return True
    else:
        return False

pandig= Memoize(pandig)

pandigs = []
for i in range(10000):
    for j in range(10000):
        if i*j < 987654 and pandig(i,j, i*j):
            pandigs.append(i*j)
            print(i*j)
pandigs = set(pandigs)

print(sum(list(pandigs)))
