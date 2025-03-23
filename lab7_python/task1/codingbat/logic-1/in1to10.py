n = int(input())
outside_mode = input().strip().lower() == "true"
if outside_mode:
    result = n <= 1 or n >= 10
else:
    result = 1 <= n <= 10

print(result)
