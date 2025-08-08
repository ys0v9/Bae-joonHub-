import sys
input = sys.stdin.readline

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    max = n

    while n != 1:

        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1

        if n > max:
            max = n

    results.append(str(max))

print('\n'.join(results))
