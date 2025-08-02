n = int(input())
a = n % 8
if n <= 5:
    print(n)
elif a == 1:
    print(1)
elif a == 0 or a == 2:
    print(2)
elif a == 7 or a == 3:
    print(3)
elif a == 6 or a == 4:
    print(4)
else:
    print(5)