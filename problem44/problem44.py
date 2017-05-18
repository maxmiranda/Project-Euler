pent_numbers = [n*(3*n-1)/2 for n in range(1,100000)]

pents =set(pent_numbers)
min_diff =10000000000000000000
for pent1 in pent_numbers:
    for pent2 in pent_numbers:
        if pent1 > pent2 and (pent1 + pent2) in pents and (pent1 - pent2) in pents:
            print(abs(pent1-pent2), pent1, pent2)
