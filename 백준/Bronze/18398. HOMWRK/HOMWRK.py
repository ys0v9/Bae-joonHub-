t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n):
        a, b = map(int, input().split())
        print(a + b, a * b)