temp=int(input())
is_summer=input().lower()=="true"
if (60<=temp<=90 and not is_summer) or (60<=temp<=100 and is_summer):
    print("True")
else:
    print("False")