f = open('p042_words.txt', 'r')
words = f.read().replace('"', '').split(',')

position_sums = [sum(ord(char) -ord('A') +1 for char in word)
 for word in words]

triangles = [.5*n*(n+1) for n in range(1000)]

def is_triangle(n):
    return n in triangles

position_sums= [position for position in position_sums
if is_triangle(position)]

print(len(position_sums))
