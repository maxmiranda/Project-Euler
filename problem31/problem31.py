denoms = [1, 2, 5, 10, 20, 50, 100, 200]

def make_amt(n, last=200):
    if n ==0:
        return 1
    else:
        return sum([make_amt(n-denom, denom) for denom in denoms if denom <= n and denom <=last])

print(make_amt(200))
