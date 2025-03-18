x=int(input())
count_divisor=0;
for i in range(1,x+1):
    if x%i==0:
        count_divisor+=1

print(count_divisor)

