n, m = map(int, input().split())
trees = list(map(int, input().split()))

def cut_trees(trees, mid):
    total = 0
    for i in trees:
        if i > mid:
            total += i - mid
    return total


low, high = 0, max(trees)
result = 0

while low <= high:
    mid = (low + high) // 2
    total = cut_trees(trees, mid)

    if total >= m:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
