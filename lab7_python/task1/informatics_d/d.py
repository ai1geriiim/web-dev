numbers=list(map(int,input().split()))
max1_array=float('-inf')
max2_array=float('-inf')
for i in numbers:
    if i>max1_array:
        max2_array=max1_array
        max1_array=i
    elif i>max2_array and i!=max1_array:
        max2_array=i
print(max1_array,end=" ")
print(max2_array)





