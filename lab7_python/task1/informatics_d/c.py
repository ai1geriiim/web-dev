numbers=list(map(int,input().split()))
count_positive=0
for i in numbers:
    if i>0:
        count_positive+=1
print(count_positive)