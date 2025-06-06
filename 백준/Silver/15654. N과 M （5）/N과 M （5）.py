import itertools
n, m = map(int,input().split())
num = list(map(int,input().split()))
for i in sorted(itertools.permutations(num,m)):
    print(*i)