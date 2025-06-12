import sys

n = int(sys.stdin.readline())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

points.sort()

for x, y in points:
    print(x, y)