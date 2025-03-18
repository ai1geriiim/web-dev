numbers=list(map(int,input().split()))
count_larger=0
for i in range(len(numbers)-1):#не доходим до последнего элемента
    if numbers[i]>numbers[i+1]:
        count_larger+=1
print(count_larger)