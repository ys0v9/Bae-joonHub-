n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

cnt = 0

for i in size:
    cnt += i // t
    if i % t != 0:
        cnt += 1

print(cnt)
print(n // p, n % p)
