t1, e1, f1 = map(int,input().split())
t2, e2, f2 = map(int,input().split())

a = t1*3 + e1*20 + f1*120
b = t2*3 + e2*20 + f2*120

if a>b:
    print("Max")
elif a == b:
    print("Draw")
else:
    print("Mel")