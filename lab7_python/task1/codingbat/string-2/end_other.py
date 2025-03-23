string1,string2=input().lower().split(",")
if string1 in string2 or string2 in string1:
    print("True")
else:
    print("False")