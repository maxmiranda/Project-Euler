def fact(n):
    if n == 1 or n ==0:
        return 1
    else:
        return n * fact(n-1)


total = 0
for number in range(10,100000):
    if sum([fact(int(digit)) for digit in str(number)]) ==number:
        print(number)
        total = total + number

print(total)
