import math

n=int(input())
i=n
while math.log(i,2) <= n:
    if n==i:
        print(math.ceil(math.log(i,2)))
    i=i+1
#print(math.log(n,2))
