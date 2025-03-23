def close_far(a,b,c):
    if a==b-1 and b==c-1:
        return False
    elif a==b-1 and b<c:
        return True
    elif c==a-1 and b<c:
        return True
a,b,c=map(int,input().split(","))
print(close_far(a,b,c))
