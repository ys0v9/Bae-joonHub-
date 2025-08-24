n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

best = points[0]

for p in points:
    if p[1] < best[1] or (p[1] == best[1] and p[0] < best[0]):
        best = p

print(best[0], best[1])
