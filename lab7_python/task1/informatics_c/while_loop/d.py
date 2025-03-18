import math

n=int(input())
i=0
while pow(2,i)<=n:
    if pow(2,i)==n:
        print("YES")
        break
    i=i+1
else:
    print("NO")

