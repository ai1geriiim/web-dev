a,b=map(int,input().split())
if a<0 and b<0:
    print("True")
elif a>0 and b<0:
    print("False")
elif a<0 and b>0:
    print("True")
else:
    print("False")
