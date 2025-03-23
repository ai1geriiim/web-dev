from collections import Counter
def top_three_common_chars(s):
    count = Counter(s)
    sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    for char, freq in sorted_count[:3]:
        print(f"{char} {freq}")
s=input()
print(top_three_common_chars(s))




