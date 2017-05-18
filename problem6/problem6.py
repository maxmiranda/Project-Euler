def problem6(n):
    sumOfSquares = sum([i**2 for i in range(1,n+1)])
    squareOfSum =  (sum([i for i in range(1, n+1)]))**2
    print(squareOfSum -sumOfSquares)

problem6(100)
