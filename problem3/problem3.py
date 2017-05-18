def problem3(n):
    """returning the largest prime factor"""
    for i in range(2,n):
        if n%i == 0 and is_prime(n/i):
            return n/i


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

print(problem3(600851475143))
