import itertools
while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    k = nums[0]
    numbers = nums[1:]
    for i in itertools.combinations(numbers, 6):
        print(*i)
    print()