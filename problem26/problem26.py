
def is_prime(n):
  if n%2 ==0:
      return False
  if n%3 == 0:
      return False
  square_root = int(n**0.5)
  f = 5
  while f <= square_root:
    if n%f == 0 or n%(f+2) == 0:
        return False
    f +=6
  return True

def recur(d):
    if is_prime(d):
        for n in range(1,d):
            if ((10**n)-1) % d ==0:
                return n
    return 0


longestRecur = [0,0]

for number in range(1,1000):
    if recur(number) > longestRecur[0]:
        longestRecur = [recur(number),number]
print(longestRecur)
