file = open('p022_names.txt', 'r')
names = file.read().replace('"','').split(',')
names.sort()

alph_scores = [sum(ord(char) -ord('A') +1 for char in name) for name in names]
total =0
for i in range(len(alph_scores)):
    total += alph_scores[i] * (i+1)

print(total)
