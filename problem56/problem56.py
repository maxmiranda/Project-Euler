sums = []

for a in range(100):
    for b in range(100):
        sums +=  [sum([int(digit) for digit in str(a**b)])]

print(max(sums))
