from itertools import combinations
n = int(input())
decreasing_numbers = []

for length in range(1, 11):
    for i in combinations(range(10), length):
        num = ''.join(map(str, sorted(i, reverse=True)))
        decreasing_numbers.append(int(num))

if n>=len(decreasing_numbers):
    print(-1)
else:
    print(sorted(decreasing_numbers)[n])
