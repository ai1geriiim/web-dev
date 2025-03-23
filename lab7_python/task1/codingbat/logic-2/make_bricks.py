def make_bricks(small, big, goal):
    max_big = min(big, goal // 5)
    return (goal - max_big * 5) <= small
small,big,goal = map(int, input().split(","))
print(make_bricks(small, big, goal))