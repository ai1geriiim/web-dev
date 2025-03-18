numbers=list(map(int,input().split()))
for i in range(0,len(numbers),2): #перебирает только четные индексы 
    print(numbers[i],end=" ")

