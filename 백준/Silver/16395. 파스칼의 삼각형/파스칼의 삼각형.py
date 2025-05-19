n, k= map(int,input().split())

numbers = []

for i in range(n):
    row = []
    for j in range(i+1):
        row.append(1)
    numbers.append(row)

for i in range(2, n):
    for j in range(1, i):
        numbers[i][j] = numbers[i-1][j-1] + numbers[i-1][j]

print(numbers[n-1][k-1])