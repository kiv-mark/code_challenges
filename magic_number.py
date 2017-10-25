def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)
         
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

count = 0
number = int(raw_input())

import pdb; pdb.set_trace()

for i in range(1, number+1):
    for k in range(1, (number+1)*2):
        if gcd(i, k) == 1 and (i * k) == factorial(i):
            count = count + 1

print count
