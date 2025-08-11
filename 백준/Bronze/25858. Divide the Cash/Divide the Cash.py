n, d = map(int, input().split())
problems = [int(input()) for _ in range(n)]

total_problems = sum(problems)
dollars_per_problem = d // total_problems

for p in problems:
    print(p * dollars_per_problem)
