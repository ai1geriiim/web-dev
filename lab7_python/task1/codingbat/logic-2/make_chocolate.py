def make_chocolate(small, big, goal):
    max_big = min(big, goal // 5)
    remainder = goal - (max_big * 5)
    return remainder if remainder <= small else -1
small,big,goal = map(int, input().split(","))
print(make_chocolate(small, big, goal))