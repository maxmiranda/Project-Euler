import operator

sums_a_b_c =[0 for i in range(1001)]

for c in range(700):
    for b in range(c):
        for a in range(b):
            if a**2 + b**2 == c**2 and a+b+c <= 1000:
                sums_a_b_c[a+b+c]+=1

max_index, max_value = max(enumerate(sums_a_b_c), key=operator.itemgetter(1))

print(max_index)
