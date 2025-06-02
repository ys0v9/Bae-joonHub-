arr = []
for i in range(7):
    n = int(input())
    if n % 2 != 0:
        arr.append(n)

if arr == []:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))