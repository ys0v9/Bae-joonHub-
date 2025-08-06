n = int(input())
k = list(str(int(input())))
j = 0
h = 0
for i in k:
    i = int(i)
    if i % 2 == 0:
        j += 1
    else:
        h += 1

if j > h:
    print(0)
elif h > j:
    print(1)
else:
    print(-1)