speed=int(input())
is_birthday=input()=="True"

if speed<=65 and is_birthday==True:
    print("0")
elif speed<=60 and is_birthday==False:
    print("0")
elif 66<=speed<=85 and is_birthday==True:
    print("1")
elif 61<=speed<=80 and is_birthday==False:
    print("1")
elif speed>=86 and is_birthday==True:
    print("2")
elif speed>=81 and is_birthday==False:
    print("2")