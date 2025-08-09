n = int(input())
plan = list(map(int, input().split()))
study = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if plan[i] <= study[i]:
        cnt += 1

print(cnt)