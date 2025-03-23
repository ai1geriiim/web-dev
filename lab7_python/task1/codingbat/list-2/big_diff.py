my_list=input()
num=[int(n) for n in my_list.strip('[]').split(',')]
max_num=float('-inf')
min_num=float('inf')
for i in num:
    if i>max_num:
        max_num=i
    if i<min_num:
        min_num=i
print(max_num-min_num)