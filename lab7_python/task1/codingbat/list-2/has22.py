my_list=eval(input())
found=False
for i in range(len(my_list)-1):
    if my_list[i]==2 and my_list[i+1]==2:
        found=True
    else:
        found=False
print(found)