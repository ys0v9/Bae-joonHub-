primes=[True]*(2*123456+1)
primes[0]=False
primes[1]=False
for i in range(2,2*123456+1):
    if primes[i]==True:
        for j in range(i*i,2*123456+1,i):
            primes[j]=False
n=int(input())
while n !=0:
    cnt=0
    for i in range(n+1,2*n+1):
        if primes[i]==True:
            cnt +=1
    print(cnt)
    n=int(input())