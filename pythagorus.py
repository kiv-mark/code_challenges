"""
First input will be the number of pythogorous triplets.
After that in each line pythagorous triplets will be provided seperated by space.
NOTE: The triplets shoud be cocurrent prime to each other.
"""

limit = int(raw_input())
result = []

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

for i in range(limit):
    sort_val = (map(int,raw_input().split()))
    
    if gcd(sort_val[0], sort_val[1]) == 1 and gcd(sort_val[1], sort_val[2]) == 1 and gcd(sort_val[0], sort_val[2]) == 1:
        if (sort_val[2] * sort_val[2]) == (sort_val[1] * sort_val[1]) + (sort_val[0] * sort_val[0]):
            result.append("YES")
        else:
            result.append("NO")

for k in result:
    print k

