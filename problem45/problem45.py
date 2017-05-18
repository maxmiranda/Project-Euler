tri_numbers = [n*(n+1)/2 for n in range(286,1000000)]
pent_numbers = [n*(3*n -1)/2 for n in range(166,100000)]
hex_numbers = [n*(2*n-1) for n in range(144, 1000000)]

pents =set(pent_numbers)
hexs = set(hex_numbers)

for tri in tri_numbers:
    if tri in pents and tri in hexs:
        print(tri)
