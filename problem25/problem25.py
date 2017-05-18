def fib(prev, curr):
    count = 2
    while len(str(curr))< 1000:
        prev, curr = curr, prev + curr
        count+=1
    return count
print(fib(1,1))
