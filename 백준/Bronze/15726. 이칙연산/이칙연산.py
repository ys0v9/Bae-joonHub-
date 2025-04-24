a, b, c = map(int,input().split())
mulAndDis=(a*b)/c
disAndMul=(a/b)*c
print(max(int(mulAndDis),int(disAndMul)))