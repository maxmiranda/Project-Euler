def sumOfDigits(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n= n//10
    print(sum(digits))

sumOfDigits(2**1000)
