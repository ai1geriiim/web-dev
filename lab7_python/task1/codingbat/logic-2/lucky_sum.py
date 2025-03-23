a,b,c=map(int,input().split(","))
if a==13:
    print(b+c)
elif c==13:
    print(b+a)
elif b==13:
    print(a)
else:
    print(a+b+c)