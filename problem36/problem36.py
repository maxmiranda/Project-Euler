def is_palindrome(n):
    i=n
    backwards = 0
    while i>0:
        backwards*= 10
        j = i %10
        i = i//10
        backwards+=j
    if backwards == n:
        return True
    return False

def binary(n):
    if n ==1:
        return 1
    if n %2 % 2 ==0 or n==2:
        return 10 * binary(n//2)
    bina = 0
    while n > 0:
        bina*=10
        bina+= n%2
        n = n//2
    return bina

total = 0
for i in range(1,1000000):
    if is_palindrome(i) and is_palindrome(binary(i)):
        print(i, binary(i))
        total += i

print(total)
