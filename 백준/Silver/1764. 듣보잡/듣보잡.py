n,m=map(int,input().split())
nm={}
for i in range(n):
    name=input().strip()
    nm[name]=True
result=[]
for i in range(m):
    name=input().strip()
    if nm.get(name, False):
        result.append(name)
result.sort()
print(len(result))
for name in result:
    print(name)