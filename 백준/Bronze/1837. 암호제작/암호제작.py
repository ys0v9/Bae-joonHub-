p, k = map(int,input().split())

for i in range(2,k):
    if p % i == 0:
        print("BAD", i)
        break
else:
    print("GOOD")