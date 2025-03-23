def round10(num):
    return (num + 5) // 10 * 10
a, b, c = map(int, input().split())
print(round10(a) + round10(b) + round10(c))
