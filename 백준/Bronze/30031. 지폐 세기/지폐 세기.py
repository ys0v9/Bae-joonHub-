n = int(input())
money = 0
for _ in range(n):
    g, s = map(int,input().split())
    if g == 136:
        money += 1000
    elif g == 142:
        money += 5000
    elif g == 148:
        money += 10000
    else:
        money += 50000
print(money)