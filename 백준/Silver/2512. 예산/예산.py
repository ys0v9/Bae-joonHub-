n = int(input())
budgets = list(map(int,input().split()))
limit = int(input())

def adjust(budgets, cap):
    total = 0
    for i in budgets:
        total += min(i, cap)
    return total

low = 0 
high = max(budgets)
answer = 0 

while low <= high:
    cap = (low+high)//2
    total = adjust(budgets, cap)
    if total > limit:
        high = cap -1
    else:
        answer = cap
        low = cap +1
print(answer)