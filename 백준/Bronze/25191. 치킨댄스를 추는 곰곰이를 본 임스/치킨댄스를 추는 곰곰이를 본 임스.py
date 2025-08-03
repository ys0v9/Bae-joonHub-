n = int(input())
a, b = map(int,input().split())
cnt = 0
cnt += (a//2)
cnt += b
if cnt > n:
    print(n)
else:
    print(cnt)