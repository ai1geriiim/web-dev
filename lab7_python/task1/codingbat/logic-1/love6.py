a,b=map(int,input().split())

sum=a+b
diff=a-b
if a==6 or b==6:
    print("True")
elif sum==6 or diff==6:
    print("True")
else:
    print("False")