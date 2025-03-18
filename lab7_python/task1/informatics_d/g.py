numbers=list(map(int,input().split()))
max_array=float('-inf')
max_index=-1
for i in range(len(numbers)):
    if numbers[i] > max_array:
        max_array = numbers[i]
        max_index=i #обновление индекса
print(max_array,max_index)






