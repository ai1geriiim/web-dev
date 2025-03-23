def no_teen_sum(sum):
    if 13<=sum<=19 and sum not in (15,16):
        return 0
    return sum
a,b,c=map(int,input().split(","))
result=no_teen_sum(a)+no_teen_sum(b)+no_teen_sum(c)
print(result)
