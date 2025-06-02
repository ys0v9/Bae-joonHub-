import itertools
n, m = map(int,input().split())
nums = list(range(1,n+1))
for i in itertools.combinations(nums,m):
    print(*i)