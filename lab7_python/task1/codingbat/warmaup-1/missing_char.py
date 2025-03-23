string,index=input().split()
index=int(index)
new_string=""
for i in range(len(string)):
    if i!=index:
        new_string+=string[i]
print(new_string)