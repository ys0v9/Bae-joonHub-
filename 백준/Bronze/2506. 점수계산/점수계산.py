n = int(input())
sum = 0
result = 0
l = list(map(int, input().split()))

for i in range(n):
    if l[i] == 1:
        sum += 1
        result += sum
    else:
        sum = 0

print(result)