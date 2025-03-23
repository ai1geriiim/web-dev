string=input()
result=""
for i in range(len(string)):
    result+=string[:i+1]
print(result)
