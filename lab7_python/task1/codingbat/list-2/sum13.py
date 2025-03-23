my_list=eval(input())
filtered_list=[x for x in my_list if x!=13]
print(sum(filtered_list))